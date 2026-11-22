# Security

> **Draft. Nothing here is decided.** This is a starting brief. Every idea is a proposal, and every number is a guess until measured. See the [integrations overview](../README.md) and the [proposed baseline](../../DECISIONS.md).

## Goal

Protect the box, its data, and any network it joins, without locking out the people it is for. Keep it simple and honest. It is a box of spare parts, not a bank.

## What we are protecting

| Thing | From |
|---|---|
| The parts | Someone taking everything, or dumping junk. Maybe that is fine. See [CHALLENGES.md](../../CHALLENGES.md) |
| The people using it | Anything unsafe, and any data collected about them |
| The lab's network | Anything on the box that could be a way in |
| The project | Stolen credit, fake boxes, tampered files |
| The box itself | Vandalism and theft |

## Rules to start from

- The box works with no network and no accounts
- Anything on the network is outbound only where possible, and kept apart from the lab's own network
- No secrets, keys, or passwords in this repository, ever
- Devices can be updated, and can be switched off
- Any lock needs its own `rfc`. It must never trap anything, and must have a manual way open. See the unlock-through-GitHub draft in [issue-drafts.md](../../docs/issue-drafts.md)
- Collect the least data possible

## Open questions

1. Do we need a lock at all? What does it protect, and what does it cost in friction?
2. What is the simplest threat model for a box like this?
3. How does a device join a network safely, and how does it leave?
4. How do we update firmware without a trip to the box?
5. How do we know a "Swapatron" elsewhere is the real project, or a safe one?

## Wanted

- A one page threat model
- A "what could a vandal do" list, and how to make it boring
- A checklist for putting a device on the lab's network, written for the lab's staff
- A short guide to safe defaults for the box's devices

## How to start

1. Read the [integrations overview](../README.md) and the rules every track follows.
2. [Start a brief](../../../../issues/new?template=start-a-brief.yml), or copy the [template](../_template/README.md).
3. Post it. Others will comment. A short, honest brief is better than a polished one.
4. Say if an AI helped. See [ai-contribute.md](../../docs/ai-contribute.md).
5. Anything involving a battery, a lock, a camera, or structure needs review by a qualified person before it is built.
