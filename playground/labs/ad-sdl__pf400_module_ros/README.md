# PF400 arm through ad-sdl pf400_module_ros

`labs/ad-sdl__pf400_module_ros` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

PF400 arm through ad-sdl pf400_module_ros, adapted from ad-sdl/pf400_module_ros. It reads `traj_state`; runs `move_joints` and `halt`. `move_joints`: send mspeed and MoveJ for robot 1. A leading 0 is the client's success code (tcp_driver.py:23), not proof the target was reached. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ad-sdl__pf400_module_ros
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ad-sdl__pf400_module_ros --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pf400_module_ros": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ad-sdl__pf400_module_ros",
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

- **Reads:** `traj_state`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_joints` | Send mspeed and MoveJ for robot 1. A leading 0 is the client's success code (tcp_driver.py:23), not proof the target was reached |
| `halt` | On the status port, select robot 1 and halt. Confirms TrajState 0 or 1 only when every MoveJ this endpoint wrote has been answered, and this halt has read state after that. The reply follows the mailbox wait (Main.gpl:225). RapidDecel does not retire an unanswered command |

## Source and status

- Upstream: [ad-sdl/pf400_module_ros](https://github.com/ad-sdl/pf400_module_ros) at `dad325c4bf86` (MIT); fetch it with `python3 scripts/add_device.py labs/ad-sdl__pf400_module_ros` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ad-sdl__pf400_module_ros`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ad-sdl__pf400_module_ros) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ad-sdl__pf400_module_ros/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ad-sdl__pf400_module_ros/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
