# Sartorius balance via sartoriuslib

`labs/graysonbellamy__sartoriuslib` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Sartorius balance via sartoriuslib, adapted from graysonbellamy/sartoriuslib. It reads `net_weight`, `gross_weight`, `tare_value`, `stable` and 4 more; sets `display_unit`, `filter_mode`, `auto_zero`, `isocal_mode` and 2 more; runs `measure_mass`. `measure_mass`: measure the mass on a balance or load cell and report the value and stability flag. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/graysonbellamy__sartoriuslib
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/graysonbellamy__sartoriuslib --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sartoriuslib": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/graysonbellamy__sartoriuslib",
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

- **Reads:** `net_weight`, `gross_weight`, `tare_value`, `stable`, `status_state`, `model`, `serial`, `software`
- **Sets:** `display_unit`, `filter_mode`, `auto_zero`, `isocal_mode`, `tare_behavior`, `menu_access`

| Action | What it does |
| --- | --- |
| `measure_mass` | Measure the mass on a balance or load cell and report the value and stability flag. |

## Source and status

- Upstream: [graysonbellamy/sartoriuslib](https://github.com/graysonbellamy/sartoriuslib) at `52f520767051` (MIT); fetch it with `python3 scripts/add_device.py labs/graysonbellamy__sartoriuslib` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/graysonbellamy__sartoriuslib`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/graysonbellamy__sartoriuslib) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/graysonbellamy__sartoriuslib/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/graysonbellamy__sartoriuslib/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
