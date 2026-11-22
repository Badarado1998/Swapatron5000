#!/usr/bin/env python3
"""Build CONTRIBUTORS.md (the wall and the leaderboard) from contributions.csv.

Run from the repository root:  python3 scripts/build_wall.py
Uses only the Python standard library.

contributions.csv columns: date, username, type, description, points
The points column is optional. A blank or missing value counts as 1.
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
ALLOWED_POINTS = {1, 2, 3, 5}
LEVELS = [(30, "Architect"), (15, "Builder"), (5, "Tinkerer"), (1, "Spark")]
# badge name, contribution type, how many contributions of that type
BADGES = [
    ("Giver", "part", 3),
    ("Maker", "build", 2),
    ("Coder", "code", 2),
    ("Scribe", "docs", 2),
    ("Keeper", "upkeep", 4),
    ("Thinker", "idea", 3),
]
ALL_ROUNDER_TYPES = 4
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
            raw = (row.get("points") or "").strip()
            try:
                points = int(raw) if raw else 1
            except ValueError:
                points = -1
            if points not in ALLOWED_POINTS:
                raise SystemExit(
                    f"contributions.csv line {line_no}: points must be 1, 2, 3, "
                    f"or 5 (or blank for 1). Found '{raw}'."
                )
            if kind == "part" and points != 1:
                raise SystemExit(
                    f"contributions.csv line {line_no}: giving a part is always "
                    f"1 point, whatever it cost."
                )
            rows.append((user, kind, points))
    return rows


def level_for(points):
    for threshold, name in LEVELS:
        if points >= threshold:
            return name
    return ""


def badges_for(kind_counts):
    earned = [name for name, kind, need in BADGES if kind_counts[kind] >= need]
    if sum(1 for kind in TYPES if kind_counts[kind]) >= ALL_ROUNDER_TYPES:
        earned.append("All-rounder")
    return earned


def render(rows):
    points = Counter()
    counts = Counter()
    kinds = defaultdict(Counter)
    for user, kind, pts in rows:
        points[user] += pts
        counts[user] += 1
        kinds[user][kind] += 1

    out = [
        "# Contributors Wall",
        "",
        "Everyone who has helped the IoT Swapatron 5000. Thank you.",
        "",
        "This page is built automatically from `contributions.csv`. "
        "Do not edit it by hand. See [BOUNTIES.md](BOUNTIES.md) for how "
        "points, levels, and badges work.",
        "",
    ]

    if not points:
        out += ["Nobody is on the wall yet. Be the first!", ""]
        return "\n".join(out)

    ranked = sorted(points.items(), key=lambda item: (-item[1], item[0].lower()))

    out += [
        "## Leaderboard",
        "",
        "Points are for fun and for thanks. Giving a part is always 1 point, "
        "whatever it cost.",
        "",
        "| Rank | Contributor | Points | Level | Contributions |",
        "|---|---|---|---|---|",
    ]
    rank = 0
    previous = None
    for position, (user, pts) in enumerate(ranked[:TOP_N], start=1):
        if pts != previous:
            rank = position
            previous = pts
        out.append(
            f"| {rank} | [@{user}](https://github.com/{user}) | {pts} | "
            f"{level_for(pts)} | {counts[user]} |"
        )

    out += ["", "## The wall", ""]
    for user in sorted(points, key=str.lower):
        helped = ", ".join(TYPES[kind] for kind in TYPES if kinds[user][kind])
        line = (
            f"- [@{user}](https://github.com/{user}) "
            f"({level_for(points[user])}): {helped}"
        )
        earned = badges_for(kinds[user])
        if earned:
            line += ". Badges: " + ", ".join(earned)
        out.append(line)
    out.append("")
    return "\n".join(out)


def main():
    OUTPUT.write_text(render(load()), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
