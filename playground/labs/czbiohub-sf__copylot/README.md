# Vortran Stradus laser (copylot VortranLaser)

`labs/czbiohub-sf__copylot` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

Vortran Stradus laser (copylot VortranLaser), adapted from czbiohub-sf/copylot. It reads `emission`, `maximum_power`, `fault_code` and `fault_description`; sets `power`, `emission_delay` and `pulse_mode`; runs `emission_on` and `emission_off`. `emission_on`: switch the laser emission on (the upstream turn_on alias, LE=1). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/czbiohub-sf__copylot
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/czbiohub-sf__copylot --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "copylot": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/czbiohub-sf__copylot",
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

- **Reads:** `emission`, `maximum_power`, `fault_code`, `fault_description`
- **Sets:** `power`, `emission_delay`, `pulse_mode`

| Action | What it does |
| --- | --- |
| `emission_on` | Switch the laser emission on (the upstream turn_on alias, LE=1) |
| `emission_off` | Switch the laser emission off (the upstream turn_off alias, LE=0); the safe state |

## Source and status

- Upstream: [czbiohub-sf/copylot](https://github.com/czbiohub-sf/copylot) at `eac4fdbf6ee4` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/czbiohub-sf__copylot` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/czbiohub-sf__copylot`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/czbiohub-sf__copylot) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/czbiohub-sf__copylot/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/czbiohub-sf__copylot/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
