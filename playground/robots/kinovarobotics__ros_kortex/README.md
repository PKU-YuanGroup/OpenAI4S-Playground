# Kinova Kortex ROS 1 base stop services

`robots/kinovarobotics__ros_kortex` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

Kinova Kortex ROS 1 base stop services, adapted from kinovarobotics/ros_kortex. It runs `stop` and `apply_emergency_stop`. `stop`: invoke the acknowledged Kortex base/stop service; this reports the ROS callback result only, not a measured stopping position or zero velocity. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/kinovarobotics__ros_kortex
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/kinovarobotics__ros_kortex --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros_kortex": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/kinovarobotics__ros_kortex",
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

- **Reads:** —
- **Sets:** —

| Action | What it does |
| --- | --- |
| `stop` | Invoke the acknowledged Kortex base/stop service; this reports the ROS callback result only, not a measured stopping position or zero velocity |
| `apply_emergency_stop` | Invoke the acknowledged Kortex base/apply_emergency_stop service; this reports the ROS callback result only and does not claim a physical emergency stop |

## Source and status

- Upstream: [kinovarobotics/ros_kortex](https://github.com/kinovarobotics/ros_kortex) at `c3280d8a6a6b` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/kinovarobotics__ros_kortex` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/kinovarobotics__ros_kortex`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/kinovarobotics__ros_kortex) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/kinovarobotics__ros_kortex/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/kinovarobotics__ros_kortex/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
