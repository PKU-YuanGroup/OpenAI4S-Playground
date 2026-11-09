# NEJE laser 2 engraver controller (pyGraver serial protocol)

`labs/beniroquai__opentrons-microscope-platereader` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence MIT

NEJE laser 2 engraver controller (pyGraver serial protocol), adapted from beniroquai/opentrons-microscope-platereader. It reads `carving_progress`; runs `move_xy`, `set_laser`, `pause_carving` and `stop_carving`. `move_xy`: move the engraver head to an absolute XY target (moveXY frame). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/beniroquai__opentrons-microscope-platereader
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/beniroquai__opentrons-microscope-platereader --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "opentrons-microscope-platereader": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/beniroquai__opentrons-microscope-platereader",
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

- **Reads:** `carving_progress`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_xy` | Move the engraver head to an absolute XY target (moveXY frame) |
| `set_laser` | Set the laser power and idle bytes (setPWD frame) |
| `pause_carving` | Pause the current carving job (pauseCarving frame) |
| `stop_carving` | Stop carving with the controller's stop frame (the safe state; the stop command takes no deceleration input) |

## Source and status

- Upstream: [beniroquai/opentrons-microscope-platereader](https://github.com/beniroquai/opentrons-microscope-platereader) at `867f54163da7` (MIT); fetch it with `python3 scripts/add_device.py labs/beniroquai__opentrons-microscope-platereader` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/beniroquai__opentrons-microscope-platereader`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/beniroquai__opentrons-microscope-platereader) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/beniroquai__opentrons-microscope-platereader/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/beniroquai__opentrons-microscope-platereader/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
