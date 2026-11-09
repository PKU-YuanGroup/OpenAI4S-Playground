# Opentrons OT-2 liquid handler (ot2_interface.OT2_Driver)

`labs/ad-sdl__ot2_module` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Opentrons OT-2 liquid handler (ot2_interface.OT2_Driver), adapted from ad-sdl/ot2_module. It reads `robot_status`, `runs`, `active_run_id` and `active_run_status`; runs `start_protocol` and `stop_active_run`. `start_protocol`: upload an Opentrons protocol file that the operator overlay allows, create a run and send the robot's play action; the run continues on the robot after this action returns, until it ends or is stopped, and the protocol alone decides what the robot does in it. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ad-sdl__ot2_module
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ad-sdl__ot2_module --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ot2_module": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ad-sdl__ot2_module",
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

- **Reads:** `robot_status`, `runs`, `active_run_id`, `active_run_status`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `start_protocol` | Upload an Opentrons protocol file that the operator overlay allows, create a run and send the robot's play action; the run continues on the robot after this action returns, until it ends or is stopped, and the protocol alone decides what the robot does in it |
| `stop_active_run` | Send the robot's run stop action to every run it lists as running, paused, finishing or in a status the clone does not name, and to a run of this driver whose play may be in flight, and confirm each by a fresh read; it takes no input |

## Source and status

- Upstream: [ad-sdl/ot2_module](https://github.com/ad-sdl/ot2_module) at `39ffdfdb73c3` (MIT); fetch it with `python3 scripts/add_device.py labs/ad-sdl__ot2_module` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ad-sdl__ot2_module`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ad-sdl__ot2_module) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ad-sdl__ot2_module/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ad-sdl__ot2_module/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
