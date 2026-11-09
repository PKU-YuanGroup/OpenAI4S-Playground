# Coppolam ROS MAV swarm simulator (uav1)

`robots/coppolam__ros_mav_swarm_simulator` · Simulation · UAVs · simulation · risk R2 · licence NOASSERTION

Coppolam ROS MAV swarm simulator (uav1), adapted from coppolam/ros_mav_swarm_simulator. It reads `read_odometry`; runs `set_velocity`, `enable_motors` and `land`. `set_velocity`: publish one geometry_msgs/Twist velocity command on /uav1/cmd_vel; the receipt reports the values sent and confirms transmission only, not arrival, motion or a continuous stream. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/coppolam__ros_mav_swarm_simulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/coppolam__ros_mav_swarm_simulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros_mav_swarm_simulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/coppolam__ros_mav_swarm_simulator",
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
| `set_velocity` | Publish one geometry_msgs/Twist velocity command on /uav1/cmd_vel; the receipt reports the values sent and confirms transmission only, not arrival, motion or a continuous stream |
| `enable_motors` | Send the fixed EnableMotors enable=true request on /uav1/enable_motors; success is the service response flag, not a sensed motor state |
| `land` | Land below the current pose and disable motors through hector_uav_msgs/LandingAction; an ordinary command, not a stop: its pose goal re-enables the motors first |

## Source and status

- Upstream: [coppolam/ros_mav_swarm_simulator](https://github.com/coppolam/ros_mav_swarm_simulator) at `eca05eaaecc0` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/coppolam__ros_mav_swarm_simulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/coppolam__ros_mav_swarm_simulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/coppolam__ros_mav_swarm_simulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/coppolam__ros_mav_swarm_simulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/coppolam__ros_mav_swarm_simulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
