# BASF pyTEM TEM interface (pyTEM.Interface.Interface)

`labs/basf__pytem` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence MIT

BASF pyTEM TEM interface (pyTEM.Interface.Interface), adapted from basf/pytem. It reads `stage_home`, `beam_blanked`, `screen_position`, `column_valve_position` and 5 more; sets `stage_x`, `stage_y`, `stage_z`, `stage_alpha` and 1 more; runs `reset_stage_position` and `enter_safe_state`. `reset_stage_position`: reset the stage to x=y=z=alpha=beta=0 (the native reset_stage_position). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/basf__pytem
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/basf__pytem --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pytem": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/basf__pytem",
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

- **Reads:** `stage_home`, `beam_blanked`, `screen_position`, `column_valve_position`, `column_vacuum`, `accelerator_vacuum`, `mode`, `projection_mode`, `illumination_mode`
- **Sets:** `stage_x`, `stage_y`, `stage_z`, `stage_alpha`, `stage_beta`

| Action | What it does |
| --- | --- |
| `reset_stage_position` | Reset the stage to x=y=z=alpha=beta=0 (the native reset_stage_position) |
| `enter_safe_state` | Enter the native safe state: close the column valve, blank the beam and insert the screen |

## Source and status

- Upstream: [basf/pytem](https://github.com/basf/pytem) at `d2b280032952` (MIT); fetch it with `python3 scripts/add_device.py labs/basf__pytem` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/basf__pytem`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/basf__pytem) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/basf__pytem/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/basf__pytem/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
