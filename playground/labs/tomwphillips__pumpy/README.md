# Harvard PHD 2000 syringe pump (pumpy.PHD2000)

`labs/tomwphillips__pumpy` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Harvard PHD 2000 syringe pump (pumpy.PHD2000), adapted from tomwphillips/pumpy. It sets `diameter`, `flowrate` and `targetvolume`; runs `pump` and `stop_pump`. `pump`: run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/tomwphillips__pumpy
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/tomwphillips__pumpy --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pumpy": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/tomwphillips__pumpy",
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

- **Reads:** —
- **Sets:** `diameter`, `flowrate`, `targetvolume`

| Action | What it does |
| --- | --- |
| `pump` | Run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. |
| `stop_pump` | Stop the pump with STP (the native stop, the safe state); it takes no input |

## Source and status

- Upstream: [tomwphillips/pumpy](https://github.com/tomwphillips/pumpy) at `3e49d71a73d2` (MIT); fetch it with `python3 scripts/add_device.py labs/tomwphillips__pumpy` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/tomwphillips__pumpy`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/tomwphillips__pumpy) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/tomwphillips__pumpy/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/tomwphillips__pumpy/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
