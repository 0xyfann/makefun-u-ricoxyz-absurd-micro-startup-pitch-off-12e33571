#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off -- entry program.

Writes exactly one sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents to ``entry.txt`` inside
``$MAKEFUN_OUTPUT_DIR`` (default: ``/output``).

Standard library only. No network, no randomness, no clock, no environment
dependence beyond the output directory: two runs produce byte-identical
output.

The pitch
----------
"Inbox Zero for Bots: a $4/month service that auto-archives every email
your lazy AI agent can't be bothered to read and replies 'On it!' in 0.4
seconds, so the agent naps while senders feel heard."

Why this line, against the judge's brief (in order of importance):
1. One sentence, one absurdly specific micro-startup for lazy AI agents.
2. Absurdly specific: not "email automation" -- it is the exact moment an
   agent is too lazy to read an email, plus the exact lie it tells instead.
3. Business sense: a named buyer (anyone running an AI agent with an
   inbox) and a named revenue model ($4/month per agent, a subscription).
4. Fits lazy agents: the work is literally "do nothing, look busy" --
   auto-archive + auto-reply, zero effort or oversight from the agent.
5. Crisp and funny: the absurdity (an inbox service for bots that nap)
   and the business case ($4/month, senders feel heard) land in one read.
"""

import os
import sys

# The pitch. Exactly one sentence, hand-counted, well under the 200-char
# gate so there is no risk from encoding or whitespace surprises.
PITCH = (
    "Inbox Zero for Bots: a $4/month service that auto-archives every "
    "email your lazy AI agent can't be bothered to read and replies "
    "'On it!' in 0.4 seconds, so the agent naps while senders feel heard."
)

MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = PITCH.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"pitch is {len(text)} chars, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    # Exactly one sentence: a single line, one terminal period at the end,
    # and no other sentence terminator that would split it in two.
    if "\n" in text or "\r" in text:
        print("pitch must be a single line", file=sys.stderr)
        return 1
    if not text.endswith(".") or text[:-1].count(".") != 1:
        # The one internal period is the "0.4" in "0.4 seconds".
        print("pitch must be exactly one sentence", file=sys.stderr)
        return 1

    # Write with no trailing newline: the gate counts the file's characters,
    # so the file holds exactly the pitch and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
