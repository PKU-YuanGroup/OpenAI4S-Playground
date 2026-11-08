# Unitree Go2 (Go2Py GO2Real)

`robots/machines-in-motion__go2py` · Mobile robots · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Unitree Go2 (Go2Py GO2Real), adapted from machines-in-motion/go2py. It reads `joint_positions`, `joint_velocities`, `joint_torques`, `motor_temperatures` and 6 more; runs `stop_motion`, `drive` and `command_joints`. `stop_motion`: stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/machines-in-motion__go2py
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/machines-in-motion__go2py --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "go2py": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/machines-in-motion__go2py",
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

- **Reads:** `joint_positions`, `joint_velocities`, `joint_torques`, `motor_temperatures`, `imu_acceleration`, `imu_angular_velocity`, `imu_orientation`, `imu_temperature`, `foot_contact_forces`, `battery_soc`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |
| `drive` | Command forward, lateral and yaw velocity through setCommandsHigh; the command stays in effect until another command or the stop action, because the clone documents no expiry |
| `command_joints` | Command 12 joint angles and 12 feedforward torques through setCommandsLow, with zero desired velocity and the upstream FSM's tracking gains kp 150 and kd 3; the target is sent at once, with no ramp from the current pose |

## Source and status

- Upstream: [machines-in-motion/go2py](https://github.com/machines-in-motion/go2py) at `eff240b82b0f` (MIT); fetch it with `python3 scripts/add_device.py robots/machines-in-motion__go2py` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/machines-in-motion__go2py`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/machines-in-motion__go2py) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/machines-in-motion__go2py/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/machines-in-motion__go2py/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
