# CHEMYX syringe pump

`labs/cukelarter__chemyx-syringe-pump` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

CHEMYX syringe pump, adapted from cukelarter/chemyx-syringe-pump. It reads `pump_status`, `parameters`, `parameter_limits`, `displaced_volume` and 1 more; sets `units`, `diameter`, `rate`, `volume` and 2 more; runs `start_run`, `pause_run`, `restart_run` and `stop_run`. `start_run`: start the configured run (start). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/cukelarter__chemyx-syringe-pump
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/cukelarter__chemyx-syringe-pump --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "chemyx-syringe-pump": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/cukelarter__chemyx-syringe-pump",
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

- **Reads:** `pump_status`, `parameters`, `parameter_limits`, `displaced_volume`, `elapsed_time`
- **Sets:** `units`, `diameter`, `rate`, `volume`, `delay`, `time`

| Action | What it does |
| --- | --- |
| `start_run` | Start the configured run (start) |
| `pause_run` | Pause the current run (pause) |
| `restart_run` | Restart the pump (restart) |
| `stop_run` | Stop the pump (stop), the safe state |

## Source and status

- Upstream: [cukelarter/chemyx-syringe-pump](https://github.com/cukelarter/chemyx-syringe-pump) at `14011ba2aeb2` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/cukelarter__chemyx-syringe-pump` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/cukelarter__chemyx-syringe-pump`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/cukelarter__chemyx-syringe-pump) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/cukelarter__chemyx-syringe-pump/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/cukelarter__chemyx-syringe-pump/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
