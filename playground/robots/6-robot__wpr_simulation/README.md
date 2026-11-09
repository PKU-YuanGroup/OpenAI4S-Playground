# WPR Gazebo mobile-robot simulation

`robots/6-robot__wpr_simulation` · Simulation · mobile robots · simulation · risk R2 · licence GPL-3.0

WPR Gazebo mobile-robot simulation, adapted from 6-robot/wpr_simulation. It reads `read_odometry` and `read_pose_diff`; runs `publish_cmd_vel` and `resume_simulation`. `publish_cmd_vel`: publish one geometry_msgs/Twist velocity setpoint on /cmd_vel. The WPRPlugin callback stores the components, also while the world is paused; the receipt is transmission evidence and the values sent, not motion or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/6-robot__wpr_simulation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/6-robot__wpr_simulation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "wpr_simulation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/6-robot__wpr_simulation",
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

- **Reads:** `read_odometry`, `read_pose_diff`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_cmd_vel` | Publish one geometry_msgs/Twist velocity setpoint on /cmd_vel. The WPRPlugin callback stores the components, also while the world is paused; the receipt is transmission evidence and the values sent, not motion or stopping. |
| `resume_simulation` | The declared re-enable after a safety reset: publish a zero Twist on /cmd_vel, then unpause the Gazebo world with /gazebo/unpause_physics. WPRPlugin keeps the last cmd_vel it stored and applies it as soon as the world runs; the zero replaces it, but it is an unacknowledged publication, so a stored command can still act for a few world steps. |

## Source and status

- Upstream: [6-robot/wpr_simulation](https://github.com/6-robot/wpr_simulation) at `9c2861944205` (GPL-3.0); fetch it with `python3 scripts/add_device.py robots/6-robot__wpr_simulation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/6-robot__wpr_simulation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/6-robot__wpr_simulation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/6-robot__wpr_simulation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/6-robot__wpr_simulation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
