# HECTOR humanoid Gazebo simulation

`robots/drcl-usc__hector_simulation` · Simulation · humanoid robots · simulation · risk R2 · licence BSD-3-Clause

HECTOR humanoid Gazebo simulation, adapted from drcl-usc/hector_simulation. It reads `read_model_states`; runs `send_left_hip_command`, `send_left_hip2_command`, `send_left_thigh_command`, `send_left_calf_command` and 6 more. `send_left_hip_command`: publish one unitree_legged_msgs/MotorCmd for the simulated left_hip joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/drcl-usc__hector_simulation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/drcl-usc__hector_simulation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "hector_simulation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/drcl-usc__hector_simulation",
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

- **Reads:** `read_model_states`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `send_left_hip_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated left_hip joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |
| `send_left_hip2_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated left_hip2 joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |
| `send_left_thigh_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated left_thigh joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |
| `send_left_calf_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated left_calf joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |
| `send_left_toe_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated left_toe joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |
| `send_right_hip_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated right_hip joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |
| `send_right_hip2_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated right_hip2 joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |
| `send_right_thigh_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated right_thigh joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |
| `send_right_calf_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated right_calf joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |
| `send_right_toe_command` | Publish one unitree_legged_msgs/MotorCmd for the simulated right_toe joint. The receipt proves only that rosbridge accepted the publication; it does not prove that the controller applied it, that the joint moved, or that the robot is stable. |

## Source and status

- Upstream: [drcl-usc/hector_simulation](https://github.com/drcl-usc/hector_simulation) at `edfdc7b1a985` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/drcl-usc__hector_simulation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/drcl-usc__hector_simulation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/drcl-usc__hector_simulation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/drcl-usc__hector_simulation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/drcl-usc__hector_simulation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
