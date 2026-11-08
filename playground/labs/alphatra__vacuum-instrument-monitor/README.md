# Granville-Phillips 350 ion gauge controller

`labs/alphatra__vacuum-instrument-monitor` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Granville-Phillips 350 ion gauge controller, adapted from alphatra/vacuum-instrument-monitor. It reads `pressure`; sets `filament_1`, `filament_2` and `degas`; runs `all_off`. `all_off`: switch both ion-gauge filaments and the degas cycle off. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/alphatra__vacuum-instrument-monitor
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/alphatra__vacuum-instrument-monitor --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "vacuum-instrument-monitor": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/alphatra__vacuum-instrument-monitor",
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

- **Reads:** `pressure`
- **Sets:** `filament_1`, `filament_2`, `degas`

| Action | What it does |
| --- | --- |
| `all_off` | Switch both ion-gauge filaments and the degas cycle off |

## Source and status

- Upstream: [alphatra/vacuum-instrument-monitor](https://github.com/alphatra/vacuum-instrument-monitor) at `838275818a2f` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/alphatra__vacuum-instrument-monitor` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/alphatra__vacuum-instrument-monitor`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/alphatra__vacuum-instrument-monitor) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/alphatra__vacuum-instrument-monitor/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/alphatra__vacuum-instrument-monitor/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
