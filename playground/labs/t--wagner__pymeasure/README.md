# Keithley 2000 multimeter

`labs/t--wagner__pymeasure` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Keithley 2000 multimeter, adapted from t--wagner/pymeasure. It reads `identification`, `voltage_dc`, `current_dc` and `resistance`; sets `voltage_range`; runs `measure_voltage`, `measure_current` and `measure_resistance`. `measure_voltage`: measure a DC or RMS voltage on a declared channel or terminal pair and return the value with its sampling timestamp and measurement range. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/t--wagner__pymeasure
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/t--wagner__pymeasure --backend fake --port 7400
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
        "labs/t--wagner__pymeasure",
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

- **Reads:** `identification`, `voltage_dc`, `current_dc`, `resistance`
- **Sets:** `voltage_range`

| Action | What it does |
| --- | --- |
| `measure_voltage` | Measure a DC or RMS voltage on a declared channel or terminal pair and return the value with its sampling timestamp and measurement range. |
| `measure_current` | Measure current on a declared channel and return the value with its timestamp and range. |
| `measure_resistance` | Measure resistance or impedance on a declared channel and return the value with its timestamp and excitation method. |

## Source and status

- Upstream: [t--wagner/pymeasure](https://github.com/t--wagner/pymeasure) at `d9c552f3a3fa` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/t--wagner__pymeasure` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/t--wagner__pymeasure`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/t--wagner__pymeasure) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/t--wagner__pymeasure/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/t--wagner__pymeasure/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
