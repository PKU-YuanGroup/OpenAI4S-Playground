# Cetoni Nemesys V4 syringe pump

`labs/bennomeier__cetoni` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Cetoni Nemesys V4 syringe pump, adapted from bennomeier/cetoni. It reads `current_position` and `status`; sets `target_position`, `velocity`, `flow_rate` and `valve_position`; runs `pump` and `stop_pump`. `pump`: run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/bennomeier__cetoni
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/bennomeier__cetoni --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "cetoni": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/bennomeier__cetoni",
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

- **Reads:** `current_position`, `status`
- **Sets:** `target_position`, `velocity`, `flow_rate`, `valve_position`

| Action | What it does |
| --- | --- |
| `pump` | Run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. |
| `stop_pump` | Disable the drive with control word 0x06 (shutdown), the safe state; it takes no input |

## Source and status

- Upstream: [bennomeier/cetoni](https://github.com/bennomeier/cetoni) at `b957067d56c2` (MIT); fetch it with `python3 scripts/add_device.py labs/bennomeier__cetoni` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/bennomeier__cetoni`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/bennomeier__cetoni) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/bennomeier__cetoni/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/bennomeier__cetoni/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
