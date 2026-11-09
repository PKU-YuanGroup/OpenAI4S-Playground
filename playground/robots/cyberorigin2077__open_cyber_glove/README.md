# OpenCyberGlove data glove (OpenCyberGlove SDK)

`robots/cyberorigin2077__open_cyber_glove` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

OpenCyberGlove data glove (OpenCyberGlove SDK), adapted from cyberorigin2077/open_cyber_glove. It reads `hand`, `acquisition`, `tensile`, `accelerometer` and 5 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/cyberorigin2077__open_cyber_glove
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/cyberorigin2077__open_cyber_glove --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "open_cyber_glove": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/cyberorigin2077__open_cyber_glove",
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

- **Reads:** `hand`, `acquisition`, `tensile`, `accelerometer`, `gyroscope`, `magnetometer`, `temperature`, `packet_timestamp_us`, `read_sensors`
- **Sets:** —

## Source and status

- Upstream: [cyberorigin2077/open_cyber_glove](https://github.com/cyberorigin2077/open_cyber_glove) at `88910bec8433` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/cyberorigin2077__open_cyber_glove` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/cyberorigin2077__open_cyber_glove`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/cyberorigin2077__open_cyber_glove) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/cyberorigin2077__open_cyber_glove/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/cyberorigin2077__open_cyber_glove/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
