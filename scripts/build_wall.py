#!/usr/bin/env python3
"""Build CONTRIBUTORS.md (the wall and the leaderboard) from contributions.csv.

Run from the repository root:  python3 scripts/build_wall.py
Uses only the Python standard library.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "contributions.csv"
OUTPUT = ROOT / "CONTRIBUTORS.md"

TYPES = {
    "part": "Parts and supplies",
    "build": "Building",
    "code": "Code and electronics",
    "docs": "Docs and signs",
    "upkeep": "Box upkeep",
    "idea": "Ideas",
}
TOP_N = 10


def load():
    rows = []
    with SOURCE.open(newline="", encoding="utf-8") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            user = (row.get("username") or "").strip().lstrip("@")
            kind = (row.get("type") or "").strip().lower()
            if not user:
                continue
            if kind not in TYPES:
                raise SystemExit(
                    f"contributions.csv line {line_no}: unknown type '{kind}'. "
                    f"Use one of: {', '.join(TYPES)}"
                )
            rows.append((user, kind))
    return rows


def render(rows):
    totals = Counter(user for user, _ in rows)
    kinds = defaultdict(Counter)
    for user, kind in rows:
        kinds[user][kind] += 1

    out = [
        "# Contributors Wall",
        "",
        "Everyone who has helped the IoT Swapatron 5000. Thank you.",
        "",
        "This page is built automatically from `contributions.csv`. "
        "Do not edit it by hand.",
        "",
    ]

    if not totals:
        out += ["Nobody is on the wall yet. Be the first!", ""]
        return "\n".join(out)

    ranked = sorted(totals.items(), key=lambda item: (-item[1], item[0].lower()))

    out += [
        "## Leaderboard",
        "",
        "One point per contribution of any kind. A bag of resistors counts "
        "the same as a solar panel.",
        "",
        "| Rank | Contributor | Contributions |",
        "|---|---|---|",
    ]
    rank = 0
    previous = None
    for position, (user, count) in enumerate(ranked[:TOP_N], start=1):
        if count != previous:
            rank = position
            previous = count
        out.append(f"| {rank} | [@{user}](https://github.com/{user}) | {count} |")

    out += ["", "## The wall", ""]
    for user in sorted(totals, key=str.lower):
        helped = ", ".join(
            TYPES[kind] for kind in TYPES if kinds[user][kind]
        )
        out.append(f"- [@{user}](https://github.com/{user}): {helped}")
    out.append("")
    return "\n".join(out)


def main():
    OUTPUT.write_text(render(load()), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
