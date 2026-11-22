# Inventory

> **Draft. Nothing here is decided.** This is a starting brief. Every idea is a proposal, and every number is a guess until measured. See the [integrations overview](../README.md) and the [proposed baseline](../../DECISIONS.md).

## Goal

Know what is in the box, and what it needs, with as little effort as possible. Better to be roughly right and simple than exactly right and abandoned.

## The ladder of effort

| Level | How | Needs |
|---|---|---|
| 0 | Stewards look at the box on the weekly check and update a list | Nothing |
| 1 | A QR code opens a "took and left" form. Visitors tap what they took or left | A form and a spreadsheet |
| 2 | A door switch counts openings, to guess how busy the box is | A sensor |
| 3 | A weight sensor under a bin notices changes | A sensor and a way to calibrate |
| 4 | A camera counts items | See [camera/](../camera/README.md). Needs an `rfc` |

Start at level 0 or 1. Move up only if the simpler level is not enough.

## Open questions

1. What is the minimum a visitor can tell us in two taps?
2. Where does the inventory live? Probably a file in this repository, or a free form
3. How do we handle someone who does not use the form?
4. How should the wishlist (`bom/BOM.csv`) and the inventory connect?
5. How do we show the inventory to people before they make the trip?

## Wanted

- A paper mock-up of the took and left flow
- A tiny working form, built with a free tool
- A data format for "what is in the box"
- A weekly check list that updates the inventory

## How to start

1. Read the [integrations overview](../README.md) and the rules every track follows.
2. [Start a brief](../../../../issues/new?template=start-a-brief.yml), or copy the [template](../_template/README.md).
3. Post it. Others will comment. A short, honest brief is better than a polished one.
4. Say if an AI helped. See [ai-contribute.md](../../docs/ai-contribute.md).
5. Anything involving a battery, a lock, a camera, or structure needs review by a qualified person before it is built.
