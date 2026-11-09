# GW Instek GPP-4323 DC power supply

`labs/alexlegoshin__idm-dnkmetr` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

GW Instek GPP-4323 DC power supply, adapted from alexlegoshin/idm-dnkmetr. It reads `identity`, `voltage` and `current`; sets `voltage_setpoint` and `current_limit`; runs `enable_output`. `enable_output`: close or open the power-supply output (ALLOUTON/ALLOUTOFF). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/alexlegoshin__idm-dnkmetr
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/alexlegoshin__idm-dnkmetr --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "idm-dnkmetr": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/alexlegoshin__idm-dnkmetr",
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

- **Reads:** `identity`, `voltage`, `current`
- **Sets:** `voltage_setpoint`, `current_limit`

| Action | What it does |
| --- | --- |
| `enable_output` | Close or open the power-supply output (ALLOUTON/ALLOUTOFF) |

## Source and status

- Upstream: [alexlegoshin/idm-dnkmetr](https://github.com/alexlegoshin/idm-dnkmetr) at `8f69873e51d2` (MIT); fetch it with `python3 scripts/add_device.py labs/alexlegoshin__idm-dnkmetr` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/alexlegoshin__idm-dnkmetr`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/alexlegoshin__idm-dnkmetr) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/alexlegoshin__idm-dnkmetr/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/alexlegoshin__idm-dnkmetr/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
