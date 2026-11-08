# Opentrons Temp Deck Gen 3

`labs/opentrons__opentrons-modules` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Opentrons Temp Deck Gen 3, adapted from opentrons/opentrons-modules. It reads `plate_temperature_1`, `plate_temperature_2`, `heatsink_temperature`, `peltier_current` and 2 more; sets `fan_power`; runs `set_target_temperature` and `deactivate`. `set_target_temperature`: set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/opentrons__opentrons-modules
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/opentrons__opentrons-modules --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "opentrons-modules": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/opentrons__opentrons-modules",
        "--mcp"
      ],
      "env": {
        "PYTHONPATH": "/path/to/OpenMHS/MHS/sdk/src"
      }
    }
  }
}
```

## What it exposes

- **Reads:** `plate_temperature_1`, `plate_temperature_2`, `heatsink_temperature`, `peltier_current`, `fan_speed`, `peltier_power`
- **Sets:** `fan_power`

| Action | What it does |
| --- | --- |
| `set_target_temperature` | Set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. |
| `deactivate` | Deactivate the thermal system (M18): clear the target, disable the peltier and set fan power 0 |

## Source and status

- Upstream: [opentrons/opentrons-modules](https://github.com/opentrons/opentrons-modules) at `bb98120ac93c` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/opentrons__opentrons-modules` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/opentrons__opentrons-modules`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/opentrons__opentrons-modules) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/opentrons__opentrons-modules/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/opentrons__opentrons-modules/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
