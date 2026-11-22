# Guide for AI assistants

This file is for any AI assistant or agent that a person points at this project. Read it first. It tells you what the project is, what state it is in, and where you can help most.

People: you can paste this to your assistant: "Read AGENTS.md in github.com/Fishers-Founders-United/Swapatron5000 and help me contribute."

## The project in five lines

- **What:** the IoT Swapatron 5000, a proposed free outdoor swap box for IoT and electronics parts. Take a part, leave a part.
- **Where:** proposed for the Indiana IoT Lab, 9059 Technology Lane, Fishers, Indiana. Site approval is pending.
- **Who:** a community project under the Fishers Founders United GitHub organization. Many contributors are new to GitHub. Some are kids.
- **Mission (draft):** make IoT parts free to share, and help the community learn to build things together in the open.
- **Status:** planning. **Nothing is decided and nothing is built.**

## The most important rule

**Never present a proposal as a decision.** Every design, rule, date, and name in this repository is a proposal until it appears in the "Decided" table in [DECISIONS.md](DECISIONS.md). When you summarize the project, say "proposed". If a person asks "what did they decide about X", check that table first.

## Read these, in this order

1. [README.md](README.md): the front door
2. [DECISIONS.md](DECISIONS.md): every open question, and how decisions are made
3. [ROADMAP.md](ROADMAP.md): the proposed timeline
4. [BOUNTIES.md](BOUNTIES.md): jobs that need doing, with points
5. [CONTRIBUTING.md](CONTRIBUTING.md): how contributions work
6. The team page for the work at hand: [hardware/](hardware/README.md), [electronics/](electronics/README.md), [software/](software/README.md), or [ux/](ux/README.md)

## Proposed timeline

| Phase | Proposed dates |
|---|---|
| Listen | To Sun Jan 10, 2027 |
| Decide | Jan 11 to Jan 31, 2027 |
| Gather materials | Feb 1 to Mar 14, 2027 |
| Build day | Sat Mar 20, 2027 |
| Install, then open | Sat Apr 10 and Sat Apr 24, 2027 |

Check [ROADMAP.md](ROADMAP.md) for the current version. Dates may have moved since this file was written.

## Where you can help most

| If the person wants to... | You can... |
|---|---|
| Give an opinion | Help them find the right open question in DECISIONS.md and draft a short, specific comment in their own voice |
| Share a design | Help them describe it, or produce an SVG based on `hardware/designs/example-concept/concept-front.svg` |
| Take a bounty | Help them pick one that fits their skills and plan the work |
| Review something | Check a design against the proposed brief in `hardware/README.md`, or a doc for clarity |
| Write code | Propose small, readable, standard-library-first solutions. See `software/README.md` for the principles |
| Design electronics | Draft a power budget, a schematic outline, or firmware, and flag every assumption |
| Learn GitHub | Walk them through each tap. See `docs/have-your-say.md` and `docs/learn-github.md` |
| Fix the docs | Find confusing or contradictory text and propose plain-language fixes |

High-value gaps right now: design sketches, a suggestion for the standard bin, the sign and label designs, a "took and left" form, and a battery safety summary reviewed by a qualified person.

## How to write for this project

- Plain words and short sentences. Many readers are beginners, and some are children.
- Explain any GitHub term the first time you use it.
- Sentence case for headings.
- No em dashes. Use commas, periods, or parentheses.
- Do not invent facts. No made-up prices, part numbers, dates, measurements, or contributor names. If you do not know, say so and mark it as an open question.
- Label assumptions as assumptions.
- One change per pull request, with a plain description of what changed and why.

## Safety, privacy, and scope limits

These are the project's proposed safety baseline. Do not design around them. If you think one is wrong, say so in an issue.

- No mains power in or on the box
- No loose lithium cells in the outdoor box, and no battery charging there
- No collection of used or damaged batteries
- Any camera, microphone, or lock needs its own `rfc` issue and review before it is designed in
- Collect no personal data by default. Using the box must not require an account unless the community decides otherwise
- Children use this project. Keep everything suitable for them
- The site host can veto anything on its property

For batteries, electrical design, and anything structural, tell the person that a qualified human must review the work before it is built.

## Working in the repository

- `bom/BOM.csv` is the wishlist. It is a draft until a design is chosen. Do not delete rows.
- `contributions.csv` feeds `scripts/build_wall.py`, which writes `CONTRIBUTORS.md`. Never edit `CONTRIBUTORS.md` by hand. Only maintainers add contribution lines.
- `docs/index.html` is the public web page. It is a single self-contained file with no outside dependencies. Keep it that way.
- Relative links such as `../../issues` work on GitHub but break on the published web page. Use full URLs in `docs/index.html`.
- Run `python3 scripts/build_wall.py` after changing the script, and check it still handles an empty `contributions.csv`.

## What not to do

- Do not open issues, pull requests, or comments on a person's behalf without showing them the text first.
- Do not mark anything as decided.
- Do not add dependencies, services, or costs without an `rfc` issue.
- Do not add the names, photos, or contact details of real people.
- Do not rewrite large parts of the repository in one change.

## If you are unsure

Say so. Then help the person open a "Help, I am stuck" issue so a maintainer can answer.
