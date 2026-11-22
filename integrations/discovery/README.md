# Discovery

> **Draft. Nothing here is decided.** This is a starting brief. Every idea is a proposal, and every number is a guess until measured. See the [integrations overview](../README.md) and the [proposed baseline](../../DECISIONS.md).

## Goal

Two kinds of finding:

1. **People finding the box**, and seeing what is in it before they make the trip
2. **Devices finding each other**, so the box's sensors and gateway can talk without a lot of setup

## People finding the box

| Idea | Notes |
|---|---|
| A QR code on the box | The simplest. Opens a phone page |
| A web page with the box's status | What is in it, what it needs, when it was last checked |
| A listing of every box | A simple file in this repository could list each box and its town, if the network happens. See [your-swapatron.md](../../docs/your-swapatron.md) |
| A map | Later |
| Word of mouth | Still the best |

## Devices finding each other

| Idea | Notes |
|---|---|
| Fixed addresses | The simplest, and the most fragile |
| Local discovery on the network | Devices announce themselves. Needs care for security |
| A radio link such as LoRa or a mesh | For a box far from Wi-Fi. See [electronics/](../../electronics/README.md) |

None of these is chosen. Each one needs a brief.

## Open questions

1. What is the one thing a visitor most wants to know before they go?
2. Should a box's status be public, and what could go wrong if it is?
3. What is the smallest status page that would help?
4. How do a few devices find each other without a lot of setup, and safely?
5. If other towns hatch boxes, who keeps the list, and how does a box leave it?

## Wanted

- A paper sketch of the "what is in the box" page
- A list of facts a visitor wants, in order
- A simple file format for a box's status, with an example, marked as a proposal
- A comparison of Wi-Fi, LoRa, and no radio for the box

## How to start

1. Read the [integrations overview](../README.md) and the rules every track follows.
2. [Start a brief](../../../../issues/new?template=start-a-brief.yml), or copy the [template](../_template/README.md).
3. Post it. Others will comment. A short, honest brief is better than a polished one.
4. Say if an AI helped. See [ai-contribute.md](../../docs/ai-contribute.md).
5. Anything involving a battery, a lock, a camera, or structure needs review by a qualified person before it is built.
