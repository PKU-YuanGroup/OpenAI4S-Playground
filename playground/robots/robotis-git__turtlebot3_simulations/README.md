# ROBOTIS TurtleBot3 fake simulation node

`robots/robotis-git__turtlebot3_simulations` · Simulation · simulation · risk R2 · licence Apache-2.0

ROBOTIS TurtleBot3 fake simulation node, adapted from robotis-git/turtlebot3_simulations. It reads `odom_pose`, `odom_twist`, `wheel_velocity`, `read_odometry` and 1 more; runs `publish_velocity`. `publish_velocity`: publish one geometry_msgs/Twist to the upstream /cmd_vel subscription; the fake node consumes only linear.x and angular.z. The receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. /cmd_vel is also a physical TurtleBot3 command topic, so this action is R2. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/robotis-git__turtlebot3_simulations
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/robotis-git__turtlebot3_simulations --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "turtlebot3_simulations": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/robotis-git__turtlebot3_simulations",
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

- **Reads:** `odom_pose`, `odom_twist`, `wheel_velocity`, `read_odometry`, `read_joint_states`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_velocity` | Publish one geometry_msgs/Twist to the upstream /cmd_vel subscription; the fake node consumes only linear.x and angular.z. The receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. /cmd_vel is also a physical TurtleBot3 command topic, so this action is R2. |

## Source and status

- Upstream: [robotis-git/turtlebot3_simulations](https://github.com/robotis-git/turtlebot3_simulations) at `9be186fb03d8` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/robotis-git__turtlebot3_simulations` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/robotis-git__turtlebot3_simulations`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/robotis-git__turtlebot3_simulations) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/robotis-git__turtlebot3_simulations/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/robotis-git__turtlebot3_simulations/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
