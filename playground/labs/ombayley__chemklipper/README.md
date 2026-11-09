# ChemKlipper CoreXY gantry (chem_klipper.devices.gantry:Gantry)

`labs/ombayley__chemklipper` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

ChemKlipper CoreXY gantry (chem_klipper.devices.gantry:Gantry), adapted from ombayley/chemklipper. It reads `connected`, `status`, `position` and `target_position`; runs `home_gantry`, `move_cartesian` and `stop_motion`. `home_gantry`: home all gantry axes with the native G28. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ombayley__chemklipper
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ombayley__chemklipper --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "chemklipper": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ombayley__chemklipper",
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

- **Reads:** `connected`, `status`, `position`, `target_position`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `home_gantry` | Home all gantry axes with the native G28 |
| `move_cartesian` | Move the gantry to a Cartesian X/Y/Z point in millimetres |
| `stop_motion` | De-energise the gantry motors (M18), the native safe state |

## Source and status

- Upstream: [ombayley/chemklipper](https://github.com/ombayley/chemklipper) at `e88503106b48` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/ombayley__chemklipper` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ombayley__chemklipper`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ombayley__chemklipper) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ombayley__chemklipper/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ombayley__chemklipper/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
