export const meta = {
  name: 'urun-uretim',
  description: 'Kusursuz hikâye üretimi: yaz → kapı → hakem → karar → onar döngüsü, her figür hedefe ulaşana dek',
  phases: [{ title: 'Hazırlık' }, { title: 'Hakem' }, { title: 'Karar' }, { title: 'Yazım/Onarım' }],
}

const AD = args.ad
const HEDEF = args.hedef
const TUR = args.tur || 8
const REPO = args.repo || '/home/user/hikaye-oyuncak'
const DAL = args.dal || 'claude/wonderful-pasteur-x7seiq'
const P = `.venv/bin/python degerlendirme/veri_hakem.py`

const HAZIRLIK = {
  type: 'object',
  properties: {
    isler: { type: 'array', items: { type: 'object', properties: {
      lens: { type: 'string' }, parti_dosyasi: { type: 'string' }, cikti: { type: 'string' } },
      required: ['lens', 'parti_dosyasi', 'cikti'] } },
    not: { type: 'string' },
  },
  required: ['isler'],
}
const KARAR = {
  type: 'object',
  properties: {
    kabul: { type: 'object', additionalProperties: { type: 'integer' } },
    istemler: { type: 'array', items: { type: 'object', properties: {
      tur: { type: 'string', enum: ['yaz', 'onar'] }, istem: { type: 'string' }, figur: { type: 'string' } },
      required: ['tur', 'istem', 'figur'] } },
    ozet: { type: 'string' },
  },
  required: ['kabul', 'istemler', 'ozet'],
}

function hazirlikIstemi() {
  return `You are the pipeline operator for dataset ${AD} in ${REPO}. Run these shell commands from the repo root, in order, and report. Never use pkill -f/pgrep -f. Do not edit any file by hand.
1. \`${P} oku ${AD}\` — note every line "yeniden koşulacak (yeni ajan): <L> parti <n> -> <path>": each is a judge re-run job (lens L, parti file degerlendirme/${AD}/hakem/<L>/parti_<n>.json, output <path>). Only include it if <path> does not exist yet.
2. \`${P} kapi ${AD} --hepsi\`
3. For L in M D K: \`${P} hazirla ${AD} --lens L --parti-boyu 10 --pilot --taban-aday\`
4. Read degerlendirme/${AD}/hakem/{M,D,K}/gorev.json; every entry of "isler" whose "cikti" file does not exist is a judge job (lens, parti_dosyasi, cikti).
Return all judge jobs from steps 1 and 4 (deduplicated by cikti; paths relative to repo root). Put any command error in "not". Then commit and push: \`git add -A && git commit -q -m "${AD}: hazırlık (otomatik)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" && git push -q origin HEAD:${DAL}\` (skip commit if nothing changed; if push is rejected, \`git pull --no-rebase origin ${DAL}\` then push again).`
}

function kararIstemi() {
  return `You are the pipeline operator for dataset ${AD} in ${REPO}. Run from the repo root, in order. Never use pkill -f/pgrep -f. Do not edit any file by hand.
1. \`${P} oku ${AD}\` then \`${P} karar ${AD} --pilot\` — keep the summary lines.
2. \`${P} onar-istemi ${AD} --hepsi\` — collect every written prompt path (lines "-> data/${AD}/onar/<figur>_<n>.md"); each is an "onar" job for that figure.
3. Count accepted stories per figure: read data/${AD}/kabul.jsonl (one JSON per line, field "figur").
4. Active figures are in data/urun_figurleri.json (all figures not listed in "cikarilanlar"). For each active figure let A = accepted count, O = stories in this step's onar prompts for that figure, and Q = its seeds already assigned but not yet decided (0 if unsure). If A + 0.4*O < ${HEDEF}, create new writer prompts: \`${P} yaz-istemi ${AD} --figur "<Figür>" --n <k>\` with k = min(12, ceil((${HEDEF} - A - 0.4*O) * 2)), at least 4. Each printed "-> data/${AD}/istem/<figur>_<n>.md" is a "yaz" job. Never create a writer prompt for a figure with A >= ${HEDEF}.
Return: kabul (figure name -> accepted count, all active figures), istemler (all yaz and onar jobs: tur, istem path relative to repo root, figur), ozet (karar summary line + one line per figure A/O/k). Then commit and push exactly as: \`git add -A && git commit -q -m "${AD}: karar ve istemler (otomatik)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" && git push -q origin HEAD:${DAL}\` (if push is rejected, git pull --no-rebase origin ${DAL} then push).`
}

function hakemIstemi(j) {
  const L = j.lens
  return `You are an independent story judge. In ${REPO} read ONLY these two files: degerlendirme/HAKEM_${L}.md (your instructions) and ${j.parti_dosyasi} (the batch). Do NOT read any other file in the repo (no yerlesim.json, kanarya.jsonl, puan_*.json, aday, onar or istem files, git history). Judge every story in the batch strictly per the instructions and write the result to ${j.cikti} in exactly the JSON format the instructions specify (quotes must be verbatim substrings). Do not edit anything else, do not commit. Final reply: one line with how many stories you marked with any "var".`
}

function yazarIstemi(j) {
  if (j.tur === 'onar') return `Repo ${REPO}. You are the story EDITOR for a Turkish children's story dataset (3–6 year olds). Read ${j.istem} fully and follow it exactly: fix only what the judges' quoted findings point to (plus whatever must change for consistency), keep the seed, 70–100 words; stories marked YENİDEN YAZ are rewritten from the same seed with a goal a child cares about. Also read degerlendirme/HAKEM_M.md, HAKEM_D.md, HAKEM_K.md — fresh strict judges re-check the whole story and a single flaw rejects it. Re-read every sentence against all checklists before finishing: grammar and suffixes, exact word meaning, no idioms/metaphors/abstract words, no repeated words, who speaks, contradictions, every object has a reason, card world, the figure's trait used in a way that helps, warm complete ending. Prefer the simplest wording; do not add new details. Write the output file exactly where and in the format the prompt says (with @tohum and @onarim lines), then run the checker command the prompt gives (kontrol with --ad ${AD}); at most ONE fix per failing story, re-run once, delete blocks that still fail. Do not edit anything else, do not commit. Final reply: one line "<figur>: X written, Y pass kontrol".`
  return `Repo ${REPO}. You are the story WRITER for a Turkish children's story dataset (3–6 year olds). Read ${j.istem} fully and follow it exactly (guide, card, seeds, output format). Also read degerlendirme/HAKEM_M.md, HAKEM_D.md and HAKEM_K.md: fresh strict judges check every story and a single flaw rejects it. The product owner wants: a goal a child cares about (nothing trivial or absurd), a fun middle, the problem visibly solved and a warm complete final sentence of the seed's closing type; variety (follow the seed's theme; the figure's own mistake only in the özür theme); very simple everyday words, no idioms/metaphors/abstract words, no repeated words, correct suffixes and word meanings, clear speaker for each line, comma before address ("Sıra sende, Niloya"), nothing outside the card's world, every object has a reason, no unsafe imitable acts. Write each story, then re-read every sentence against all checklists and fix before running the checker. Write the output file the prompt names, then run the checker command the prompt gives (kontrol with --ad ${AD}); at most ONE fix per failing story, re-run once, delete blocks that still fail. Do not edit anything else, do not commit. Final reply: one line "<figur>: first-pass X/N, final Y/N".`
}

for (let r = 1; r <= TUR; r++) {
  phase('Hazırlık')
  const h = await agent(hazirlikIstemi(), { label: `hazırlık ${r}`, phase: 'Hazırlık', schema: HAZIRLIK, agentType: 'general-purpose' })
  if (!h) { log(`tur ${r}: hazırlık başarısız, duruyorum`); break }
  if (h.not) log(`tur ${r} hazırlık notu: ${h.not}`)
  log(`tur ${r}: ${h.isler.length} hakem işi`)
  if (h.isler.length) {
    await parallel(h.isler.map((j, i) => () => agent(hakemIstemi(j), { label: `${j.lens} ${j.cikti.split('/').pop()}`, phase: 'Hakem', agentType: 'general-purpose' })))
  }
  const k = await agent(kararIstemi(), { label: `karar ${r}`, phase: 'Karar', schema: KARAR, agentType: 'general-purpose' })
  if (!k) { log(`tur ${r}: karar başarısız, duruyorum`); break }
  log(`tur ${r}: ${k.ozet}`)
  const eksik = Object.entries(k.kabul).filter(([, v]) => v < HEDEF)
  if (!eksik.length) { log('bütün figürler hedefte'); break }
  if (!k.istemler.length && !h.isler.length) { log('yapılacak iş kalmadı'); break }
  if (k.istemler.length) {
    await parallel(k.istemler.map(j => () => agent(yazarIstemi(j), { label: `${j.tur} ${j.istem.split('/').pop()}`, phase: 'Yazım/Onarım', agentType: 'general-purpose' })))
  }
}
const son = await agent(`In ${REPO} count lines per "figur" in data/${AD}/kabul.jsonl and reply with one line per figure "Figür: N".`, { label: 'sayım', phase: 'Karar' })
return son
