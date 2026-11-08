# BCR 7-DOF arm

`robots/blackcoffeerobotics__bcr_arm` · Robot arms and grippers · simulation · risk R2 · licence Apache-2.0

BCR 7-DOF arm, adapted from blackcoffeerobotics/bcr_arm. It reads `joint_positions`, `joint_velocities` and `read_joint_state`; runs `follow_arm_trajectory` and `activate_trajectory_controller`. `follow_arm_trajectory`: send FollowJointTrajectory points; return the controller error_code/error_string. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/blackcoffeerobotics__bcr_arm
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/blackcoffeerobotics__bcr_arm --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "bcr_arm": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/blackcoffeerobotics__bcr_arm",
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

- **Reads:** `joint_positions`, `joint_velocities`, `read_joint_state`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `follow_arm_trajectory` | Send FollowJointTrajectory points; return the controller error_code/error_string |
| `activate_trajectory_controller` | The declared re-enable after a safety reset: switch joint_trajectory_controller on again through /controller_manager/switch_controller (STRICT), so the trajectory the e-stop dropped is not resumed. On activation the controller holds the state it starts from: the last command-interface values when set_last_command_interface_value_as_state_on_activation (true by default) applies and every state interface has a command interface, else the measured joints. With this deployment's position-only command interface (position and velocity states) that is the measured position; a configuration that also commanded velocity would hold the last position command, which can differ from the measured position |

## Source and status

- Upstream: [blackcoffeerobotics/bcr_arm](https://github.com/blackcoffeerobotics/bcr_arm) at `9bd3d60b306b` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/blackcoffeerobotics__bcr_arm` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/blackcoffeerobotics__bcr_arm`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/blackcoffeerobotics__bcr_arm) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/blackcoffeerobotics__bcr_arm/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/blackcoffeerobotics__bcr_arm/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
