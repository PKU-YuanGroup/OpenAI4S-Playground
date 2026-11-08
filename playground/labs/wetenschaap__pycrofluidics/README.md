# Elveflow OB1 pressure controller (pycrofluidics.OB1elve)

`labs/wetenschaap__pycrofluidics` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

Elveflow OB1 pressure controller (pycrofluidics.OB1elve), adapted from wetenschaap/pycrofluidics. It reads `flow_1`, `flow_2`, `flow_3`, `flow_4` and 1 more; sets `pressure_1`, `pressure_2`, `pressure_3` and `pressure_4`; runs `read_pressure`, `read_flow`, `start_remote` and `stop_remote`. `read_pressure`: read the pressure of one OB1 channel and return it in mbar. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/wetenschaap__pycrofluidics
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/wetenschaap__pycrofluidics --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pycrofluidics": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/wetenschaap__pycrofluidics",
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

- **Reads:** `flow_1`, `flow_2`, `flow_3`, `flow_4`, `remote`
- **Sets:** `pressure_1`, `pressure_2`, `pressure_3`, `pressure_4`

| Action | What it does |
| --- | --- |
| `read_pressure` | Read the pressure of one OB1 channel and return it in mbar |
| `read_flow` | Read the flow sensor of one OB1 channel and return it in uL/min |
| `start_remote` | Start the upstream remote control loop, which reads all sensors and regulators |
| `stop_remote` | Stop the remote control loop and command all four pressure channels to 0 mbar (safe state) |

## Source and status

- Upstream: [wetenschaap/pycrofluidics](https://github.com/wetenschaap/pycrofluidics) at `319de9d08c1a` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/wetenschaap__pycrofluidics` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/wetenschaap__pycrofluidics`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/wetenschaap__pycrofluidics) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/wetenschaap__pycrofluidics/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/wetenschaap__pycrofluidics/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
