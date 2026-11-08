# Duke Humanoid V1 (biped_controller.BipedController)

`robots/generalroboticslab__dukehumanoidhardwarecontrol` · Mobile robots · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Duke Humanoid V1 (biped_controller.BipedController), adapted from generalroboticslab/dukehumanoidhardwarecontrol. It reads `joint_positions`, `joint_velocities`, `joint_currents`, `dof_position_target` and 6 more; sets `command_forward`, `command_lateral` and `command_yaw`; runs `control_step` and `halt`. `control_step`: run one closed-loop control step: update the command, refresh the observation, compute the policy action and write the motor target. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/generalroboticslab__dukehumanoidhardwarecontrol
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/generalroboticslab__dukehumanoidhardwarecontrol --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "dukehumanoidhardwarecontrol": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/generalroboticslab__dukehumanoidhardwarecontrol",
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

- **Reads:** `joint_positions`, `joint_velocities`, `joint_currents`, `dof_position_target`, `foot_force_raw`, `foot_contact`, `angular_velocity`, `gravity_vector`, `base_quaternion`, `sample_rate`
- **Sets:** `command_forward`, `command_lateral`, `command_yaw`

| Action | What it does |
| --- | --- |
| `control_step` | Run one closed-loop control step: update the command, refresh the observation, compute the policy action and write the motor target |
| `halt` | Stop the motors: set every motor's torque limit to 0 and end the EtherCAT motor loop, the first two steps of the upstream's check_termination |

## Source and status

- Upstream: [generalroboticslab/dukehumanoidhardwarecontrol](https://github.com/generalroboticslab/dukehumanoidhardwarecontrol) at `3a9c3cd4c8da` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/generalroboticslab__dukehumanoidhardwarecontrol` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/generalroboticslab__dukehumanoidhardwarecontrol`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/generalroboticslab__dukehumanoidhardwarecontrol) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/generalroboticslab__dukehumanoidhardwarecontrol/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/generalroboticslab__dukehumanoidhardwarecontrol/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
