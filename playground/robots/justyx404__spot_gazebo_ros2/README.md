# Spot quadruped in an Ignition/Gazebo ROS 2 simulation

`robots/justyx404__spot_gazebo_ros2` · Mobile robots · simulation · risk R2 · licence Apache-2.0

Spot quadruped in an Ignition/Gazebo ROS 2 simulation, adapted from justyx404/spot_gazebo_ros2. It reads `read_odometry`, `read_joint_states` and `read_sim_clock`; runs `publish_velocity`. `publish_velocity`: publish one geometry_msgs/Twist on /cmd_vel; the receipt reports transmission and the three components handed to rosbridge, not motion, arrival or a stop. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/justyx404__spot_gazebo_ros2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/justyx404__spot_gazebo_ros2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "spot_gazebo_ros2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/justyx404__spot_gazebo_ros2",
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

- **Reads:** `read_odometry`, `read_joint_states`, `read_sim_clock`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_velocity` | Publish one geometry_msgs/Twist on /cmd_vel; the receipt reports transmission and the three components handed to rosbridge, not motion, arrival or a stop |

## Source and status

- Upstream: [justyx404/spot_gazebo_ros2](https://github.com/justyx404/spot_gazebo_ros2) at `23166d6efd67` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/justyx404__spot_gazebo_ros2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/justyx404__spot_gazebo_ros2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/justyx404__spot_gazebo_ros2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/justyx404__spot_gazebo_ros2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/justyx404__spot_gazebo_ros2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
