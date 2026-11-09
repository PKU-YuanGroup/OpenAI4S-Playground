# Cobolt laser (microscope.lights.cobolt:CoboltLaser)

`labs/python-microscope__microscope` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

Cobolt laser (microscope.lights.cobolt:CoboltLaser), adapted from python-microscope/microscope. It reads `is_on`, `enabled`, `measured_power` and `status`; sets `power`; runs `enable_emission` and `disable_emission`. `enable_emission`: switch the laser emission on (the native enable). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/python-microscope__microscope
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/python-microscope__microscope --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "microscope": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/python-microscope__microscope",
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

- **Reads:** `is_on`, `enabled`, `measured_power`, `status`
- **Sets:** `power`

| Action | What it does |
| --- | --- |
| `enable_emission` | Switch the laser emission on (the native enable) |
| `disable_emission` | Switch the laser emission off (the native disable, the safe state); it takes no input |

## Source and status

- Upstream: [python-microscope/microscope](https://github.com/python-microscope/microscope) at `47c13d0342dc` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/python-microscope__microscope` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/python-microscope__microscope`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/python-microscope__microscope) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/python-microscope__microscope/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/python-microscope__microscope/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
