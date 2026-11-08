# Franka Hand ROS 1 gripper

`robots/frankarobotics__franka_ros` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence Apache-2.0

Franka Hand ROS 1 gripper, adapted from frankarobotics/franka_ros. It reads `finger_positions`; runs `grasp`, `move_gripper`, `home_gripper` and `stop_gripper`. `grasp`: close the gripper on a target object with a bounded force and report the achieved grasp width. A failed grasp is a completed operation with grasped=false, not a silent success. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/frankarobotics__franka_ros
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/frankarobotics__franka_ros --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "franka_ros": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/frankarobotics__franka_ros",
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

- **Reads:** `finger_positions`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `grasp` | Close the gripper on a target object with a bounded force and report the achieved grasp width. A failed grasp is a completed operation with grasped=false, not a silent success. |
| `move_gripper` | Move the gripper fingers to a total opening width with the upstream MoveAction |
| `home_gripper` | Home the gripper with the upstream HomingAction |
| `stop_gripper` | Request the independent native StopAction and confirm only after all older effects have settled and a fresh stop has succeeded |

## Source and status

- Upstream: [frankarobotics/franka_ros](https://github.com/frankarobotics/franka_ros) at `ddd2fffd9de4` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/frankarobotics__franka_ros` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/frankarobotics__franka_ros`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/frankarobotics__franka_ros) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/frankarobotics__franka_ros/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/frankarobotics__franka_ros/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
