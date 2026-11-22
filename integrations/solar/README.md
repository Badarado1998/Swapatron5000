# Solar and power

> **Draft. Nothing here is decided.** This is a starting brief. Every idea is a proposal, and every number is a guess until measured. See the [integrations overview](../README.md) and the [proposed baseline](../../DECISIONS.md).

## Goal

If the box has electronics, keep them running safely in every Indiana season. If it does not work with no power, we have designed it wrong.

## Read this first: what the safety baseline does and does not say

The proposed baseline says no loose lithium cells in the box, no battery charging in the box, and no collection of used batteries. Those rules are about **parts that visitors leave**.

Whether the box may hold **its own** sealed battery, and charge it from a solar panel, is a separate question. It is not decided, and it needs its own `rfc` and review by a qualified person before anything is built. See the battery chemistry issue.

## Open questions

1. How much power does the whole thing need per day? Start with a power budget, with every assumption labelled
2. Does the box need a battery at all? Could a small super-capacitor, or mains from the lab (no, the baseline says no mains), or no power at all be enough?
3. If a battery: which chemistry, which temperature rating, and which sealed pack from a known maker? Cells are commonly warned against charging below freezing, so the Indiana winter matters. Verify the limits for the exact part
4. Where does it live in the box so that it can not be reached by hands or water?
5. What happens in a long cloudy week?
6. What turns it off safely?

## Wanted

- A power budget spreadsheet, with every number marked as measured or guessed
- A comparison of "no battery", "a small sealed pack", and "no power at all"
- A list of what could go wrong with a battery in a cold, wet box
- A list of qualified people we could ask to review it

## How to start

1. Read the [integrations overview](../README.md) and the rules every track follows.
2. [Start a brief](../../../../issues/new?template=start-a-brief.yml), or copy the [template](../_template/README.md).
3. Post it. Others will comment. A short, honest brief is better than a polished one.
4. Say if an AI helped. See [ai-contribute.md](../../docs/ai-contribute.md).
5. Anything involving a battery, a lock, a camera, or structure needs review by a qualified person before it is built.
