# Opentrons OT-2 (HTTP wrapper)

`labs/steiva__opentrons-ot2-http-python-wrapper` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Opentrons OT-2 (HTTP wrapper), adapted from steiva/opentrons-ot2-http-python-wrapper. It reads `robot_model` and `run_count`; runs `aspirate`, `dispense`, `create_run`, `load_pipette` and 4 more. `aspirate`: draw a specified volume of liquid from a declared labware well into a pipette tip, with a bounded flow rate and an optional liquid-level offset. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/steiva__opentrons-ot2-http-python-wrapper
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/steiva__opentrons-ot2-http-python-wrapper --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "opentrons-ot2-http-python-wrapper": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/steiva__opentrons-ot2-http-python-wrapper",
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

- **Reads:** `robot_model`, `run_count`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `aspirate` | Draw a specified volume of liquid from a declared labware well into a pipette tip, with a bounded flow rate and an optional liquid-level offset. |
| `dispense` | Dispense a specified volume from the pipette into a declared labware well, with optional blowout and mixing after dispense. |
| `create_run` | Create a run on the robot; needed before pipette, labware, movement and fluid commands |
| `load_pipette` | Load the configured pipette on a mount |
| `load_labware` | Load labware into a deck slot |
| `home` | Home the robot gantry |
| `control_run` | Play, pause, stop or recover the current run |
| `stop_run` | Stop the current run (the safe-state action); it takes no input |

## Source and status

- Upstream: [steiva/opentrons-ot2-http-python-wrapper](https://github.com/steiva/opentrons-ot2-http-python-wrapper) at `6bf929c11fe9` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/steiva__opentrons-ot2-http-python-wrapper` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/steiva__opentrons-ot2-http-python-wrapper`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/steiva__opentrons-ot2-http-python-wrapper) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/steiva__opentrons-ot2-http-python-wrapper/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/steiva__opentrons-ot2-http-python-wrapper/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
