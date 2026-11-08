# UFACTORY xArm 7 (xarm.XArmAPI)

`robots/xarm-developer__xarm-python-sdk` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

UFACTORY xArm 7 (xarm.XArmAPI), adapted from xarm-developer/xarm-python-sdk. It reads `joint_positions`, `tcp_pose`, `state`, `mode` and 2 more; runs `move_joints`, `move_pose`, `jog_joints` and `enable_motion`. `move_joints`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/xarm-developer__xarm-python-sdk
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/xarm-developer__xarm-python-sdk --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "xarm-python-sdk": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/xarm-developer__xarm-python-sdk",
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

- **Reads:** `joint_positions`, `tcp_pose`, `state`, `mode`, `error_code`, `warn_code`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_joints` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |
| `move_pose` | Move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. |
| `jog_joints` | Command continuous joint velocities for a bounded duration. The operation stops at the end of the duration or when cancelled. |
| `enable_motion` | Re-enable the arm after a safety reset (the declared re-enable): clean_error, clean_warn, motion_enable(True), set_mode(0) and set_state(0), the recovery the SDK documents after an error; it takes no input, is refused while the e-stop is latched and is never run by the reset |

## Source and status

- Upstream: [xarm-developer/xarm-python-sdk](https://github.com/xarm-developer/xarm-python-sdk) at `d911319cebc4` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/xarm-developer__xarm-python-sdk` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/xarm-developer__xarm-python-sdk`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/xarm-developer__xarm-python-sdk) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/xarm-developer__xarm-python-sdk/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/xarm-developer__xarm-python-sdk/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
