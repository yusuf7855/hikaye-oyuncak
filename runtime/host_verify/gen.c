// PC generator: same C inference as the ESP32, plus temperature/top-k sampling.
// usage: gen <model.bin> <n_tokens> <temperature> <top_k> <seed> <rep_penalty> [-b id,id,...] <prompt ids...>
// -b: banned token ids (e.g. names of figures that were not scanned); their logits are masked
// before sampling. On the ESP32 this is the same ~20-entry list, applied once per token.
// rep_penalty > 1 lowers the odds of any token used in the last REP_WINDOW tokens (1 = off);
// cheap enough for the ESP32: one pass over a 64-entry ring buffer per token.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include "../llm.h"

#define REP_WINDOW 64

static uint8_t *read_file(const char *p, size_t *n) {
  FILE *f = fopen(p, "rb"); if (!f) { perror(p); exit(1); }
  fseek(f, 0, SEEK_END); *n = ftell(f); fseek(f, 0, SEEK_SET);
  uint8_t *b = malloc(*n); if (fread(b, 1, *n, f) != *n) exit(1); fclose(f); return b;
}

static int pick(const float *lg, int V, float temp, int k) {
  int best = 0; for (int v = 1; v < V; v++) if (lg[v] > lg[best]) best = v;
  if (temp <= 0) return best;
  int *idx = malloc(k * sizeof(int)); int n = 0;
  for (int v = 0; v < V; v++) {          // keep top-k by insertion
    int j = n < k ? n++ : k;
    if (j == k && lg[v] <= lg[idx[k - 1]]) continue;
    if (j == k) j = k - 1;
    while (j > 0 && lg[idx[j - 1]] < lg[v]) { idx[j] = idx[j - 1]; j--; }
    idx[j] = v;
  }
  double *p = malloc(n * sizeof(double)), sum = 0;
  for (int i = 0; i < n; i++) sum += p[i] = exp((lg[idx[i]] - lg[best]) / temp);
  double r = (double)rand() / RAND_MAX * sum; int out = idx[n - 1];
  for (int i = 0; i < n; i++) if ((r -= p[i]) <= 0) { out = idx[i]; break; }
  free(idx); free(p); return out;
}

int main(int argc, char **argv) {
  if (argc < 8) { fprintf(stderr, "usage: gen model.bin n temp topk seed rep ids...\n"); return 2; }
  size_t nb; uint8_t *buf = read_file(argv[1], &nb);
  Model m; if (llm_load(buf, &m)) { fprintf(stderr, "bad magic\n"); return 1; }
  int N = atoi(argv[2]); float temp = atof(argv[3]); int K = atoi(argv[4]);
  srand(atoi(argv[5]));
  float rep = atof(argv[6]);
  int recent[REP_WINDOW], n_recent = 0;
  int ban[512], n_ban = 0, first_id = 7, with_logp = 0;
  for (;;) {  // options: -b id,id,...  (banned tokens)   -l  (also print log-prob of each sampled token)
    if (argc > first_id + 1 && strcmp(argv[first_id], "-b") == 0) {
      for (char *t = strtok(argv[first_id + 1], ","); t && n_ban < 512; t = strtok(NULL, ",")) ban[n_ban++] = atoi(t);
      first_id += 2;
    } else if (argc > first_id && strcmp(argv[first_id], "-l") == 0) {
      with_logp = 1; first_id += 1;
    } else break;
  }
  int D = m.c.dim, L = m.c.n_layers, P = m.c.ple_dim, F = m.c.ffn, V = m.out_vocab, S = m.c.seq_len;
  Scratch s;
  s.x = malloc(D * 4); s.h = malloc((F > D ? F : D) * 4);
  s.qkv = malloc(3 * D * 4); s.att = malloc(D * 4);
  s.g1 = malloc(F * 4); s.g2 = malloc((P > F ? P : F) * 4);
  s.ple = malloc(L * P * 4); s.tmpP = malloc(L * P * 4); s.trow = malloc(L * P * 4);
  s.logits = malloc(V * 4); s.scores = malloc(S * 4);
  s.kcache = malloc((size_t)L * S * D * 4); s.vcache = malloc((size_t)L * S * D * 4);
  int pos = 0, tok = 0;
  for (int i = first_id; i < argc; i++) {
    tok = atoi(argv[i]);
    recent[n_recent++ % REP_WINDOW] = tok;
    llm_forward(&m, tok, pos++, &s);
  }
  clock_t t0 = clock(); int made = 0;
  for (int step = 0; step < N && pos < S; step++) {
    if (rep > 1.f) {  // CTRL-style: shrink positive logits, push negative ones further down
      int n = n_recent < REP_WINDOW ? n_recent : REP_WINDOW;
      for (int i = 0; i < n; i++) {
        int dup = 0;  // penalise each distinct token once, not once per occurrence
        for (int j = 0; j < i && !dup; j++) dup = recent[j] == recent[i];
        if (dup) continue;
        float *l = &s.logits[recent[i]];
        *l = *l > 0 ? *l / rep : *l * rep;
      }
    }
    for (int i = 0; i < n_ban; i++) if (ban[i] >= 0 && ban[i] < V) s.logits[ban[i]] = -1e30f;
    tok = pick(s.logits, V, temp, K);
    recent[n_recent++ % REP_WINDOW] = tok;
    if (with_logp) {  // model confidence in its own choice: used to rank pre-generated candidates
      float mx = s.logits[0]; for (int v = 1; v < V; v++) if (s.logits[v] > mx) mx = s.logits[v];
      double z = 0; for (int v = 0; v < V; v++) z += exp(s.logits[v] - mx);
      printf("%d %.4f\n", tok, s.logits[tok] - mx - log(z));
    } else printf("%d\n", tok);
    fflush(stdout);
    llm_forward(&m, tok, pos++, &s); made++;
  }
  fprintf(stderr, "%d tokens, %.1f tok/s\n", made, made / ((double)(clock() - t0) / CLOCKS_PER_SEC));
  return 0;
}
