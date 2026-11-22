# Electronics team

We add power, light, and sensing to the box. This is Phase 5 work, but planning can start now.

> **Draft. Nothing here is decided.** This page is a starting point for discussion. See [DECISIONS.md](../DECISIONS.md) and [how to have your say](../docs/have-your-say.md).

## Proposed ground rules

- The box must work with no electronics at all. Everything here is an add-on.
- No mains power.
- Any battery design must name the chemistry, the temperature rating, and the enclosure.
- Electronics live in a weatherproof enclosure rated IP65 or better.

## Modules we want

| Module | What it does | Status |
|---|---|---|
| Power | Small solar panel, charge controller, battery | Needs owner |
| Lighting | LED strip that turns on when the door opens | Needs owner |
| Sensor node | Temperature, humidity, and a door switch | Needs owner |
| Radio link | Sends sensor data out. Lab Wi-Fi or LoRa | Needs a decision |

The detailed briefs for power, safety, and radio live in [integrations/](../integrations/README.md). Start there.

## Open questions

1. How much power does the whole thing need per day? We need a power budget before picking a panel and battery.
2. Which battery chemistry is safe from an Indiana winter to a July afternoon inside a closed box?
3. Wi-Fi or LoRa?
4. What data format does the sensor node send? Agree this with the software team.

## How to contribute

Put each module in its own folder, for example `electronics/sensor-node/`, with a schematic, a parts list, firmware, and a short README.
