# UR5LegoVision UR5 ROS 1 arm

`robots/anhtuduong__ur5legovision` · Robot arms and grippers · simulation · risk R2 · licence MIT

UR5LegoVision UR5 ROS 1 arm, adapted from anhtuduong/ur5legovision. It reads `read_joint_state` and `read_ee_pose`; runs `move_joints`, `move_gripper`, `pause` and `resume`. `move_joints`: command six joint positions through the upstream /ur5/move_joints service; the boolean acknowledgement does not establish measured arrival. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/anhtuduong__ur5legovision
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/anhtuduong__ur5legovision --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ur5legovision": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/anhtuduong__ur5legovision",
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

- **Reads:** `read_joint_state`, `read_ee_pose`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_joints` | Command six joint positions through the upstream /ur5/move_joints service; the boolean acknowledgement does not establish measured arrival |
| `move_gripper` | Command the soft-gripper opening diameter through /ur5/move_gripper; the ack means the upstream loop finished, not that an object was grasped |
| `pause` | Pause the Gazebo simulation with the acknowledged /gazebo/pause_physics service |
| `resume` | Resume the Gazebo simulation with the acknowledged /gazebo/unpause_physics service; an interrupted motion callback then continues its old motion |

## Source and status

- Upstream: [anhtuduong/ur5legovision](https://github.com/anhtuduong/ur5legovision) at `7cf487fbadcf` (MIT); fetch it with `python3 scripts/add_device.py robots/anhtuduong__ur5legovision` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/anhtuduong__ur5legovision`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/anhtuduong__ur5legovision) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/anhtuduong__ur5legovision/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/anhtuduong__ur5legovision/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
