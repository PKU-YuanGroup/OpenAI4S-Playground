# Tricontinent C3000 syringe pump (PyLabware)

`labs/croningp__pylabware` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Tricontinent C3000 syringe pump (PyLabware), adapted from croningp/pylabware. It reads `plunger_position`, `initialized`, `idle` and `connected`; sets `valve_position`; runs `transfer`, `move_plunger`, `move_home`, `set_speed` and 6 more. `transfer`: dispense or withdraw a number of plunger increments. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/croningp__pylabware
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/croningp__pylabware --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pylabware": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/croningp__pylabware",
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

- **Reads:** `plunger_position`, `initialized`, `idle`, `connected`
- **Sets:** `valve_position`

| Action | What it does |
| --- | --- |
| `transfer` | Dispense or withdraw a number of plunger increments |
| `move_plunger` | Move the plunger to an absolute or a relative position |
| `move_home` | Home the plunger with the native move_home (an absolute move to position 0) |
| `set_speed` | Set the maximum plunger velocity in increments per second |
| `set_start_velocity` | Set the starting velocity of the plunger ramp |
| `set_stop_velocity` | Set the cut-off velocity at the end of the plunger ramp |
| `set_predefined_speed` | Select a predefined maximum-velocity code (SPEED_MODES) |
| `set_ramp_slope` | Select an acceleration/deceleration ramp code (RAMP_PLOPE_MODES) |
| `set_resolution_mode` | Select the plunger motor resolution mode N0, N1 or N2 |
| `stop_pump` | Safe state: stop the current plunger program with the native stop (T); it takes no input |

## Source and status

- Upstream: [croningp/pylabware](https://github.com/croningp/pylabware) at `fbf287c7866a` (MIT); fetch it with `python3 scripts/add_device.py labs/croningp__pylabware` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/croningp__pylabware`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/croningp__pylabware) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/croningp__pylabware/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/croningp__pylabware/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
