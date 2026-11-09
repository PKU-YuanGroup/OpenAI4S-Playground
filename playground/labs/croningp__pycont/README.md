# Tricontinent C3000 syringe pump (pycont.C3000Controller)

`labs/croningp__pycont` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

Tricontinent C3000 syringe pump (pycont.C3000Controller), adapted from croningp/pycont. It reads `volume`, `plunger_position`, `top_velocity`, `default_top_velocity` and 2 more; sets `valve_position`; runs `run_pump` and `terminate`. `run_pump`: run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/croningp__pycont
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/croningp__pycont --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pycont": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/croningp__pycont",
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

- **Reads:** `volume`, `plunger_position`, `top_velocity`, `default_top_velocity`, `busy`, `initialized`
- **Sets:** `valve_position`

| Action | What it does |
| --- | --- |
| `run_pump` | Run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. |
| `terminate` | Stop the current pump or valve movement with the native terminate command |

## Source and status

- Upstream: [croningp/pycont](https://github.com/croningp/pycont) at `3f6dacb2a6ee` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/croningp__pycont` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/croningp__pycont`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/croningp__pycont) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/croningp__pycont/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/croningp__pycont/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
