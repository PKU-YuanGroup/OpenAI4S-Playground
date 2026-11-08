# Lake Shore Model 332 temperature controller

`labs/daanwielens__research-python` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Lake Shore Model 332 temperature controller, adapted from daanwielens/research-python. It reads `temperature`, `temperature_celsius`, `heater_output` and `pid`; sets `setpoint`, `heater_range` and `manual_output`; runs `set_pid` and `heater_off`. `set_pid`: set the loop-1 proportional, integral and derivative terms. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/daanwielens__research-python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/daanwielens__research-python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "research-python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/daanwielens__research-python",
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

- **Reads:** `temperature`, `temperature_celsius`, `heater_output`, `pid`
- **Sets:** `setpoint`, `heater_range`, `manual_output`

| Action | What it does |
| --- | --- |
| `set_pid` | Set the loop-1 proportional, integral and derivative terms |
| `heater_off` | Set the heater range to 0 (off) as the declared safe state |

## Source and status

- Upstream: [daanwielens/research-python](https://github.com/daanwielens/research-python) at `c17811c9b43b` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/daanwielens__research-python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/daanwielens__research-python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/daanwielens__research-python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/daanwielens__research-python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/daanwielens__research-python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
