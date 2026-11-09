# Webots gym_env Panda bridge

`robots/alexanderkeijzer__ros-gym-env-webots` · Simulation · mobile robots · simulation · risk R2 · licence NOASSERTION

Webots gym_env Panda bridge, adapted from alexanderkeijzer/ros-gym-env-webots. It reads `read_joint_positions` and `read_reward`; runs `act_and_step`, `step_simulation` and `reset_simulation`. `act_and_step`: publish one normalized nine-joint action vector, request one Webots time_step and read the joint positions after it; a failure after the publication is an unknown outcome, and the observation does not prove that the node applied the action before the step. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/alexanderkeijzer__ros-gym-env-webots
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/alexanderkeijzer__ros-gym-env-webots --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros-gym-env-webots": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/alexanderkeijzer__ros-gym-env-webots",
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

- **Reads:** `read_joint_positions`, `read_reward`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `act_and_step` | Publish one normalized nine-joint action vector, request one Webots time_step and read the joint positions after it; a failure after the publication is an unknown outcome, and the observation does not prove that the node applied the action before the step |
| `step_simulation` | Request one Webots robot/time_step advance through the gym_env step service |
| `reset_simulation` | Reset the Webots simulation through the gym_env reset service |

## Source and status

- Upstream: [alexanderkeijzer/ros-gym-env-webots](https://github.com/alexanderkeijzer/ros-gym-env-webots) at `6cc613bdee4b` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/alexanderkeijzer__ros-gym-env-webots` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/alexanderkeijzer__ros-gym-env-webots`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/alexanderkeijzer__ros-gym-env-webots) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/alexanderkeijzer__ros-gym-env-webots/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/alexanderkeijzer__ros-gym-env-webots/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
