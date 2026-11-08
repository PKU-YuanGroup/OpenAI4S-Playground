# Opentrons OT-2 motion controller (OT2MotionController)

`labs/accelerationconsortium__opentrons-ot2` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Opentrons OT-2 motion controller (OT2MotionController), adapted from accelerationconsortium/opentrons-ot2. It reads `simulating`, `position`, `firmware_version`, `serial_number` and 6 more; sets `button_light` and `rail_lights`; runs `cartesian_pose`, `move_axes`, `home_all`, `aspirate` and 3 more. `cartesian_pose`: move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/accelerationconsortium__opentrons-ot2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/accelerationconsortium__opentrons-ot2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "opentrons-ot2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/accelerationconsortium__opentrons-ot2",
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

- **Reads:** `simulating`, `position`, `firmware_version`, `serial_number`, `pipette_left_model`, `pipette_left_id`, `pipette_right_model`, `pipette_right_id`, `button_pressed`, `door_closed`
- **Sets:** `button_light`, `rail_lights`

| Action | What it does |
| --- | --- |
| `cartesian_pose` | Move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. |
| `move_axes` | Move all six OT-2 axes to absolute machine positions in millimetres with the native move(); refused PRECONDITION_UNMET after a halt until the re-enable |
| `home_all` | Home all six OT-2 axes with the native home(); refused PRECONDITION_UNMET after a halt, when the re-enable (which clears the alarm lock and then homes) is the way back |
| `aspirate` | Draw liquid with the native aspirate(axis, volume_ul, ul_per_mm, flow_rate_ul_s); the caller supplies the pipette conversion and the plunger must already be at its bottom; refused PRECONDITION_UNMET after a halt until the re-enable |
| `dispense` | Expel liquid with the native dispense(axis, volume_ul, ul_per_mm, flow_rate_ul_s); the caller supplies the pipette conversion; refused PRECONDITION_UNMET after a halt until the re-enable |
| `halt_motion` | Halt all motion with the native stop() (SmoothieDriver.hard_halt, after the controller lock is free); it takes no input, is the declared safe state, and leaves the driver refusing motion until the re-enable |
| `reenable` | Recovery after a halt (an e-stop, the halt action or a cancelled action): clear the Smoothie alarm lock with reset_from_error() (M999) and re-home all six axes; it takes no input, is refused while latched, and is the only Smoothie command the driver sends after a halt |

## Source and status

- Upstream: [accelerationconsortium/opentrons-ot2](https://github.com/accelerationconsortium/opentrons-ot2) at `9ba663504dcf` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/accelerationconsortium__opentrons-ot2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/accelerationconsortium__opentrons-ot2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/accelerationconsortium__opentrons-ot2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/accelerationconsortium__opentrons-ot2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/accelerationconsortium__opentrons-ot2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
