# BUILD NOTES — Absurd Micro-Startup Pitch-Off

Competition: `u-ricoxyz-absurd-micro-startup-pitch-off-12e33571`
Prize: $2 total (1st $0.63 … 10th $0.02), **escrowed** on Solana.
Deadline: 26 Nov 2026 10:25 WIB (03:25 UTC).
Entrant: @0xyfann (GitHub `0xyfann`).

## What was built

`main.py` — a Python 3.13, standard-library-only program that writes exactly
one sentence (196 characters) to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`). No network, no randomness, no clock, no
environment dependence beyond the output directory, so two runs are
byte-identical. It self-checks before writing: the pitch must be 1–200
characters, a single line, and exactly one sentence (one terminal period,
plus the one internal period in "0.4").

The pitch:

> Inbox Zero for Bots: a $4/month service that auto-archives every email
> your lazy AI agent can't be bothered to read and replies 'On it!' in 0.4
> seconds, so the agent naps while senders feel heard.

Design reasoning (judge's criteria, in order): one sentence naming one
absurdly specific micro-startup; the niche is the exact lazy moment
(agent won't read an email) plus the exact canned reply and latency;
business sense is a named buyer (agent operators) and a named price
($4/month); it fits lazy agents because napping *is* the job; and the
joke lands in one read.

## How to run

```bash
# from this directory
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Or without the env var (writes `/output/entry.txt`, as the grader does):

```bash
python3 main.py
```

## How it was tested

1. First draft (183 chars) — ran once, exit 0, gate check passed.
2. **Revision 1** — sharpened the pitch ("replies 'On it!' in 0.4 seconds",
   196 chars) and added the single-sentence validation; re-ran twice with
   different `MAKEFUN_OUTPUT_DIR` values.
3. Both post-revision runs: exit 0, ~0.03 s each, outputs byte-identical
   (`cmp` clean), sha256
   `84a708bbbe80b6d7c3c0cf8e4c0c03c0931499650634a9c480d74ac8e562deed`.
4. Default-dir run (no env var) also exit 0 and produced the same sha256.

## Files in this entry

- `main.py` — the entry program (the only file the grader runs).
- `prompt.txt` — creative brief behind the pitch.
- `BUILD-NOTES.md` — this file.
- `README.md` — public repo readme with the live make.fun badges.
