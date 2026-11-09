# Raspberry Pi hat IOC (caproto EPICS Channel Access)

`labs/danielballan__caproto-rpi` · Other devices · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Raspberry Pi hat IOC (caproto EPICS Channel Access), adapted from danielballan/caproto-rpi. It sets `hat_state`; runs `hat_on` and `all_off`. `hat_on`: drive the hat pins HIGH through the state PV and confirm the state PV reads 1. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/danielballan__caproto-rpi
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/danielballan__caproto-rpi --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "caproto-rpi": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/danielballan__caproto-rpi",
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
- **Sets:** `hat_state`

| Action | What it does |
| --- | --- |
| `hat_on` | Drive the hat pins HIGH through the state PV and confirm the state PV reads 1 |
| `all_off` | Write state 0 (every configured hat pin LOW) and confirm it reads back; the declared stop |

## Source and status

- Upstream: [danielballan/caproto-rpi](https://github.com/danielballan/caproto-rpi) at `3642405070a5` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/danielballan__caproto-rpi` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/danielballan__caproto-rpi`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/danielballan__caproto-rpi) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/danielballan__caproto-rpi/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/danielballan__caproto-rpi/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
