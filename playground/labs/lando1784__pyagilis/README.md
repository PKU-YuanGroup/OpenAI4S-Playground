# Newport Agilis agUC2

`labs/lando1784__pyagilis` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence LGPL-3.0

Newport Agilis agUC2, adapted from lando1784/pyagilis. It reads `x_steps`, `y_steps`, `x_at_limit`, `y_at_limit` and 2 more; runs `jog`, `go_to_zero`, `set_zero` and `stop_motion`. `jog`: jog axis 1 and axis 2 by signed step counts (relative motion). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/lando1784__pyagilis
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/lando1784__pyagilis --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pyagilis": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/lando1784__pyagilis",
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

- **Reads:** `x_steps`, `y_steps`, `x_at_limit`, `y_at_limit`, `x_last_operation`, `y_last_operation`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `jog` | Jog axis 1 and axis 2 by signed step counts (relative motion) |
| `go_to_zero` | Move both axes back to counter zero (the upstream goToZero) |
| `set_zero` | Reset both axis counters to zero without moving (the upstream setZero) |
| `stop_motion` | Stop both axes (the native stop); the device's safe state |

## Source and status

- Upstream: [lando1784/pyagilis](https://github.com/lando1784/pyagilis) at `7d27bd1571aa` (LGPL-3.0); fetch it with `python3 scripts/add_device.py labs/lando1784__pyagilis` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/lando1784__pyagilis`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/lando1784__pyagilis) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/lando1784__pyagilis/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/lando1784__pyagilis/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
