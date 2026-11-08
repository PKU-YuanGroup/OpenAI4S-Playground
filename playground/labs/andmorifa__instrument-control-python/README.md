# Red Pitaya SCPI client (redpitaya_client.RedPitayaClient)

`labs/andmorifa__instrument-control-python` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence MIT

Red Pitaya SCPI client (redpitaya_client.RedPitayaClient), adapted from andmorifa/instrument-control-python. It reads `connected`; runs `scpi_query`. `scpi_query`: send one SCPI query through the client and return the response text. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/andmorifa__instrument-control-python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/andmorifa__instrument-control-python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "instrument-control-python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/andmorifa__instrument-control-python",
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

- **Reads:** `connected`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `scpi_query` | Send one SCPI query through the client and return the response text |

## Source and status

- Upstream: [andmorifa/instrument-control-python](https://github.com/andmorifa/instrument-control-python) at `0622a4aee5cf` (MIT); fetch it with `python3 scripts/add_device.py labs/andmorifa__instrument-control-python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/andmorifa__instrument-control-python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/andmorifa__instrument-control-python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/andmorifa__instrument-control-python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/andmorifa__instrument-control-python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
