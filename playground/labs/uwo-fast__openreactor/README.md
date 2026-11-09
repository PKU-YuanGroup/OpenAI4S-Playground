# openreactor RLHT heater slice (openreactor.rlht.RlhtSlice)

`labs/uwo-fast__openreactor` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence AGPL-3.0

openreactor RLHT heater slice (openreactor.rlht.RlhtSlice), adapted from uwo-fast/openreactor. It reads `state`, `version`, `mode`, `estop` and 2 more; sets `setpoint_1` and `setpoint_2`; runs `stop_heating`. `stop_heating`: put both heater outputs in the safe state (setpoints zero, then open-loop duty zero). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/uwo-fast__openreactor
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/uwo-fast__openreactor --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "openreactor": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/uwo-fast__openreactor",
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

- **Reads:** `state`, `version`, `mode`, `estop`, `temperature_1`, `temperature_2`
- **Sets:** `setpoint_1`, `setpoint_2`

| Action | What it does |
| --- | --- |
| `stop_heating` | Put both heater outputs in the safe state (setpoints zero, then open-loop duty zero) |

## Source and status

- Upstream: [uwo-fast/openreactor](https://github.com/uwo-fast/openreactor) at `ade88dc17e1c` (AGPL-3.0); fetch it with `python3 scripts/add_device.py labs/uwo-fast__openreactor` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/uwo-fast__openreactor`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/uwo-fast__openreactor) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/uwo-fast__openreactor/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/uwo-fast__openreactor/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
