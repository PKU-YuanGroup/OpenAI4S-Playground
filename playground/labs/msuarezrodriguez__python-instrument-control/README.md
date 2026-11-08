# Lake Shore 336 temperature controller (QCoDeS VisaInstrument)

`labs/msuarezrodriguez__python-instrument-control` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Lake Shore 336 temperature controller (QCoDeS VisaInstrument), adapted from msuarezrodriguez/python-instrument-control. It reads `identity`, `temperature` and `sensor_units`; sets `setpoint`, `ramp_rate`, `ramp_enabled`, `heater_range` and 4 more; runs `heaters_off`. `heaters_off`: turn both heater outputs off (RANGE n,0 and OUTMODE n,0,0,0) and read the ranges and modes back; this is the safe-state action. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/msuarezrodriguez__python-instrument-control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/msuarezrodriguez__python-instrument-control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "python-instrument-control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/msuarezrodriguez__python-instrument-control",
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

- **Reads:** `identity`, `temperature`, `sensor_units`
- **Sets:** `setpoint`, `ramp_rate`, `ramp_enabled`, `heater_range`, `output_mode`, `output_input`, `output_powerup_enable`, `manual_output`

| Action | What it does |
| --- | --- |
| `heaters_off` | Turn both heater outputs off (RANGE n,0 and OUTMODE n,0,0,0) and read the ranges and modes back; this is the safe-state action |

## Source and status

- Upstream: [msuarezrodriguez/python-instrument-control](https://github.com/msuarezrodriguez/python-instrument-control) at `e56156e1ba6a` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/msuarezrodriguez__python-instrument-control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/msuarezrodriguez__python-instrument-control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/msuarezrodriguez__python-instrument-control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/msuarezrodriguez__python-instrument-control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/msuarezrodriguez__python-instrument-control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
