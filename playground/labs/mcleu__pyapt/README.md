# Thorlabs APT motion controller (PyAPT)

`labs/mcleu__pyapt` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Thorlabs APT motion controller (PyAPT), adapted from mcleu/pyapt. It reads `connected`, `stage_minimum`, `stage_maximum`, `stage_units` and 6 more; sets `position`, `acceleration` and `maximum_velocity`; runs `move_relative`, `home` and `stop_stage`. `move_relative`: move the stage relative to its current position; mRel waits for the move and the driver returns the position the controller reports afterwards. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/mcleu__pyapt
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/mcleu__pyapt --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pyapt": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/mcleu__pyapt",
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

- **Reads:** `connected`, `stage_minimum`, `stage_maximum`, `stage_units`, `pitch`, `minimum_velocity`, `maximum_acceleration_limit`, `maximum_velocity_limit`, `reverse_limit_switch`, `forward_limit_switch`
- **Sets:** `position`, `acceleration`, `maximum_velocity`

| Action | What it does |
| --- | --- |
| `move_relative` | Move the stage relative to its current position; mRel waits for the move and the driver returns the position the controller reports afterwards |
| `home` | Home the stage with the controller's configured homing parameters; go_home waits for the move and the driver returns the position the controller reports afterwards |
| `stop_stage` | Stop stage motion with the native APT profiled stop (MOT_StopProfiled); it takes no input |

## Source and status

- Upstream: [mcleu/pyapt](https://github.com/mcleu/pyapt) at `2d5c4c64350d` (MIT); fetch it with `python3 scripts/add_device.py labs/mcleu__pyapt` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/mcleu__pyapt`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/mcleu__pyapt) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/mcleu__pyapt/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/mcleu__pyapt/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
