# Zaber microscopy stage (pymista.ZaberStage)

`labs/wetenschaap__pymista` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Zaber microscopy stage (pymista.ZaberStage), adapted from wetenschaap/pymista. It reads `position`, `moving` and `homed`; runs `move_absolute`, `move_relative`, `home_axes` and `stop_motion`. `move_absolute`: move the axes to absolute positions in micrometres and wait until the stage is idle. The array names the leading axes in order; trailing axes keep their current position. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/wetenschaap__pymista
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/wetenschaap__pymista --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymista": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/wetenschaap__pymista",
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

- **Reads:** `position`, `moving`, `homed`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_absolute` | Move the axes to absolute positions in micrometres and wait until the stage is idle. The array names the leading axes in order; trailing axes keep their current position. |
| `move_relative` | Move the axes by relative displacements in micrometres and wait until the stage is idle. The array names the leading axes in order; trailing axes do not move. |
| `home_axes` | Home every axis with the native force homing and report whether every axis is homed. It takes no input. |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [wetenschaap/pymista](https://github.com/wetenschaap/pymista) at `b30040a192c3` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/wetenschaap__pymista` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/wetenschaap__pymista`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/wetenschaap__pymista) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/wetenschaap__pymista/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/wetenschaap__pymista/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
