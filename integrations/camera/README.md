# Camera

> **Draft. Nothing here is decided.** This is a starting brief. Every idea is a proposal, and every number is a guess until measured. See the [integrations overview](../README.md) and the [proposed baseline](../../DECISIONS.md).

## The honest first question

**Should the box have a camera at all?** Maybe not. Parts can be counted with a door switch, a weight sensor, or a "took and left" form. A camera is the most sensitive thing in this project, and it can end up recording people, including children.

This track starts by asking that question. A brief that says "no camera, and here is why" is a great contribution.

## If the answer is "maybe"

Any camera design must start from these rules:

- Off by default, and needs its own `rfc` and a privacy review before it is designed in
- Looks only at the bins, never at the street, the building, or people
- Nothing leaves the device if it can be avoided. Count things, do not store pictures
- No face recognition, no tracking of people, no audio
- A clear sign on the box says exactly what the camera does
- Short retention, or none
- A physical way to switch it off, and a cover
- The site host can veto it

## Open questions

1. What would a camera tell us that a door switch and a form can not?
2. Can it work with no images stored, such as counting only?
3. Who decides what it sees, and how do we prove it?
4. How do we keep a camera pointed at bins from ever being pointed at a person?
5. Is the benefit worth the trust it costs?

## Wanted

- A one page "do we need a camera?" brief
- A comparison of camera and no-camera ways to count parts
- A privacy review checklist
- A sign that explains it in five seconds

## How to start

1. Read the [integrations overview](../README.md) and the rules every track follows.
2. [Start a brief](../../../../issues/new?template=start-a-brief.yml), or copy the [template](../_template/README.md).
3. Post it. Others will comment. A short, honest brief is better than a polished one.
4. Say if an AI helped. See [ai-contribute.md](../../docs/ai-contribute.md).
5. Anything involving a battery, a lock, a camera, or structure needs review by a qualified person before it is built.
