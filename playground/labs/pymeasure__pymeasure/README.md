# Keithley DMM6500 multimeter

`labs/pymeasure__pymeasure` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Keithley DMM6500 multimeter, adapted from pymeasure/pymeasure. It reads `mode`, `digits`, `measure_voltage` and `measure_resistance`; sets `nplc`; runs `measure_current`. `measure_current`: measure current on a declared channel and return the value with its timestamp and range. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pymeasure__pymeasure
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pymeasure__pymeasure --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymeasure": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pymeasure__pymeasure",
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

- **Reads:** `mode`, `digits`, `measure_voltage`, `measure_resistance`
- **Sets:** `nplc`

| Action | What it does |
| --- | --- |
| `measure_current` | Measure current on a declared channel and return the value with its timestamp and range. |

## Source and status

- Upstream: [pymeasure/pymeasure](https://github.com/pymeasure/pymeasure) at `9c6a96014e74` (MIT); fetch it with `python3 scripts/add_device.py labs/pymeasure__pymeasure` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pymeasure__pymeasure`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pymeasure__pymeasure) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pymeasure__pymeasure/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pymeasure__pymeasure/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
