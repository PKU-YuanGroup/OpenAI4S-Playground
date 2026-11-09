# Vacuubrand DCP 3000 vacuum controller

`labs/tiagocoutinho__vacuubrand` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence LGPL-3.0

Vacuubrand DCP 3000 vacuum controller, adapted from tiagocoutinho/vacuubrand. It reads `pressure`, `transducer_pressures`, `configuration`, `errors` and 2 more; sets `event_time_interval`, `on_setpoint_1`, `off_setpoint_1`, `on_setpoint_2` and 5 more; runs `measure_pressure`, `switch_on`, `switch_off`, `open_venting_valve` and 2 more. `measure_pressure`: measure absolute, gauge or differential pressure at a declared port and return the value with its reference and timestamp. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/tiagocoutinho__vacuubrand
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/tiagocoutinho__vacuubrand --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "vacuubrand": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/tiagocoutinho__vacuubrand",
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

- **Reads:** `pressure`, `transducer_pressures`, `configuration`, `errors`, `version`, `recording_time_interval`
- **Sets:** `event_time_interval`, `on_setpoint_1`, `off_setpoint_1`, `on_setpoint_2`, `off_setpoint_2`, `on_setpoint_3`, `off_setpoint_3`, `on_setpoint_4`, `off_setpoint_4`

| Action | What it does |
| --- | --- |
| `measure_pressure` | Measure absolute, gauge or differential pressure at a declared port and return the value with its reference and timestamp. |
| `switch_on` | Enter remote control (native REMOTE 1) |
| `switch_off` | Release remote control (native REMOTE -); it takes no input |
| `open_venting_valve` | Open the venting valve (native OUT_VENT 1); it takes no input |
| `close_venting_valve` | Close the venting valve (native OUT_VENT 0); it takes no input and is the safe-state valve command |
| `vent` | Vent until atmospheric pressure (native OUT_VENT 2); it takes no input |

## Source and status

- Upstream: [tiagocoutinho/vacuubrand](https://github.com/tiagocoutinho/vacuubrand) at `12b2e12aa438` (LGPL-3.0); fetch it with `python3 scripts/add_device.py labs/tiagocoutinho__vacuubrand` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/tiagocoutinho__vacuubrand`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/tiagocoutinho__vacuubrand) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/tiagocoutinho__vacuubrand/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/tiagocoutinho__vacuubrand/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
