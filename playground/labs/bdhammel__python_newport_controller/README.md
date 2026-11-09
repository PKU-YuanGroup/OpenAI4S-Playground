# New Focus Picomotor controller (newport.Controller)

`labs/bdhammel__python_newport_controller` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

New Focus Picomotor controller (newport.Controller), adapted from bdhammel/python_newport_controller. It reads `positions`; runs `move_steps` and `stop_motion`. `move_steps`: move one Picomotor channel by a relative number of steps (the native xPRnn command). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/bdhammel__python_newport_controller
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/bdhammel__python_newport_controller --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "python_newport_controller": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/bdhammel__python_newport_controller",
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

- **Reads:** `positions`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_steps` | Move one Picomotor channel by a relative number of steps (the native xPRnn command) |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [bdhammel/python_newport_controller](https://github.com/bdhammel/python_newport_controller) at `1d960070435d` (MIT); fetch it with `python3 scripts/add_device.py labs/bdhammel__python_newport_controller` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/bdhammel__python_newport_controller`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/bdhammel__python_newport_controller) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/bdhammel__python_newport_controller/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/bdhammel__python_newport_controller/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
