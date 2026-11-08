# Multi-robot TurtleBot3 Gazebo/Nav stack

`robots/mortezaaliyari__multi-robot-gazebo-navistack` · Simulation · multi-robot systems · simulation · risk R2 · licence MIT

Multi-robot TurtleBot3 Gazebo/Nav stack, adapted from mortezaaliyari/multi-robot-gazebo-navistack. It reads `read_tb3_0_odom`, `read_tb3_0_scan`, `read_tb3_1_odom` and `read_tb3_1_scan`; runs `publish_tb30_cmd_vel`, `publish_tb31_cmd_vel` and `resume_simulation`. `publish_tb30_cmd_vel`: publish one geometry_msgs/Twist velocity setpoint to the tb3_0 Gazebo cmd_vel topic; the receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/mortezaaliyari__multi-robot-gazebo-navistack
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/mortezaaliyari__multi-robot-gazebo-navistack --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "multi-robot-gazebo-navistack": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/mortezaaliyari__multi-robot-gazebo-navistack",
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

- **Reads:** `read_tb3_0_odom`, `read_tb3_0_scan`, `read_tb3_1_odom`, `read_tb3_1_scan`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_tb30_cmd_vel` | Publish one geometry_msgs/Twist velocity setpoint to the tb3_0 Gazebo cmd_vel topic; the receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping |
| `publish_tb31_cmd_vel` | Publish one geometry_msgs/Twist velocity setpoint to the tb3_1 Gazebo cmd_vel topic; the receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping |
| `resume_simulation` | The declared re-enable after a safety reset: publish a zero Twist on /tb3_0/cmd_vel and /tb3_1/cmd_vel, then unpause the Gazebo world with /gazebo/unpause_physics. Each differential-drive plugin keeps the last cmd_vel it stored and applies it as soon as the world runs; the zeros replace them, but they are unacknowledged publications, so a stored command can still act for a few world steps, and a running move_base publishes new ones. |

## Source and status

- Upstream: [mortezaaliyari/multi-robot-gazebo-navistack](https://github.com/mortezaaliyari/multi-robot-gazebo-navistack) at `afcc20c73158` (MIT); fetch it with `python3 scripts/add_device.py robots/mortezaaliyari__multi-robot-gazebo-navistack` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/mortezaaliyari__multi-robot-gazebo-navistack`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/mortezaaliyari__multi-robot-gazebo-navistack) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/mortezaaliyari__multi-robot-gazebo-navistack/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/mortezaaliyari__multi-robot-gazebo-navistack/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
