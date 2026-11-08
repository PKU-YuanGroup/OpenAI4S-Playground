# SICK scan2 ROS 2 laser scanner

`robots/nobleo__sick_scan2` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

SICK scan2 ROS 2 laser scanner, adapted from nobleo/sick_scan2. It reads `read_laser_scan`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/nobleo__sick_scan2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/nobleo__sick_scan2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sick_scan2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/nobleo__sick_scan2",
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

- **Reads:** `read_laser_scan`
- **Sets:** —

## Source and status

- Upstream: [nobleo/sick_scan2](https://github.com/nobleo/sick_scan2) at `8e851e7f728e` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/nobleo__sick_scan2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/nobleo__sick_scan2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/nobleo__sick_scan2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/nobleo__sick_scan2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/nobleo__sick_scan2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
