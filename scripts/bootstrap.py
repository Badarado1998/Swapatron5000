#!/usr/bin/env python3
"""One-time setup: create the labels and starter issues, then link the decision table.

Run it from the Actions tab ("Set up labels and issues"). It is safe to run twice:
labels are updated in place, and an issue is skipped if one with the same title exists.

It reads the tables in the docs, so the docs stay the source of truth:
  docs/starter-issues.md  ->  starter and standing issues
  DECISIONS.md            ->  one decision issue per open question
  CHALLENGES.md           ->  one challenge issue per row
  BOUNTIES.md             ->  one bounty issue per row

Needs the GitHub CLI (`gh`) and a token in GH_TOKEN. Use --dry-run to only print.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "Fishers-Founders-United/Swapatron5000"
BLOB = f"https://github.com/{REPO}/blob/main"
DRY = "--dry-run" in sys.argv

LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
NOTHING_DECIDED = "> **Nothing is decided yet.** This is a proposal. Comment below and help shape it."

LABELS = {
    "ask": ("1D76DB", "Someone is asking for a part"),
    "bounty": ("FBCA04", "A job with points attached"),
    "decision": ("5319E7", "An open question that will be decided in the open"),
    "challenge": ("D93F0B", "A known problem Swapatron needs help with"),
    "event": ("0E8A16", "An in-person event. Thumbs up if you are coming"),
    "rfc": ("C5DEF5", "A longer proposal that needs comments"),
    "hardware": ("BFD4F2", "The box, the shell, the bins"),
    "electronics": ("FEF2C0", "Power, sensors, radios"),
    "software": ("D4C5F9", "Inventory, alerts, forms"),
    "docs": ("C2E0C6", "Writing, signs, drawings, the tutorial"),
    "network": ("0E8A16", "Boxes in other towns and how they connect"),
    "supplies": ("F9D0C4", "Bags, labels, desiccant, lumber"),
    "needs owner": ("EDEDED", "Nobody has claimed this yet. Comment to take it"),
    "good first issue": ("7057FF", "A friendly place to start"),
    "help wanted": ("008672", "Extra hands welcome"),
}


def gh(*args, check=True):
    return subprocess.run(["gh", *args], capture_output=True, text=True, check=check)


def table_rows(path, heading_hint=None):
    """Yield the cells of each data row in the first table after heading_hint."""
    text = (ROOT / path).read_text(encoding="utf-8")
    if heading_hint:
        idx = text.find(heading_hint)
        text = text[idx:] if idx >= 0 else text
    rows, started = [], False
    for line in text.splitlines():
        if line.startswith("|"):
            started = True
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            rows.append(cells)
        elif started:
            break
    return rows[1:]  # drop the header row


def labels_from(cell):
    return [x.strip("` ") for x in cell.split(",") if x.strip("` ")]


def issue(title, labels, body):
    return {"title": title, "labels": labels, "body": body}


def build_issues():
    items = []

    # Starter issues
    for title, labs in table_rows("docs/starter-issues.md"):
        items.append(issue(
            title, labels_from(labs),
            f"{NOTHING_DECIDED}\n\nThis is one of the starter jobs for Swapatron5000. "
            f"Comment to say you would like to take it, or to share a thought.\n\n"
            f"New to GitHub? [Here is how to comment]({BLOB}/docs/have-your-say.md)."))

    # Standing and extra issues (second table in the same file)
    text = (ROOT / "docs/starter-issues.md").read_text(encoding="utf-8")
    extra = table_rows("docs/starter-issues.md", "Also create:")
    for title, labs in extra:
        if title.startswith("One issue per bounty") or title.startswith("Confirm with the lab"):
            continue
        if any(i["title"] == title for i in items):
            continue
        items.append(issue(title, labels_from(labs),
                           f"{NOTHING_DECIDED}\n\nA standing issue. Add a comment whenever you have something to report."))
    items.append(issue(
        "Confirm with the lab whether parcels can be received",
        ["needs owner"],
        "People can ask for parts to be shipped to the lab, but the lab has not agreed to receive parcels yet. "
        f"Until it does, the notice in [ASKS.md]({BLOB}/ASKS.md) stays. When the lab confirms, "
        "a maintainer removes the notice and records the answer here."))

    # Decisions
    for num, question, status, _where in table_rows("DECISIONS.md", "## Open questions"):
        items.append(issue(
            f"Decision {num}: {question}", ["decision"],
            f"{NOTHING_DECIDED}\n\n**Question {num} in [DECISIONS.md]({BLOB}/DECISIONS.md):** {question}\n\n"
            f"**Status:** {LINK_RE.sub(r'\\1', status)}\n\n"
            "Comments are open until Sunday, January 10, 2027. Maintainers post a proposed answer "
            "between January 11 and 17, and final comments close January 31. Tell us what you think, "
            "even if it is just a thumbs up or a thumbs down on the question."))

    # Challenges
    for doubt, _status, first in table_rows("CHALLENGES.md", "## Challenges we already know about"):
        items.append(issue(
            f"Challenge: {doubt}", ["challenge"],
            f"Swapatron heard this one and is not scared.\n\n**First thoughts:** {first}\n\n"
            "Pile on. What makes this worse than we think? What would fix it? You do not need a solution. "
            f"Spotting the problem earns a point. See [CHALLENGES.md]({BLOB}/CHALLENGES.md)."))

    # Bounties
    for job, points, kind in table_rows("BOUNTIES.md", "| Bounty | Points | Type |"):
        items.append(issue(
            f"Bounty ({points}): {LINK_RE.sub(r'\\1', job)}", ["bounty"],
            f"**Worth {points} point{'s' if points != '1' else ''}.** Type: {kind}.\n\n"
            "To take it, comment \"I'll take this\". Nobody has to ask permission, and more than one person "
            "can work on the same bounty. When you are done, link your work here. A maintainer adds you to "
            f"the Contributors Wall.\n\nHow points work: [BOUNTIES.md]({BLOB}/BOUNTIES.md)."))
    return items


def ensure_labels():
    for name, (color, desc) in LABELS.items():
        print(f"label: {name}")
        if not DRY:
            gh("label", "create", name, "--color", color, "--description", desc, "--force")


def existing_issues():
    out = gh("issue", "list", "--repo", REPO, "--state", "all", "--limit", "1000",
             "--json", "title,number").stdout
    return {i["title"]: i["number"] for i in json.loads(out)}


def link_decisions(numbers):
    """Replace 'Issues tab' in DECISIONS.md with a link to each decision issue."""
    path = ROOT / "DECISIONS.md"
    lines, changed = path.read_text(encoding="utf-8").splitlines(), False
    for n, line in enumerate(lines):
        m = re.match(r"\|\s*(\d+)\s*\|", line)
        if m and line.rstrip().endswith("| Issues tab |"):
            title = next((t for t in numbers if t.startswith(f"Decision {m.group(1)}:")), None)
            if title:
                link = f"[Comment](https://github.com/{REPO}/issues/{numbers[title]})"
                lines[n] = line.rstrip()[: -len("Issues tab |")] + link + " |"
                changed = True
    if changed and not DRY:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed


def main():
    ensure_labels()
    have = {} if DRY else existing_issues()
    created = skipped = 0
    for it in build_issues():
        if it["title"] in have:
            skipped += 1
            continue
        print(f"issue: {it['title']}  {it['labels']}")
        if not DRY:
            args = ["issue", "create", "--repo", REPO, "--title", it["title"], "--body", it["body"]]
            for lab in it["labels"]:
                args += ["--label", lab]
            gh(*args)
            time.sleep(2)  # be gentle with GitHub's rate limits
        created += 1
    print(f"created {created}, skipped {skipped}")
    if not DRY:
        print("linked decisions:", link_decisions(existing_issues()))


if __name__ == "__main__":
    main()
