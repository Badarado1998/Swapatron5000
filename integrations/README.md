# IoT integrations

**How the box could sense, remember, power, protect, and announce itself. All of it is a proposal, and none of it is built.**

> **Nothing is decided yet.** The box must work with no electronics at all. Everything here is an add-on, and some of it may never happen. A good integration brief can end with "we should not do this."

The six tracks below are open. Pick one and start with a brief. You do not have to build anything.

## The tracks

| Track | Goal | Status | Start here |
|---|---|---|---|
| **Camera** | Decide whether a camera belongs in the box at all, and how to do it without harming privacy | Needs owner. Needs an `rfc` and a privacy review before anything is built | [camera/](camera/README.md) |
| **Inventory** | Know what is in the box, with as little effort as possible | Needs owner | [inventory/](inventory/README.md) |
| **Solar and power** | Keep any electronics running safely, in all weather | Needs owner. Any battery needs expert review | [solar/](solar/README.md) |
| **Safety** | Spot damp, heat, tampering, or damage before someone gets hurt | Needs owner | [safety/](safety/README.md) |
| **Security** | Protect the box, its data, and its network, without locking people out | Needs owner. A lock needs an `rfc` | [security/](security/README.md) |
| **Discovery** | Help people find the box and see what is in it, and help devices find each other | Needs owner | [discovery/](discovery/README.md) |

## How a track grows

Every track climbs the same ladder. Each step is a small thing that anyone can do.

| Step | What it is | Who can do it |
|---|---|---|
| 1. Idea | A sentence or a sketch | Anyone |
| 2. Brief | A short page from the [template](_template/README.md): goal, risks, questions | Anyone |
| 3. RFC | A proposal that others comment on for at least seven days. Needed for any camera, lock, or battery | Anyone, reviewed by maintainers |
| 4. Prototype | A bench test, on a desk, not in the box | Anyone with the [kit](../bom/KITS.md) |
| 5. Review | A qualified person checks the safety, privacy, and structure | A qualified human |
| 6. Adopted | Written in [DECISIONS.md](../DECISIONS.md) | The community and the site host |

## Rules every track follows

These are the project's proposed baseline. See [DECISIONS.md](../DECISIONS.md).

- No mains power in or on the box
- Nothing that collects personal data by default
- No account needed to use the box
- Any camera, microphone, or lock needs its own `rfc` and review before it is designed in
- Children use the box. Nothing in it should be unsafe for them
- The site host can veto anything on its property
- A qualified human reviews anything about batteries, electricity, or structure before it is built. An AI can draft. It can not sign off
- The box must work, and keep working, if the electronics fail

## How the tracks fit together

| Track | Needs from | Gives to |
|---|---|---|
| Solar and power | Safety (temperature limits) | Everything else, if it has power |
| Safety | Power, Inventory | Alerts to stewards |
| Inventory | Discovery (so people see it) | Discovery, the wishlist |
| Discovery | Inventory, Security | The network of boxes |
| Security | Everything | Everything |
| Camera | Security, Privacy review | Inventory, only if approved |

## Shared questions

1. What does the box send out, and in what format? (A simple file, a message, a web page?)
2. Where does the data live? (In this repository, on the lab's network, or nowhere?)
3. Who can see it? Stewards only, or everyone?
4. What happens when the network is down?
5. What is the cheapest, simplest version that would still help?

Start a brief: [Start a brief](../../../issues/new?template=start-a-brief.yml).
