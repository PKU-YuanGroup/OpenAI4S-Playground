# OpenLH liquid handler (uArm Swift Pro)

`labs/idc-milab__openlh` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

OpenLH liquid handler (uArm Swift Pro), adapted from idc-milab/openlh. It reads `position_x`, `position_y`, `position_z`, `polar_rotation` and 5 more; sets `base_angle`, `left_angle`, `right_angle`, `hand_angle` and 2 more; runs `move_to_position` and `tool_off`. `move_to_position`: move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/idc-milab__openlh
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/idc-milab__openlh --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "openlh": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/idc-milab__openlh",
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

- **Reads:** `position_x`, `position_y`, `position_z`, `polar_rotation`, `polar_stretch`, `polar_height`, `ultrasonic_distance`, `limit_switch`, `is_moving`
- **Sets:** `base_angle`, `left_angle`, `right_angle`, `hand_angle`, `pump_on`, `gripper_closed`

| Action | What it does |
| --- | --- |
| `move_to_position` | Move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. |
| `tool_off` | Turn the pump and the gripper off; this is the declared safe state because the upstream API has no motion halt |

## Source and status

- Upstream: [idc-milab/openlh](https://github.com/idc-milab/openlh) at `6a7562c61656` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/idc-milab__openlh` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/idc-milab__openlh`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/idc-milab__openlh) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/idc-milab__openlh/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/idc-milab__openlh/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
