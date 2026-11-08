# Siglent SPD3303X programmable power supply

`labs/little-did-i-know__scpi-instrument-control` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Siglent SPD3303X programmable power supply, adapted from little-did-i-know/scpi-instrument-control. It reads `measured_voltage`, `measured_current`, `identity` and `last_error`; sets `voltage`, `current` and `tracking`; runs `identify`, `measure_voltage` and `measure_current`. `identify`: read the instrument identity. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/little-did-i-know__scpi-instrument-control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/little-did-i-know__scpi-instrument-control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "scpi-instrument-control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/little-did-i-know__scpi-instrument-control",
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

- **Reads:** `measured_voltage`, `measured_current`, `identity`, `last_error`
- **Sets:** `voltage`, `current`, `tracking`

| Action | What it does |
| --- | --- |
| `identify` | Read the instrument identity |
| `measure_voltage` | Measure output 1 voltage |
| `measure_current` | Measure output 1 current |

## Source and status

- Upstream: [little-did-i-know/scpi-instrument-control](https://github.com/little-did-i-know/scpi-instrument-control) at `e252a04dd33d` (MIT); fetch it with `python3 scripts/add_device.py labs/little-did-i-know__scpi-instrument-control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/little-did-i-know__scpi-instrument-control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/little-did-i-know__scpi-instrument-control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/little-did-i-know__scpi-instrument-control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/little-did-i-know__scpi-instrument-control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
