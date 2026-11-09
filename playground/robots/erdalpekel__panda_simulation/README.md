# Panda arm in Gazebo simulation

`robots/erdalpekel__panda_simulation` · Robot arms and grippers · simulation · risk R2 · licence MIT

Panda arm in Gazebo simulation, adapted from erdalpekel/panda_simulation. It reads `read_joint_states`; runs `command_joint_positions` and `stop_robot`. `command_joint_positions`: publish seven arm joint positions to the custom joint-position controller; the topic has no acknowledgement, so the output reports publication only. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/erdalpekel__panda_simulation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/erdalpekel__panda_simulation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "panda_simulation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/erdalpekel__panda_simulation",
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

- **Reads:** `read_joint_states`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `command_joint_positions` | Publish seven arm joint positions to the custom joint-position controller; the topic has no acknowledgement, so the output reports publication only |
| `stop_robot` | Call /robot_control_stop: its callback calls move_group_arm->stop() for the panda_arm MoveIt group and returns true unconditionally; not a stop of the joint-position command and not a safe state |

## Source and status

- Upstream: [erdalpekel/panda_simulation](https://github.com/erdalpekel/panda_simulation) at `70b6a9d7a426` (MIT); fetch it with `python3 scripts/add_device.py robots/erdalpekel__panda_simulation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/erdalpekel__panda_simulation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/erdalpekel__panda_simulation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/erdalpekel__panda_simulation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/erdalpekel__panda_simulation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
