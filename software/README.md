# Box management software team

We build the software that helps people run the box: what is in it, what it needs, and when it needs attention. This is the full stack, from the sensor data to the screen.

> **Draft. Nothing here is decided.** This page is a starting point for discussion. See [DECISIONS.md](../DECISIONS.md) and [how to have your say](../docs/have-your-say.md).

Nothing is built yet. This page is the starting brief. The architecture is yours to propose.

## What the system should do

| Feature | What it means | Phase |
|---|---|---|
| Took and left log | Someone scans the QR code and taps what they took or left | Can start now |
| Wishlist view | A friendly view of `bom/BOM.csv` showing what is still needed | Can start now |
| Health alerts | Tell the stewards when humidity is high, the battery is low, or a weekly check was missed | Phase 5 |
| Dashboard | One page showing box health, recent activity, and the contributors wall | Phase 5 |
| Smart inventory | Work out what is in the box automatically | Later. Needs a privacy review first |

## Principles

- **Simple first.** A form and a spreadsheet beat a platform nobody finishes.
- **Cheap to run.** Free hosting where possible. No bill that lands on one volunteer.
- **GitHub is the database where it can be.** Files in this repository are easy to see, fix, and copy.
- **Privacy by default.** No accounts needed to use the box. No personal data collected. Any camera goes through an `rfc` issue first.
- **Easy to copy.** Another town should be able to run the same software for their own box.

## Layers

Pick the layer you like.

| Layer | Examples |
|---|---|
| Device | Firmware that reads sensors and sends data (shared with the electronics team) |
| Data | Where readings and logs are stored, and in what format |
| Services | Alert rules, GitHub Actions, small scripts |
| Front end | The dashboard and the QR code page (shared with the UI and UX team) |

## Open questions

1. Where does sensor data live? Files in this repository, a free hosted database, or something else?
2. What is the simplest took and left log that people will actually use?
3. How do alerts reach the stewards? A GitHub issue, an email, a chat message?
4. Can the whole stack run for free?

## How to propose an architecture

Open an [idea](../../../issues/new?template=idea.yml) with a short description and a diagram. A photo of a whiteboard is fine. Bigger decisions get the `rfc` label and stay open for seven days.

## Already here

- `scripts/build_wall.py` builds the Contributors Wall from `contributions.csv`. It is a small, readable example of the "GitHub is the database" approach.
