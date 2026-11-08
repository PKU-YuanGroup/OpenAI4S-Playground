# Yahboom ROSMASTER M3 Pro

`robots/strands-labs__robots` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence Apache-2.0

Yahboom ROSMASTER M3 Pro, adapted from strands-labs/robots. It reads `connected`, `observation`, `commanded_arm_pose` and `sensors`; runs `move_joints`, `home`, `set_gripper`, `drive_base` and 1 more. `move_joints`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/strands-labs__robots
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/strands-labs__robots --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "robots": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/strands-labs__robots",
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

- **Reads:** `connected`, `observation`, `commanded_arm_pose`, `sensors`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_joints` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |
| `home` | Move the arm to the vendor grasp-init pose with the gripper open |
| `set_gripper` | Open or close the gripper and leave the other five servos where they are |
| `drive_base` | Drive the mecanum base with a Twist in SI units for a bounded duration, then stop |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [strands-labs/robots](https://github.com/strands-labs/robots) at `f19439bf8c80` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/strands-labs__robots` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/strands-labs__robots`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/strands-labs__robots) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/strands-labs__robots/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/strands-labs__robots/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
