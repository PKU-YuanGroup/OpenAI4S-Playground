# Panda Gazebo arm

`robots/rickstaa__panda-gazebo` · Robot arms and grippers · simulation · risk R2 · licence MIT

Panda Gazebo arm, adapted from rickstaa/panda-gazebo. It reads `joint_state`; runs `follow_joint_trajectory`, `set_gripper_width` and `lock_joints`. `follow_joint_trajectory`: forward arm waypoints through /panda_control_server/panda_arm/follow_joint_trajectory and return the controller terminal error_code. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/rickstaa__panda-gazebo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/rickstaa__panda-gazebo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "panda-gazebo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/rickstaa__panda-gazebo",
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

- **Reads:** `joint_state`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `follow_joint_trajectory` | Forward arm waypoints through /panda_control_server/panda_arm/follow_joint_trajectory and return the controller terminal error_code |
| `set_gripper_width` | Send a per-finger width and max effort through the wrapper gripper service; wait is false, so accepted means the goal was sent, not that the fingers reached it |
| `lock_joints` | Freeze all Panda arm and finger joints at their present position through the world plugin's joint-limit update; the acknowledgement is not a velocity measurement, and no unlock is declared |

## Source and status

- Upstream: [rickstaa/panda-gazebo](https://github.com/rickstaa/panda-gazebo) at `113df8afa8de` (MIT); fetch it with `python3 scripts/add_device.py robots/rickstaa__panda-gazebo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/rickstaa__panda-gazebo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/rickstaa__panda-gazebo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/rickstaa__panda-gazebo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/rickstaa__panda-gazebo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
