# Opentrons OT-2 through galago-tools' Ot2Driver

`labs/sciencecorp__galago-tools` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence Apache-2.0

Opentrons OT-2 through galago-tools' Ot2Driver, adapted from sciencecorp/galago-tools. It reads `run_id` and `run_status`; runs `run_protocol` and `stop_run`. `run_protocol`: upload an operator-approved protocol file, create a run of it and play it. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/sciencecorp__galago-tools
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/sciencecorp__galago-tools --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "galago-tools": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/sciencecorp__galago-tools",
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

- **Reads:** `run_id`, `run_status`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `run_protocol` | Upload an operator-approved protocol file, create a run of it and play it |
| `stop_run` | Stop this endpoint's run and read its status until it is succeeded, stopped or failed |

## Source and status

- Upstream: [sciencecorp/galago-tools](https://github.com/sciencecorp/galago-tools) at `7ddf68c7bb7e` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/sciencecorp__galago-tools` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/sciencecorp__galago-tools`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/sciencecorp__galago-tools) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/sciencecorp__galago-tools/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/sciencecorp__galago-tools/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
