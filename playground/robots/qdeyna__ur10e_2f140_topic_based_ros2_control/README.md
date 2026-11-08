# UR10e arm (fake hardware)

`robots/qdeyna__ur10e_2f140_topic_based_ros2_control` · Robot arms and grippers · simulation · risk R2 · licence NOASSERTION

UR10e arm (fake hardware), adapted from qdeyna/ur10e_2f140_topic_based_ros2_control. It reads `joint_positions`, `joint_velocities` and `read_joint_state`; runs `follow_arm_trajectory` and `activate_trajectory_controller`. `follow_arm_trajectory`: send FollowJointTrajectory points on the fake-hardware scaled controller; return the controller error_code and error_string. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/qdeyna__ur10e_2f140_topic_based_ros2_control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/qdeyna__ur10e_2f140_topic_based_ros2_control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ur10e_2f140_topic_based_ros2_control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/qdeyna__ur10e_2f140_topic_based_ros2_control",
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
| `follow_arm_trajectory` | Send FollowJointTrajectory points on the fake-hardware scaled controller; return the controller error_code and error_string |
| `activate_trajectory_controller` | The declared re-enable after a safety reset: switch scaled_joint_trajectory_controller on again through /controller_manager/switch_controller (STRICT), so the trajectory the e-stop dropped is not resumed. On activation the controller holds the state it starts from. With this deployment's position-only command interface and position and velocity state interfaces, that is the measured position. Reset itself does not activate the controller |

## Source and status

- Upstream: [qdeyna/ur10e_2f140_topic_based_ros2_control](https://github.com/qdeyna/ur10e_2f140_topic_based_ros2_control) at `7db5397edae2` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/qdeyna__ur10e_2f140_topic_based_ros2_control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/qdeyna__ur10e_2f140_topic_based_ros2_control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/qdeyna__ur10e_2f140_topic_based_ros2_control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/qdeyna__ur10e_2f140_topic_based_ros2_control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/qdeyna__ur10e_2f140_topic_based_ros2_control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
