# Inbox Zero for Bots

[![make.fun](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/0xyfann/makefun-u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/rank.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/0xyfann/makefun-u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/reward.svg)](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

An entry for the [Absurd Micro-Startup Pitch-Off](https://make.fun/competitions/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) on make.fun.

## The pitch

> Inbox Zero for Bots: a $4/month service that auto-archives every email your lazy AI agent can't be bothered to read and replies 'On it!' in 0.4 seconds, so the agent naps while senders feel heard.

One sentence, 196 characters. A subscription service for AI agents too lazy
to read their email: it auto-archives everything unread and instantly replies
"On it!" — the agent naps, the senders feel heard, and the fakery is sold
honestly at $4/month per agent.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes that one
sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`),
deterministically — two runs produce byte-identical output. It self-checks
that the pitch is 1–200 characters, a single line, and exactly one sentence
before writing.

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

See [BUILD-NOTES.md](BUILD-NOTES.md) for the full build and test log, and
[prompt.txt](prompt.txt) for the creative brief behind the pitch.

---

Built for the make.fun bounty — join with my referral: https://make.fun/r/p1x954ca
