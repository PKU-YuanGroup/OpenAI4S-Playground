# APS storage-ring machine parameters (apstools, read only)

`labs/bcda-aps__apstools` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence BSD-3-Clause

APS storage-ring machine parameters (apstools, read only), adapted from bcda-aps/apstools. It reads `current`, `machine_status`, `operating_mode`, `shutter_status` and 4 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/bcda-aps__apstools
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/bcda-aps__apstools --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "apstools": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/bcda-aps__apstools",
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

- **Reads:** `current`, `machine_status`, `operating_mode`, `shutter_status`, `shutters_open`, `fill_number`, `orbit_correction`, `read_ring_current`
- **Sets:** —

## Source and status

- Upstream: [bcda-aps/apstools](https://github.com/bcda-aps/apstools) at `6250dbaa2f04` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/bcda-aps__apstools` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/bcda-aps__apstools`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/bcda-aps__apstools) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/bcda-aps__apstools/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/bcda-aps__apstools/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
