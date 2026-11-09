# Digimess PN300 power supply

`labs/akperuht__pydaq` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Digimess PN300 power supply, adapted from akperuht/pydaq. It reads `protection`, `measured_voltage` and `measured_current`; sets `output`, `source`, `operating_mode`, `source_type` and 2 more; runs `output_off`. `output_off`: disable the power supply output (the declared safe state). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/akperuht__pydaq
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/akperuht__pydaq --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pydaq": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/akperuht__pydaq",
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

- **Reads:** `protection`, `measured_voltage`, `measured_current`
- **Sets:** `output`, `source`, `operating_mode`, `source_type`, `voltage`, `current`

| Action | What it does |
| --- | --- |
| `output_off` | Disable the power supply output (the declared safe state) |

## Source and status

- Upstream: [akperuht/pydaq](https://github.com/akperuht/pydaq) at `edb7584d0089` (MIT); fetch it with `python3 scripts/add_device.py labs/akperuht__pydaq` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/akperuht__pydaq`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/akperuht__pydaq) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/akperuht__pydaq/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/akperuht__pydaq/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
