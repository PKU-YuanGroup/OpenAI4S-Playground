# evronix quadruped ROS 2 Gazebo sim2sim

`robots/evronix__quadruped_sim2sim` · Simulation · simulation · risk R2 · licence MIT

evronix quadruped ROS 2 Gazebo sim2sim, adapted from evronix/quadruped_sim2sim. It reads `read_joint_states` and `read_imu`; runs `publish_velocity_command`. `publish_velocity_command`: publish one PoseStamped velocity setpoint on /robot_velocity_command; the receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/evronix__quadruped_sim2sim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/evronix__quadruped_sim2sim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "quadruped_sim2sim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/evronix__quadruped_sim2sim",
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

- **Reads:** `read_joint_states`, `read_imu`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_velocity_command` | Publish one PoseStamped velocity setpoint on /robot_velocity_command; the receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping |

## Source and status

- Upstream: [evronix/quadruped_sim2sim](https://github.com/evronix/quadruped_sim2sim) at `99040173a6ec` (MIT); fetch it with `python3 scripts/add_device.py robots/evronix__quadruped_sim2sim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/evronix__quadruped_sim2sim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/evronix__quadruped_sim2sim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/evronix__quadruped_sim2sim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/evronix__quadruped_sim2sim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
