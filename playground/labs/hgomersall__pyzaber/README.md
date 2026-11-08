# Zaber multiaxis linear slides (pyzaber)

`labs/hgomersall__pyzaber` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Zaber multiaxis linear slides (pyzaber), adapted from hgomersall/pyzaber. It reads `x_mm`, `y_mm` and `z_mm`; runs `home`, `move_to_position` and `stop_motion`. `home`: home all three axes with the native home command (command 1); the clone's example homes x, y and z in turn. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/hgomersall__pyzaber
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/hgomersall__pyzaber --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pyzaber": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/hgomersall__pyzaber",
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

- **Reads:** `x_mm`, `y_mm`, `z_mm`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `home` | Home all three axes with the native home command (command 1); the clone's example homes x, y and z in turn |
| `move_to_position` | Move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. |
| `stop_motion` | Stop every axis with the native emergency-stop broadcast (command 23 to device 0); the safe state, and it takes no input |

## Source and status

- Upstream: [hgomersall/pyzaber](https://github.com/hgomersall/pyzaber) at `1a3f1e712f3d` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/hgomersall__pyzaber` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/hgomersall__pyzaber`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/hgomersall__pyzaber) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/hgomersall__pyzaber/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/hgomersall__pyzaber/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
