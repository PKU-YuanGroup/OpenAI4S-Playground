# Keithley 2400 source-measure unit

`labs/baroobob__keithley2400` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence GPL-3.0

Keithley 2400 source-measure unit, adapted from baroobob/keithley2400. It reads `trigger_delay`; sets `voltage` and `output`; runs `measure_current`, `measure_voltage`, `measure_resistance` and `safe_state`. `measure_current`: configure current measurement (CONF:CURR, FORM:ELEM CURR) in source-voltage mode and read one sample with the trigger settings of the clone; the source voltage is not changed. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/baroobob__keithley2400
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/baroobob__keithley2400 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "keithley2400": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/baroobob__keithley2400",
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

- **Reads:** `trigger_delay`
- **Sets:** `voltage`, `output`

| Action | What it does |
| --- | --- |
| `measure_current` | Configure current measurement (CONF:CURR, FORM:ELEM CURR) in source-voltage mode and read one sample with the trigger settings of the clone; the source voltage is not changed |
| `measure_voltage` | Configure voltage measurement (CONF:VOLT, FORM:ELEM VOLT) with the source current set to zero and read one sample with the trigger settings of the clone |
| `measure_resistance` | Configure resistance measurement (CONF:RES, FORM:ELEM RES) and read one sample with the trigger settings of the clone; the source setting is not changed |
| `safe_state` | Disable the source output and set the source voltage and source current to zero |

## Source and status

- Upstream: [baroobob/keithley2400](https://github.com/baroobob/keithley2400) at `6491ff740bbd` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/baroobob__keithley2400` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/baroobob__keithley2400`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/baroobob__keithley2400) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/baroobob__keithley2400/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/baroobob__keithley2400/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
