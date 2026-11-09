# Cryo-con 34 temperature controller (PICA Cryocon34Backend)

`labs/prathameshnium__pica-python-instrument-control-and-automation` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Cryo-con 34 temperature controller (PICA Cryocon34Backend), adapted from prathameshnium/pica-python-instrument-control-and-automation. It reads `temperature`, `control_engaged`, `heater_readback`, `ramp_rate` and 11 more; sets `setpoint`, `loop_type`, `loop_source`, `max_power` and 4 more; runs `control_engage` and `control_stop`. `control_engage`: engage every enabled control loop at the configured setpoint (native CONTROL). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/prathameshnium__pica-python-instrument-control-and-automation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/prathameshnium__pica-python-instrument-control-and-automation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pica-python-instrument-control-and-automation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/prathameshnium__pica-python-instrument-control-and-automation",
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

- **Reads:** `temperature`, `control_engaged`, `heater_readback`, `ramp_rate`, `input_units`, `source_units`, `input_name`, `alarm_status`, `alarm`, `ambient`, `idn`, `error_queue`, `display_resolution`, `lockout`, `factory_sensor_index`
- **Sets:** `setpoint`, `loop_type`, `loop_source`, `max_power`, `max_setpoint`, `manual_power`, `display_time_constant`, `load`

| Action | What it does |
| --- | --- |
| `control_engage` | Engage every enabled control loop at the configured setpoint (native CONTROL) |
| `control_stop` | Disengage all control loops and disconnect the heaters (native STOP), the safe state |

## Source and status

- Upstream: [prathameshnium/pica-python-instrument-control-and-automation](https://github.com/prathameshnium/pica-python-instrument-control-and-automation) at `17ce57d76e67` (MIT); fetch it with `python3 scripts/add_device.py labs/prathameshnium__pica-python-instrument-control-and-automation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/prathameshnium__pica-python-instrument-control-and-automation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/prathameshnium__pica-python-instrument-control-and-automation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/prathameshnium__pica-python-instrument-control-and-automation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/prathameshnium__pica-python-instrument-control-and-automation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
