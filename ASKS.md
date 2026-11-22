# Asks: I need a part

> **This is a proposal.** How asks work, and whether parts can be shipped to the lab, are open questions. See [DECISIONS.md](DECISIONS.md).

Need something for a project? Ask. Someone in the community may have it in a drawer.

An ask is a request for parts to be put **in the box**, where you and anyone else can pick them up.

## How to ask

1. Tap [Ask for a part](../../issues/new?template=ask-for-a-part.yml).
2. Say what you need, how many, and what you are building.
3. Tap **Submit new issue**.

Your ask appears on the [list of open asks](../../issues?q=is%3Aissue+is%3Aopen+label%3Aask). When someone fills it, they comment on your issue, and you collect the parts from the box.

Never used GitHub? [How to have your say](docs/have-your-say.md) shows you where to tap.

### A good ask

- Says exactly what: "3 soil moisture sensors, capacitive type" beats "some sensors"
- Asks for what you will use: a handful, not a hundred
- Says what it is for. People love helping a real project

## Start the ask list

The list starts empty, and it is yours to start. Asking is open now.

Good first asks:

- **Something small for a project you are doing.** One sensor, one cable, one connector
- **A part for a kid's project.** A parent can post it, and no ages or names are needed
- **A part you need to test a design.** See the [kit wishlist](bom/KITS.md) for the bench parts contributors need
- **A part you can not find locally.** Say what you tried

Please do not post an address, a phone number, an email, or a child's name or age.

Your AI can help you word it. See [ai-contribute.md](docs/ai-contribute.md).

## How to fill an ask

Browse the [open asks](../../issues?q=is%3Aissue+is%3Aopen+label%3Aask). When you can help, choose one of two ways.

### Way 1: Put it in the box yourself

1. Comment on the ask: "I've got this."
2. Bag and label the part with the ask number, for example "Ask #42".
3. Put it in the box.
4. Comment again: "It's in the box."

Until the box is built, parts go to the lab instead. **Please do not drop anything off yet.** Asking is open now. Physical drop-off will be posted here once the lab confirms.

### Way 2: Order it and have it delivered

> **Not confirmed yet. Please do not ship anything until this notice is removed.** The lab has to agree to receive packages first.

Order the part from any store and ship it to:

```
Swapatron5000
c/o Indiana IoT Lab
9059 Technology Lane
Fishers, IN 46038
```

Then comment on the ask with what you ordered and when it should arrive. A steward will put it in the box and mark the ask as filled.

**Shipping rules**

- No batteries by mail
- Nothing on the "not welcome" list in the [swap rules](docs/swap-rules.md)
- Small parcels only. Nobody at the lab can store a pallet
- Put the ask number on the order if the store allows a note or a second name line

## What you earn

Filling an ask is a contribution. It earns 1 point on the [Contributors Wall](CONTRIBUTORS.md), like any other part.

## Staying safe

- **Parts go to the box, never to a person.** Do not arrange to meet anyone, and do not ship to anyone's home.
- **No personal details.** Do not post your address, phone number, email, school, or age in an ask.
- **No money.** Asks are gifts. Nobody pays, and nobody is owed anything.
- A part left for your ask is still in a public box. Someone else may take it. That is how a swap box works.

## The box can ask too

Stewards post asks when the box runs low, for example "The box is out of jumper wires". These carry the `ask` label like any other, and anyone can fill them.

## For maintainers

- Check new asks for personal details and remove them.
- Close an ask when it is filled, or after 60 days with a friendly note.
- When a filled ask is confirmed, add a `part` line to `contributions.csv` for the giver.
