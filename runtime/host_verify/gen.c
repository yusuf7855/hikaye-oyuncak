// PC generator: same C inference as the ESP32, plus temperature/top-k sampling (../ornekle.h, shared
// with the firmware).
// usage: gen <model.bin> <n_tokens> <temperature> <top_k> <seed> <rep_penalty> [options] <prompt ids...>
// options (any order, before the prompt ids; with none given the output is the same as before they existed):
//   -b id,id,...  banned token ids (e.g. names of figures that were not scanned); their logits are masked
//                 before sampling. On the ESP32 this is the same ~20-entry list, applied once per token.
//   -N id,id,...  token ids banned only in the generated story body, e.g. the newline tokens 199 (Ċ) and
//                 9491 (ĠĊ) of the current tokenizer. The prompt carries the whole header, so here every
//                 generated token is body.
//   -P            prompt tokens stay out of the repetition window (default: they fill it), so the figure and
//                 theme words of the header are not penalised when the story repeats them.
//   -l            print "<id> <log-prob>" per sampled token instead of "<id>"; the log-prob is taken after
//                 the repetition penalty and the bans.
//   -e id         stop right after sampling (and printing) this token, e.g. <|endoftext|>; the tokens printed
//                 before it are the same as without -e, only the discarded tail is not generated.
//   -S nl         plan mode (E3): the prompt ends with "\nSorun:"; the model first writes the plan lines and
//                 then two nl tokens in a row (nl = 199, Ċ), and the story body starts after them. Plan tokens
//                 never enter the repetition window (at the body start it holds what it held when the plan
//                 began: the prompt unless -P) and the -N bans apply only in the body. If ORNEKLE_PLAN_SINIR
//                 (48) tokens pass without reaching the body, generation stops. Whenever generation ends
//                 without a body (that limit, -e, n or the context), "plan_bozuk" is printed to stderr (exit
//                 code 0). stdout is unchanged: one line per token, plan and "nl nl" included; the caller splits.
//   -W k          only the first k prompt tokens enter the repetition window (-P wins). uret.py's oracle plan
//                 condition gives the whole plan in the prompt and passes k = the "…\nSorun:" prefix, so the
//                 given plan stays out of the window exactly like a plan the model writes itself under -S.
//   -H            after generation print "hid <v1> ... <vD>" to stderr: the mean of the final normed hidden state
//                 (the head's input) over the story body tokens. The quality head (degerlendirme/odul.py) scores
//                 a candidate from it; on the ESP32 this is D additions per token and one D-dot at the end.
//   -G k          with -H: prompt tokens from position k on count as story body too (teacher forcing: give
//                 header + an existing story as the prompt and n = 0 to get that story's hidden-state mean).
// rep_penalty > 1 lowers the odds of any token used in the last ORNEKLE_PENCERE (64) tokens (1 = off);
// cheap enough for the ESP32: one pass over a 64-entry ring buffer per token.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include "../llm.h"
#include "../ornekle.h"

static uint8_t *read_file(const char *p, size_t *n) {
  FILE *f = fopen(p, "rb"); if (!f) { perror(p); exit(1); }
  fseek(f, 0, SEEK_END); *n = ftell(f); fseek(f, 0, SEEK_SET);
  uint8_t *b = malloc(*n); if (fread(b, 1, *n, f) != *n) exit(1); fclose(f); return b;
}

// Appends the comma-separated ids of s to out[n..max); returns the new count.
static int read_ids(char *s, int *out, int n, int max) {
  for (char *t = strtok(s, ","); t && n < max; t = strtok(NULL, ",")) out[n++] = atoi(t);
  return n;
}

int main(int argc, char **argv) {
  if (argc < 8) {
    fprintf(stderr, "usage: gen model.bin n temp topk seed rep [-b ids] [-N ids] [-P] [-l] [-e id] [-S nl] "
                    "[-W k] prompt_ids...\n");
    return 2;
  }
  size_t nb; uint8_t *buf = read_file(argv[1], &nb);
  Model m; if (llm_load(buf, &m)) { fprintf(stderr, "bad magic\n"); return 1; }
  int N = atoi(argv[2]); float temp = atof(argv[3]); int K = atoi(argv[4]);
  if (K < 1) K = 1;
  srand(atoi(argv[5]));
  float rep = atof(argv[6]);
  int ban[512], n_ban = 0, body_ban[512], n_body_ban = 0, first_id = 7, with_logp = 0, with_hid = 0, hid_from = -1, prompt_in_window = 1,
      stop_id = -1, plan_nl = -1, prompt_window = 1 << 30;
  for (;;) {  // options, see the usage comment at the top
    if (argc > first_id + 1 && strcmp(argv[first_id], "-b") == 0) {
      n_ban = read_ids(argv[first_id + 1], ban, n_ban, 512); first_id += 2;
    } else if (argc > first_id + 1 && strcmp(argv[first_id], "-N") == 0) {
      n_body_ban = read_ids(argv[first_id + 1], body_ban, n_body_ban, 512); first_id += 2;
    } else if (argc > first_id + 1 && strcmp(argv[first_id], "-e") == 0) {
      stop_id = atoi(argv[first_id + 1]); first_id += 2;
    } else if (argc > first_id + 1 && strcmp(argv[first_id], "-S") == 0) {
      plan_nl = atoi(argv[first_id + 1]); first_id += 2;
    } else if (argc > first_id + 1 && strcmp(argv[first_id], "-W") == 0) {
      prompt_window = atoi(argv[first_id + 1]); first_id += 2;
    } else if (argc > first_id && strcmp(argv[first_id], "-P") == 0) {
      prompt_in_window = 0; first_id += 1;
    } else if (argc > first_id && strcmp(argv[first_id], "-l") == 0) {
      with_logp = 1; first_id += 1;
    } else if (argc > first_id + 1 && strcmp(argv[first_id], "-G") == 0) {
      hid_from = atoi(argv[first_id + 1]); first_id += 2;
    } else if (argc > first_id && strcmp(argv[first_id], "-H") == 0) {
      with_hid = 1; first_id += 1;
    } else break;
  }
  int D = m.c.dim, L = m.c.n_layers, P = m.c.ple_dim, F = m.c.ffn, V = m.out_vocab, S = m.c.seq_len;
  if (K > V) K = V;  // same top-k set, bounded scratch
  Scratch s;
  s.x = malloc(D * 4); s.h = malloc((F > D ? F : D) * 4);
  s.qkv = malloc(3 * D * 4); s.att = malloc(D * 4);
  s.g1 = malloc(F * 4); s.g2 = malloc((P > F ? P : F) * 4);
  s.ple = malloc(L * P * 4); s.tmpP = malloc(L * P * 4); s.trow = malloc(L * P * 4);
  s.logits = malloc(V * 4); s.scores = malloc(S * 4);
  s.kcache = malloc((size_t)L * S * D * 4); s.vcache = malloc((size_t)L * S * D * 4);
  OrnAyar cfg = {temp, K, rep, ban, n_ban, body_ban, n_body_ban, malloc(K * sizeof(int)), malloc(K * sizeof(double))};
  OrnDurum st; orn_sifirla(&st);
  // The KV cache holds S positions and the embedding V rows: refuse a prompt that would write past either.
  if (argc - first_id < 1 || argc - first_id >= S) {
    fprintf(stderr, "prompt must be 1..%d tokens, got %d\n", S - 1, argc - first_id); return 2;
  }
  int pos = 0, tok = 0;
  double *hid = calloc(D, sizeof(double)); int n_hid = 0;
  for (int i = first_id; i < argc; i++) {
    tok = atoi(argv[i]);
    if (tok < 0 || tok >= m.c.vocab) { fprintf(stderr, "token id %d out of range\n", tok); return 2; }
    if (prompt_in_window && i - first_id < prompt_window) orn_ekle(&st, tok);
    llm_forward(&m, tok, pos++, &s);
    if (with_hid && hid_from >= 0 && i - first_id >= hid_from) { for (int j = 0; j < D; j++) hid[j] += s.x[j]; n_hid++; }
  }
  if (plan_nl >= 0) orn_plan_baslat(&st, plan_nl);  // -S: the body starts after the plan's "nl nl"
  else st.govde = 1;  // the prompt ends with the header, so the story body starts at the first sampled token
  clock_t t0 = clock(); int made = 0;
  for (int step = 0; step < N && pos < S; step++) {
    int govdede = st.govde;  // body already started: the token sampled now is a body token
    tok = orn_adim(&cfg, &st, s.logits, V);
    // model confidence in its own choice: used to rank pre-generated candidates
    if (with_logp) printf("%d %.4f\n", tok, orn_logp(s.logits, V, tok));
    else printf("%d\n", tok);
    fflush(stdout);
    made++;
    if (tok == stop_id) break;  // -e
    if (st.plan_bozuk) break;   // -S: no body within ORNEKLE_PLAN_SINIR tokens
    llm_forward(&m, tok, pos++, &s);
    if (with_hid && govdede) { for (int i = 0; i < D; i++) hid[i] += s.x[i]; n_hid++; }
  }
  if (with_hid) {
    fprintf(stderr, "hid");
    for (int i = 0; i < D; i++) fprintf(stderr, " %.5f", n_hid ? hid[i] / n_hid : 0.0);
    fprintf(stderr, "\n");
  }
  if (plan_nl >= 0 && !st.govde) fprintf(stderr, "plan_bozuk\n");
  fprintf(stderr, "%d tokens, %.1f tok/s\n", made, made / ((double)(clock() - t0) / CLOCKS_PER_SEC));
  return 0;
}
