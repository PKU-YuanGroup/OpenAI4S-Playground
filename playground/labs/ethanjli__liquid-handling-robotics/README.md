# Liquid-handling robot x-axis (sample stage)

`labs/ethanjli__liquid-handling-robotics` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

Liquid-handling robot x-axis (sample stage), adapted from ethanjli/liquid-handling-robotics. It reads `physical_position` and `sensor_position`; runs `move_by_physical_delta` and `stop_axis`. `move_by_physical_delta`: move the x-axis by a relative physical displacement along its travel. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ethanjli__liquid-handling-robotics
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ethanjli__liquid-handling-robotics --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "liquid-handling-robotics": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ethanjli__liquid-handling-robotics",
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

- **Reads:** `physical_position`, `sensor_position`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_by_physical_delta` | Move the x-axis by a relative physical displacement along its travel |
| `stop_axis` | Brake the x-axis by setting every motor duty limit to zero |

## Source and status

- Upstream: [ethanjli/liquid-handling-robotics](https://github.com/ethanjli/liquid-handling-robotics) at `fc7043558072` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/ethanjli__liquid-handling-robotics` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ethanjli__liquid-handling-robotics`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ethanjli__liquid-handling-robotics) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ethanjli__liquid-handling-robotics/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ethanjli__liquid-handling-robotics/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
