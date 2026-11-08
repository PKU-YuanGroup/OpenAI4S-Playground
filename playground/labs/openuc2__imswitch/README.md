# OpenUC2 ESP32 microscope stage

`labs/openuc2__imswitch` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

OpenUC2 ESP32 microscope stage, adapted from openuc2/imswitch. It reads `x_um`, `y_um` and `z_um`; runs `move_xyz` and `stop_motion`. `move_xyz`: move the X, Y and Z stage axes to absolute positions in micrometres with the coordinated upstream XYZ move, and report the position a device query returns afterwards; a move whose native call raises or whose position query fails ends unknown. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/openuc2__imswitch
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/openuc2__imswitch --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "imswitch": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/openuc2__imswitch",
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

- **Reads:** `x_um`, `y_um`, `z_um`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_xyz` | Move the X, Y and Z stage axes to absolute positions in micrometres with the coordinated upstream XYZ move, and report the position a device query returns afterwards; a move whose native call raises or whose position query fails ends unknown |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [openuc2/imswitch](https://github.com/openuc2/imswitch) at `e5db60f1021b` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/openuc2__imswitch` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/openuc2__imswitch`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/openuc2__imswitch) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/openuc2__imswitch/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/openuc2__imswitch/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
