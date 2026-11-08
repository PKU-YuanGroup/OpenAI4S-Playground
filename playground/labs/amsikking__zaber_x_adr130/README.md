# Zaber X-ADR130 XY microscope stage

`labs/amsikking__zaber_x_adr130` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Zaber X-ADR130 XY microscope stage, adapted from amsikking/zaber_x_adr130. It reads `x_mm` and `y_mm`; sets `x_maxspeed` and `y_maxspeed`; runs `move_xy`. `move_xy`: move both axes to absolute positions in millimetres and wait for the move to finish. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/amsikking__zaber_x_adr130
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/amsikking__zaber_x_adr130 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "zaber_x_adr130": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/amsikking__zaber_x_adr130",
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

- **Reads:** `x_mm`, `y_mm`
- **Sets:** `x_maxspeed`, `y_maxspeed`

| Action | What it does |
| --- | --- |
| `move_xy` | Move both axes to absolute positions in millimetres and wait for the move to finish |

## Source and status

- Upstream: [amsikking/zaber_x_adr130](https://github.com/amsikking/zaber_x_adr130) at `7c5926e07929` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/amsikking__zaber_x_adr130` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/amsikking__zaber_x_adr130`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/amsikking__zaber_x_adr130) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/amsikking__zaber_x_adr130/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/amsikking__zaber_x_adr130/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
