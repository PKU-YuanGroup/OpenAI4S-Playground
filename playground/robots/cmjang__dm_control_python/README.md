# DaMiao DM series CAN motor (DM_CAN.MotorControl)

`robots/cmjang__dm_control_python` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

DaMiao DM series CAN motor (DM_CAN.MotorControl), adapted from cmjang/dm_control_python. It reads `joint_position`, `joint_velocity`, `joint_torque` and `control_mode`; sets `enabled`; runs `move_joint` and `jog_joint`. `move_joint`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/cmjang__dm_control_python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/cmjang__dm_control_python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "dm_control_python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/cmjang__dm_control_python",
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

- **Reads:** `joint_position`, `joint_velocity`, `joint_torque`, `control_mode`
- **Sets:** `enabled`

| Action | What it does |
| --- | --- |
| `move_joint` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |
| `jog_joint` | Command continuous joint velocities for a bounded duration. The operation stops at the end of the duration or when cancelled. |

## Source and status

- Upstream: [cmjang/dm_control_python](https://github.com/cmjang/dm_control_python) at `7da93877ba84` (MIT); fetch it with `python3 scripts/add_device.py robots/cmjang__dm_control_python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/cmjang__dm_control_python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/cmjang__dm_control_python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/cmjang__dm_control_python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/cmjang__dm_control_python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
