# AgileX Scout V2 Gazebo empty world

`robots/agilexrobotics__ugv_gazebo_sim` · Simulation · mobile robots · simulation · risk R2 · licence NOASSERTION

AgileX Scout V2 Gazebo empty world, adapted from agilexrobotics/ugv_gazebo_sim. It runs `publish_cmd_vel`. `publish_cmd_vel`: publish geometry_msgs/Twist linear.x and angular.z on /cmd_vel. TwistCmdCallback converts them to four Float64 wheel commands and stores no Twist. The receipt is transmission evidence and the values sent, not a measured velocity and not a cleared controller. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/agilexrobotics__ugv_gazebo_sim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/agilexrobotics__ugv_gazebo_sim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ugv_gazebo_sim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/agilexrobotics__ugv_gazebo_sim",
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
| `publish_cmd_vel` | Publish geometry_msgs/Twist linear.x and angular.z on /cmd_vel. TwistCmdCallback converts them to four Float64 wheel commands and stores no Twist. The receipt is transmission evidence and the values sent, not a measured velocity and not a cleared controller. |

## Source and status

- Upstream: [agilexrobotics/ugv_gazebo_sim](https://github.com/agilexrobotics/ugv_gazebo_sim) at `27633a956c84` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/agilexrobotics__ugv_gazebo_sim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/agilexrobotics__ugv_gazebo_sim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/agilexrobotics__ugv_gazebo_sim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/agilexrobotics__ugv_gazebo_sim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/agilexrobotics__ugv_gazebo_sim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
