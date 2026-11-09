# CrazyS Crazyflie 2.0 simulator

`robots/gsilano__crazys` · Simulation · UAVs · simulation · risk R2 · licence Apache-2.0

CrazyS Crazyflie 2.0 simulator, adapted from gsilano/crazys. It reads `read_odometry`; runs `publish_attitude_thrust`. `publish_attitude_thrust`: publish a roll/pitch/yaw-rate/thrust setpoint on the Crazyflie command topic; publication is fire-and-forget and does not confirm flight or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/gsilano__crazys
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/gsilano__crazys --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "crazys": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/gsilano__crazys",
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

- **Reads:** `read_odometry`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_attitude_thrust` | Publish a roll/pitch/yaw-rate/thrust setpoint on the Crazyflie command topic; publication is fire-and-forget and does not confirm flight or stopping |

## Source and status

- Upstream: [gsilano/crazys](https://github.com/gsilano/crazys) at `c7ee25a7c6f8` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/gsilano__crazys` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/gsilano__crazys`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/gsilano__crazys) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/gsilano__crazys/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/gsilano__crazys/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
