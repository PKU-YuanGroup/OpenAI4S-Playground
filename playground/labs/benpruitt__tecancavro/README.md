# Tecan Cavro XCalibur D syringe pump

`labs/benpruitt__tecancavro` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Tecan Cavro XCalibur D syringe pump, adapted from benpruitt/tecancavro. It reads `plunger_position`, `encoder_position`, `port` and `buffer_status`; sets `start_speed`, `top_speed`, `cutoff_speed`, `microstep` and 2 more; runs `move_plunger`, `dispense` and `stop_pump`. `move_plunger`: move the plunger to an absolute position and execute the queued command. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/benpruitt__tecancavro
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/benpruitt__tecancavro --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tecancavro": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/benpruitt__tecancavro",
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

- **Reads:** `plunger_position`, `encoder_position`, `port`, `buffer_status`
- **Sets:** `start_speed`, `top_speed`, `cutoff_speed`, `microstep`, `speed_code`, `slope`

| Action | What it does |
| --- | --- |
| `move_plunger` | Move the plunger to an absolute position and execute the queued command |
| `dispense` | Select a valve port, dispense a volume from it and execute the queued command |
| `stop_pump` | Terminate the running command and clear the queued command chain |

## Source and status

- Upstream: [benpruitt/tecancavro](https://github.com/benpruitt/tecancavro) at `5267fd2ed48b` (MIT); fetch it with `python3 scripts/add_device.py labs/benpruitt__tecancavro` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/benpruitt__tecancavro`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/benpruitt__tecancavro) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/benpruitt__tecancavro/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/benpruitt__tecancavro/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
