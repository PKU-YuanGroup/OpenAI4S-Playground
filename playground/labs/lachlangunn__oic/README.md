# OIC Arduino DAQ / meter

`labs/lachlangunn__oic` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

OIC Arduino DAQ / meter, adapted from lachlangunn/oic. It reads `voltage2`; sets `voltage0` and `voltage1`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/lachlangunn__oic
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/lachlangunn__oic --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "oic": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/lachlangunn__oic",
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

- **Reads:** `voltage2`
- **Sets:** `voltage0`, `voltage1`

## Source and status

- Upstream: [lachlangunn/oic](https://github.com/lachlangunn/oic) at `6c7ab800893d` (MIT); fetch it with `python3 scripts/add_device.py labs/lachlangunn__oic` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/lachlangunn__oic`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/lachlangunn__oic) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/lachlangunn__oic/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/lachlangunn__oic/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
