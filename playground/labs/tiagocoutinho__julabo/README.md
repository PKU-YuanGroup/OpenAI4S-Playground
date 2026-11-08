# JULABO circulator (julabo.JulaboCF)

`labs/tiagocoutinho__julabo` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence LGPL-3.0

JULABO circulator (julabo.JulaboCF), adapted from tiagocoutinho/julabo. It reads `bath_temperature`, `external_temperature`, `active_set_point_channel`, `running` and 1 more; sets `setpoint`; runs `start_circulation` and `stop_circulation`. `start_circulation`: start the circulator (the native start). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/tiagocoutinho__julabo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/tiagocoutinho__julabo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "julabo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/tiagocoutinho__julabo",
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

- **Reads:** `bath_temperature`, `external_temperature`, `active_set_point_channel`, `running`, `status`
- **Sets:** `setpoint`

| Action | What it does |
| --- | --- |
| `start_circulation` | Start the circulator (the native start) |
| `stop_circulation` | Stop the circulator (the native stop, the safe state); it takes no input |

## Source and status

- Upstream: [tiagocoutinho/julabo](https://github.com/tiagocoutinho/julabo) at `650da2138459` (LGPL-3.0); fetch it with `python3 scripts/add_device.py labs/tiagocoutinho__julabo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/tiagocoutinho__julabo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/tiagocoutinho__julabo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/tiagocoutinho__julabo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/tiagocoutinho__julabo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
