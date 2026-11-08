# Multi-Tube-OD-Reader (my_app.classes.device.Device)

`labs/natlabrockies__multi-tube-od-reader` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

Multi-Tube-OD-Reader (my_app.classes.device.Device), adapted from natlabrockies/multi-tube-od-reader. It reads `serial_number`, `port_positions` and `port_usage`; sets `name`; runs `measure_voltage` and `blink`. `measure_voltage`: measure a DC or RMS voltage on a declared channel or terminal pair and return the value with its sampling timestamp and measurement range. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/natlabrockies__multi-tube-od-reader
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/natlabrockies__multi-tube-od-reader --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "multi-tube-od-reader": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/natlabrockies__multi-tube-od-reader",
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

- **Reads:** `serial_number`, `port_positions`, `port_usage`
- **Sets:** `name`

| Action | What it does |
| --- | --- |
| `measure_voltage` | Measure a DC or RMS voltage on a declared channel or terminal pair and return the value with its sampling timestamp and measurement range. |
| `blink` | Blink the device indicator LED through the native Device.blink sequence |

## Source and status

- Upstream: [natlabrockies/multi-tube-od-reader](https://github.com/natlabrockies/multi-tube-od-reader) at `e3948da8586d` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/natlabrockies__multi-tube-od-reader` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/natlabrockies__multi-tube-od-reader`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/natlabrockies__multi-tube-od-reader) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/natlabrockies__multi-tube-od-reader/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/natlabrockies__multi-tube-od-reader/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
