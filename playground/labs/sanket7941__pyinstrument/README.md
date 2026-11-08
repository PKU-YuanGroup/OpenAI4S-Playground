# pyinstrument PSupply power supply

`labs/sanket7941__pyinstrument` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence Unlicense

pyinstrument PSupply power supply, adapted from sanket7941/pyinstrument. It reads `voltage`, `current`, `measure_voltage` and `measure_current`; sets `voltage_setpoint`, `current_setpoint` and `output_enabled`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/sanket7941__pyinstrument
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/sanket7941__pyinstrument --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pyinstrument": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/sanket7941__pyinstrument",
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

- **Reads:** `voltage`, `current`, `measure_voltage`, `measure_current`
- **Sets:** `voltage_setpoint`, `current_setpoint`, `output_enabled`

## Source and status

- Upstream: [sanket7941/pyinstrument](https://github.com/sanket7941/pyinstrument) at `74278e53b075` (Unlicense); fetch it with `python3 scripts/add_device.py labs/sanket7941__pyinstrument` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/sanket7941__pyinstrument`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/sanket7941__pyinstrument) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/sanket7941__pyinstrument/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/sanket7941__pyinstrument/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
