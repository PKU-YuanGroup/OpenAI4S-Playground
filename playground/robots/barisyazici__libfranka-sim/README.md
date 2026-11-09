# Franka Hand (libfranka-sim)

`robots/barisyazici__libfranka-sim` · Robot arms and grippers · simulation · risk R2 · licence Apache-2.0

Franka Hand (libfranka-sim), adapted from barisyazici/libfranka-sim. It reads `width_mm`, `max_width_mm`, `is_grasped`, `is_stuck` and 1 more; runs `grasp`, `release`, `hand_home`, `hand_move` and 1 more. `grasp`: close the gripper on a target object with a bounded force and report the achieved grasp width. A failed grasp is a completed operation with grasped=false, not a silent success. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/barisyazici__libfranka-sim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/barisyazici__libfranka-sim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "libfranka-sim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/barisyazici__libfranka-sim",
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

- **Reads:** `width_mm`, `max_width_mm`, `is_grasped`, `is_stuck`, `temperature_c`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `grasp` | Close the gripper on a target object with a bounded force and report the achieved grasp width. A failed grasp is a completed operation with grasped=false, not a silent success. |
| `release` | Open the gripper to release the held object, optionally to a declared opening width, and report the achieved width. |
| `hand_home` | Drive the fingers fully open and clear the grasp and stuck state |
| `hand_move` | Drive the fingers to a width and wait until they settle |
| `hand_stop` | Stop the hand by driving the fingers fully open, the simulator's safe state |

## Source and status

- Upstream: [barisyazici/libfranka-sim](https://github.com/barisyazici/libfranka-sim) at `d893e17dc77a` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/barisyazici__libfranka-sim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/barisyazici__libfranka-sim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/barisyazici__libfranka-sim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/barisyazici__libfranka-sim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/barisyazici__libfranka-sim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
