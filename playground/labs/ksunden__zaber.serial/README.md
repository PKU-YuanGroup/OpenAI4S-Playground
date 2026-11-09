# Zaber serial axis (zaber.serial.ascii.AsciiAxis)

`labs/ksunden__zaber.serial` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence Apache-2.0

Zaber serial axis (zaber.serial.ascii.AsciiAxis), adapted from ksunden/zaber.serial. It reads `position` and `status`; runs `home_axis`, `move_abs`, `move_rel`, `move_vel` and 1 more. `home_axis`: send the native home command and wait until the axis reports idle. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ksunden__zaber.serial
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ksunden__zaber.serial --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "zaber.serial": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ksunden__zaber.serial",
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

- **Reads:** `position`, `status`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `home_axis` | Send the native home command and wait until the axis reports idle |
| `move_abs` | Move the axis to an absolute native position in microsteps and wait until idle |
| `move_rel` | Move the axis by a relative distance in microsteps and wait until idle |
| `move_vel` | Start continuous motion at a native speed; call stop to end it |
| `stop_axis` | Stop the axis with the native stop command and wait until it reports idle |

## Source and status

- Upstream: [ksunden/zaber.serial](https://github.com/ksunden/zaber.serial) at `4bd9e1103f6a` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/ksunden__zaber.serial` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ksunden__zaber.serial`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ksunden__zaber.serial) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ksunden__zaber.serial/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ksunden__zaber.serial/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
