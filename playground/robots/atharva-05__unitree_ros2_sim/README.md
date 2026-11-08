# Unitree GO1 Gazebo simulation

`robots/atharva-05__unitree_ros2_sim` · Mobile robots · simulation · risk R2 · licence NOASSERTION

Unitree GO1 Gazebo simulation, adapted from atharva-05/unitree_ros2_sim. It reads `read_scan` and `read_odometry`; runs `publish_cmd_vel`. `publish_cmd_vel`: publish one geometry_msgs/Twist velocity setpoint to /cmd_vel for the move_base state machine. The receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/atharva-05__unitree_ros2_sim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/atharva-05__unitree_ros2_sim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "unitree_ros2_sim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/atharva-05__unitree_ros2_sim",
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

- **Reads:** `read_scan`, `read_odometry`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_cmd_vel` | Publish one geometry_msgs/Twist velocity setpoint to /cmd_vel for the move_base state machine. The receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. |

## Source and status

- Upstream: [atharva-05/unitree_ros2_sim](https://github.com/atharva-05/unitree_ros2_sim) at `446597041695` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/atharva-05__unitree_ros2_sim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/atharva-05__unitree_ros2_sim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/atharva-05__unitree_ros2_sim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/atharva-05__unitree_ros2_sim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/atharva-05__unitree_ros2_sim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
