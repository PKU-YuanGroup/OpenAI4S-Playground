# Communication Instrument serial measurement client

`labs/amandavical__comunication-instrument` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Communication Instrument serial measurement client, adapted from amandavical/comunication-instrument. It reads `status`, `type`, `voltage`, `temperature` and 2 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/amandavical__comunication-instrument
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/amandavical__comunication-instrument --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "comunication-instrument": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/amandavical__comunication-instrument",
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

- **Reads:** `status`, `type`, `voltage`, `temperature`, `current`, `read_channels`
- **Sets:** —

## Source and status

- Upstream: [amandavical/comunication-instrument](https://github.com/amandavical/comunication-instrument) at `051c4277fb02` (MIT); fetch it with `python3 scripts/add_device.py labs/amandavical__comunication-instrument` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/amandavical__comunication-instrument`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/amandavical__comunication-instrument) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/amandavical__comunication-instrument/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/amandavical__comunication-instrument/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
