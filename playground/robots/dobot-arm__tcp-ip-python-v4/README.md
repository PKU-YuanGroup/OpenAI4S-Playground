# Dobot V4 series arm (TCP/IP Python SDK)

`robots/dobot-arm__tcp-ip-python-v4` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Dobot V4 series arm (TCP/IP Python SDK), adapted from dobot-arm/tcp-ip-python-v4. It reads `joint_positions`, `tcp_pose`, `robot_mode` and `error_ids`; runs `move_joints`, `move_pose` and `stop_motion`. `move_joints`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/dobot-arm__tcp-ip-python-v4
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/dobot-arm__tcp-ip-python-v4 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tcp-ip-python-v4": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/dobot-arm__tcp-ip-python-v4",
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

- **Reads:** `joint_positions`, `tcp_pose`, `robot_mode`, `error_ids`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_joints` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |
| `move_pose` | Move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [dobot-arm/tcp-ip-python-v4](https://github.com/dobot-arm/tcp-ip-python-v4) at `55ec1ec82201` (MIT); fetch it with `python3 scripts/add_device.py robots/dobot-arm__tcp-ip-python-v4` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/dobot-arm__tcp-ip-python-v4`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/dobot-arm__tcp-ip-python-v4) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/dobot-arm__tcp-ip-python-v4/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/dobot-arm__tcp-ip-python-v4/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
