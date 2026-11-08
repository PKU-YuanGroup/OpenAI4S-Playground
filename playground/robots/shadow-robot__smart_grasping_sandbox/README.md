# Shadow Smart Grasping Sandbox

`robots/shadow-robot__smart_grasping_sandbox` · Robot arms and grippers · simulation · risk R2 · licence GPL-3.0

Shadow Smart Grasping Sandbox, adapted from shadow-robot/smart_grasping_sandbox. It reads `read_joint_states` and `read_object_pose`; runs `pause_physics`, `unpause_physics`, `reset_world`, `home_configuration` and 2 more. `pause_physics`: pause the Gazebo simulation through /gazebo/pause_physics. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/shadow-robot__smart_grasping_sandbox
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/shadow-robot__smart_grasping_sandbox --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "smart_grasping_sandbox": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/shadow-robot__smart_grasping_sandbox",
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

- **Reads:** `read_joint_states`, `read_object_pose`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `pause_physics` | Pause the Gazebo simulation through /gazebo/pause_physics |
| `unpause_physics` | Resume the Gazebo simulation through /gazebo/unpause_physics |
| `reset_world` | Reset the Gazebo world through /gazebo/reset_world |
| `home_configuration` | Teleport the 15 UR10 and H1 joints to SmartGrasper.reset_world's fixed configuration through /gazebo/set_model_configuration, without stopping the controllers or pausing physics as reset_world does, so the running controllers can drive the joints back |
| `open_hand` | Teleport the nine H1 hand joints to the SRDF open group state through /gazebo/set_model_configuration; the running hand controller can drive them back |
| `close_hand` | Teleport the nine H1 hand joints to the SRDF close group state through /gazebo/set_model_configuration; the running hand controller can drive them back |

## Source and status

- Upstream: [shadow-robot/smart_grasping_sandbox](https://github.com/shadow-robot/smart_grasping_sandbox) at `6f8de0600126` (GPL-3.0); fetch it with `python3 scripts/add_device.py robots/shadow-robot__smart_grasping_sandbox` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/shadow-robot__smart_grasping_sandbox`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/shadow-robot__smart_grasping_sandbox) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/shadow-robot__smart_grasping_sandbox/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/shadow-robot__smart_grasping_sandbox/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
