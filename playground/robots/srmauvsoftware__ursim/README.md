# URSim underwater-vehicle simulator

`robots/srmauvsoftware__ursim` · Simulation · underwater robotics · simulation · risk R0 · licence Apache-2.0

URSim underwater-vehicle simulator, adapted from srmauvsoftware/ursim. It reads `read_depth`, `read_heading` and `read_imu`. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/srmauvsoftware__ursim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/srmauvsoftware__ursim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ursim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/srmauvsoftware__ursim",
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

- **Reads:** `read_depth`, `read_heading`, `read_imu`
- **Sets:** —

## Source and status

- Upstream: [srmauvsoftware/ursim](https://github.com/srmauvsoftware/ursim) at `feb7d257e61f` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/srmauvsoftware__ursim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/srmauvsoftware__ursim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/srmauvsoftware__ursim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/srmauvsoftware__ursim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/srmauvsoftware__ursim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
