# Thorlabs APT stage controller (pyapt)

`labs/freespace__pyapt` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Thorlabs APT stage controller (pyapt), adapted from freespace/pyapt. It reads `velocity`, `moving`, `homed`, `forward_limit_active` and 4 more; sets `position`, `soft_limits`, `maximum_velocity` and `acceleration`; runs `home`, `move_relative` and `stop_motion`. `home`: drive axes to their declared home position or reference switch, establishing the coordinate reference needed by other motion capabilities. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/freespace__pyapt
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/freespace__pyapt --backend fake --port 7400
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
        "labs/freespace__pyapt",
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

- **Reads:** `velocity`, `moving`, `homed`, `forward_limit_active`, `reverse_limit_active`, `status`, `status_bits`, `minimum_velocity`
- **Sets:** `position`, `soft_limits`, `maximum_velocity`, `acceleration`

| Action | What it does |
| --- | --- |
| `home` | Drive axes to their declared home position or reference switch, establishing the coordinate reference needed by other motion capabilities. |
| `move_relative` | Move the stage relative to its current position; the driver waits for the move to finish |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [freespace/pyapt](https://github.com/freespace/pyapt) at `914a6f618cac` (MIT); fetch it with `python3 scripts/add_device.py labs/freespace__pyapt` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/freespace__pyapt`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/freespace__pyapt) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/freespace__pyapt/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/freespace__pyapt/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
