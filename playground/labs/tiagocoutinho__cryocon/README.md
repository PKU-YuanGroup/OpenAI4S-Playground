# CryoCon temperature controller (cryocon.CryoCon)

`labs/tiagocoutinho__cryocon` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence LGPL-3.0

CryoCon temperature controller (cryocon.CryoCon), adapted from tiagocoutinho/cryocon. It reads `idn`, `name`, `hw_revision`, `fw_revision` and 20 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/tiagocoutinho__cryocon
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/tiagocoutinho__cryocon --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "cryocon": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/tiagocoutinho__cryocon",
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

- **Reads:** `idn`, `name`, `hw_revision`, `fw_revision`, `lockout`, `led`, `display_filter_time`, `date`, `time`, `control`, `channel`, `channel_name`, `temperature`, `temperature_unit`, `minimum`, `maximum`, `alarm`, `loop`, `loop_setpoint`, `loop_source`, `loop_type`, `loop_output_power`, `loop_range`, `measure_temperature`
- **Sets:** —

## Source and status

- Upstream: [tiagocoutinho/cryocon](https://github.com/tiagocoutinho/cryocon) at `a60636963d00` (LGPL-3.0); fetch it with `python3 scripts/add_device.py labs/tiagocoutinho__cryocon` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/tiagocoutinho__cryocon`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/tiagocoutinho__cryocon) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/tiagocoutinho__cryocon/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/tiagocoutinho__cryocon/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
