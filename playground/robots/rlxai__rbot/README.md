# rbot simulated 2-D LiDAR

`robots/rlxai__rbot` · Sensors and cameras · simulation · risk R0 · licence Apache-2.0

rbot simulated 2-D LiDAR, adapted from rlxai/rbot. It reads `read_scan`. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/rlxai__rbot
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/rlxai__rbot --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "rbot": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/rlxai__rbot",
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

- **Reads:** `read_scan`
- **Sets:** —

## Source and status

- Upstream: [rlxai/rbot](https://github.com/rlxai/rbot) at `47af3fc3780b` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/rlxai__rbot` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/rlxai__rbot`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/rlxai__rbot) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/rlxai__rbot/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/rlxai__rbot/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
