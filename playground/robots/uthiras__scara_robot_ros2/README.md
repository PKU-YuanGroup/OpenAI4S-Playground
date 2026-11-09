# Uthira SCARA/RRP robot simulation

`robots/uthiras__scara_robot_ros2` · Robot arms and grippers · simulation · risk R2 · licence NOASSERTION

Uthira SCARA/RRP robot simulation, adapted from uthiras/scara_robot_ros2. It reads `read_joint_states` and `read_forward_kinematics_matrix`; runs `command_joint_efforts` and `forward_velocity_kinematics`. `command_joint_efforts`: publish one three-element joint effort command on the controller's command topic; the receipt confirms only that rosbridge accepted the publication and reports the efforts sent, not that a controller applied them, that the arm moved, or that it can stop. After an e-stop and reset the world stays paused, and a command sent then acts only when the operator unpauses it. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/uthiras__scara_robot_ros2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/uthiras__scara_robot_ros2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "scara_robot_ros2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/uthiras__scara_robot_ros2",
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

- **Reads:** `read_joint_states`, `read_forward_kinematics_matrix`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `command_joint_efforts` | Publish one three-element joint effort command on the controller's command topic; the receipt confirms only that rosbridge accepted the publication and reports the efforts sent, not that a controller applied them, that the arm moved, or that it can stop. After an e-stop and reset the world stays paused, and a command sent then acts only when the operator unpauses it |
| `forward_velocity_kinematics` | Call the observational Forward_Velocity_Kinematics service and return its end-effector velocity values; the service computes from the last joint state and does not command motion |

## Source and status

- Upstream: [uthiras/scara_robot_ros2](https://github.com/uthiras/scara_robot_ros2) at `ece3e91727b0` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/uthiras__scara_robot_ros2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/uthiras__scara_robot_ros2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/uthiras__scara_robot_ros2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/uthiras__scara_robot_ros2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/uthiras__scara_robot_ros2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
