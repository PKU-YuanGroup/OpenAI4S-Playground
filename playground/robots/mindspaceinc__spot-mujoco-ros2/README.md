# MindSpaceInc Spot Mini MuJoCo ROS 2 simulator

`robots/mindspaceinc__spot-mujoco-ros2` · Mobile robots · simulation · risk R2 · licence NOASSERTION

MindSpaceInc Spot Mini MuJoCo ROS 2 simulator, adapted from mindspaceinc/spot-mujoco-ros2. It reads `joint_positions` and `read_joint_states`; runs `publish_actuator_cmds`, `reset_simulation` and `reset_safe_state`. `publish_actuator_cmds`: publish one communication/msg/ActuatorCmds message on /simulation/actuators_cmds with the 12 actuator names fixed in MJCF order. The node applies the PD expression and clamps each resulting ctrl to [-100, 100]; a publication receipt is transmission only, not motion. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/mindspaceinc__spot-mujoco-ros2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/mindspaceinc__spot-mujoco-ros2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "spot-mujoco-ros2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/mindspaceinc__spot-mujoco-ros2",
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

- **Reads:** `joint_positions`, `read_joint_states`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_actuator_cmds` | Publish one communication/msg/ActuatorCmds message on /simulation/actuators_cmds with the 12 actuator names fixed in MJCF order. The node applies the PD expression and clamps each resulting ctrl to [-100, 100]; a publication receipt is transmission only, not motion. |
| `reset_simulation` | Call the acknowledged /simulation/sim_reset service with the fixed frame_id spot, an optional base pose and optional 12 hinge positions. The callback calls mj_resetData, zeroes cached commands and returns is_success; it does not pause the physics loop. |
| `reset_safe_state` | Reset simulated data to the model defaults plus the fixed base pose with the acknowledged /simulation/sim_reset service. The callback calls mj_resetData and zeroes every cached actuator command; the MuJoCo physics loop keeps running. |

## Source and status

- Upstream: [mindspaceinc/spot-mujoco-ros2](https://github.com/mindspaceinc/spot-mujoco-ros2) at `1e07b87745ab` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/mindspaceinc__spot-mujoco-ros2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/mindspaceinc__spot-mujoco-ros2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/mindspaceinc__spot-mujoco-ros2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/mindspaceinc__spot-mujoco-ros2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/mindspaceinc__spot-mujoco-ros2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
