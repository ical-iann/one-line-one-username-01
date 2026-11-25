"""One Word, One Username, One Reward (u-rusdyxbt-one-word-one-username-one-reward-1a191fae).

Program/v1 entry: writes the entrant's own make.fun username, and nothing
else, to /output/entry.txt (via MAKEFUN_OUTPUT_DIR). No network,
deterministic.
"""

import os

# The entry must be the entrant's own make.fun handle, @witty-walrus-59,
# sent as one word: no spaces, no padding, no gloss tacked on.
LINE = "witty-walrus-59"


def main() -> None:
    # Enforce the competition gate locally: 1-30 chars, one word, non-blank.
    assert 1 <= len(LINE) <= 30, f"line is {len(LINE)} chars, gate is 1-30"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert len(LINE.split()) == 1, "line must be exactly one word"
    assert not any(c.isspace() for c in LINE), "username must contain no whitespace at all"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
