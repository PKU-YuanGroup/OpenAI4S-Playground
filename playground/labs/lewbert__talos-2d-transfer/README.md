# Zolix ZC300 XYR sample stage (talos.hal.devices.zolix:ZolixXYRStage)

`labs/lewbert__talos-2d-transfer` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

Zolix ZC300 XYR sample stage (talos.hal.devices.zolix:ZolixXYRStage), adapted from lewbert/talos-2d-transfer. It reads `x_um`, `y_um`, `r_deg`, `moving` and 2 more; runs `move_abs` and `stop_motion`. `move_abs`: move the stage to an absolute X/Y position (and R when given) and wait, bounded by the request deadline, until the controller reports no axis moving; the position it reports is returned. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/lewbert__talos-2d-transfer
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/lewbert__talos-2d-transfer --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "talos-2d-transfer": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/lewbert__talos-2d-transfer",
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

- **Reads:** `x_um`, `y_um`, `r_deg`, `moving`, `estop_active`, `alarm`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_abs` | Move the stage to an absolute X/Y position (and R when given) and wait, bounded by the request deadline, until the controller reports no axis moving; the position it reports is returned |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [lewbert/talos-2d-transfer](https://github.com/lewbert/talos-2d-transfer) at `2b85b6a9c74b` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/lewbert__talos-2d-transfer` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/lewbert__talos-2d-transfer`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/lewbert__talos-2d-transfer) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/lewbert__talos-2d-transfer/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/lewbert__talos-2d-transfer/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
