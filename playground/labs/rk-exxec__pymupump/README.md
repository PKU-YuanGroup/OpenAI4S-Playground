# Harvard Apparatus Microliter OEM syringe pump (pymupump.Microliter)

`labs/rk-exxec__pymupump` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

Harvard Apparatus Microliter OEM syringe pump (pymupump.Microliter), adapted from rk-exxec/pymupump. It sets `diameter`, `flowrate` and `targetvolume`; runs `pump` and `stop_pump`. `pump`: run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/rk-exxec__pymupump
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/rk-exxec__pymupump --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymupump": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/rk-exxec__pymupump",
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

- Upstream: [rk-exxec/pymupump](https://github.com/rk-exxec/pymupump) at `2de8fb492bbf` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/rk-exxec__pymupump` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/rk-exxec__pymupump`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/rk-exxec__pymupump) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/rk-exxec__pymupump/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/rk-exxec__pymupump/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
