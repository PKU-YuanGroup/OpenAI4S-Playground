# Petoi OpenCat quadruped

`robots/petoicamp__opencat-quadruped-robot` · Mobile robots · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Petoi OpenCat quadruped, adapted from petoicamp/opencat-quadruped-robot. It reads `identity`, `orientation` and `joint_angles_deg`; runs `rest`. `rest`: put the robot down and shut its servos down (the 'd' serial command). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/petoicamp__opencat-quadruped-robot
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/petoicamp__opencat-quadruped-robot --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "opencat-quadruped-robot": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/petoicamp__opencat-quadruped-robot",
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

- **Reads:** `identity`, `orientation`, `joint_angles_deg`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `rest` | Put the robot down and shut its servos down (the 'd' serial command) |

## Source and status

- Upstream: [petoicamp/opencat-quadruped-robot](https://github.com/petoicamp/opencat-quadruped-robot) at `24563ca2e021` (MIT); fetch it with `python3 scripts/add_device.py robots/petoicamp__opencat-quadruped-robot` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/petoicamp__opencat-quadruped-robot`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/petoicamp__opencat-quadruped-robot) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/petoicamp__opencat-quadruped-robot/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/petoicamp__opencat-quadruped-robot/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
