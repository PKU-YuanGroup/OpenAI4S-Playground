# ICRA RoboMaster AI Challenge simulator

`robots/yizhengzhang1__robomaster-simulator` · Simulation · multi-robot systems · simulation · risk R2 · licence LGPL-3.0

ICRA RoboMaster AI Challenge simulator, adapted from yizhengzhang1/robomaster-simulator. It reads `read_referee_state`; runs `pause_physics`, `unpause_physics`, `start_game`, `command_turret` and 1 more. `pause_physics`: pause Gazebo physics with the acknowledged /gazebo/pause_physics service. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/yizhengzhang1__robomaster-simulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/yizhengzhang1__robomaster-simulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "robomaster-simulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/yizhengzhang1__robomaster-simulator",
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

- **Reads:** `read_referee_state`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `pause_physics` | Pause Gazebo physics with the acknowledged /gazebo/pause_physics service |
| `unpause_physics` | Resume Gazebo physics with the acknowledged /gazebo/unpause_physics service |
| `start_game` | Ask the referee node to start or stop its game loop; the response only acknowledges receipt of the request |
| `command_turret` | Publish one turret angle in radians on /jackal0/turret_position; the publication carries no execution acknowledgement |
| `command_base_velocity` | Publish one body twist on /jackal0/cmd_vel; the mecanum controller applies its own velocity and acceleration limits and has no execution acknowledgement |

## Source and status

- Upstream: [yizhengzhang1/robomaster-simulator](https://github.com/yizhengzhang1/robomaster-simulator) at `ff085e4109a9` (LGPL-3.0); fetch it with `python3 scripts/add_device.py robots/yizhengzhang1__robomaster-simulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/yizhengzhang1__robomaster-simulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/yizhengzhang1__robomaster-simulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/yizhengzhang1__robomaster-simulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/yizhengzhang1__robomaster-simulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
