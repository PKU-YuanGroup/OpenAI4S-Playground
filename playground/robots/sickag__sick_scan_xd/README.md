# SICK sick_scan_xd LaserScan sensor

`robots/sickag__sick_scan_xd` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

SICK sick_scan_xd LaserScan sensor, adapted from SICKAG/sick_scan_xd. It runs `capture_scan`. `capture_scan`: read one LaserScan sample from the running sick_scan_xd node. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/sickag__sick_scan_xd
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/sickag__sick_scan_xd --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sick_scan_xd": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/sickag__sick_scan_xd",
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

- **Reads:** —
- **Sets:** —

| Action | What it does |
| --- | --- |
| `capture_scan` | Read one LaserScan sample from the running sick_scan_xd node |

## Source and status

- Upstream: [SICKAG/sick_scan_xd](https://github.com/SICKAG/sick_scan_xd) at `ed157563f1fd` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/sickag__sick_scan_xd` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/sickag__sick_scan_xd`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/sickag__sick_scan_xd) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/sickag__sick_scan_xd/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/sickag__sick_scan_xd/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
