# MVSim vehicle through MVSim's services

`robots/mrpt__mvsim` · Mobile robots · simulation · risk R2 · licence BSD-3-Clause

MVSim vehicle through MVSim's services, adapted from mrpt/mvsim. It reads `read_pose`; runs `set_twist`. `set_twist`: hand one twist setpoint (vx, wz) to the vehicle's controller through MVSim's set_controller_twist service; the setpoint persists until another command. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/mrpt__mvsim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/mrpt__mvsim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "mvsim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/mrpt__mvsim",
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

- **Reads:** `read_pose`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_twist` | Hand one twist setpoint (vx, wz) to the vehicle's controller through MVSim's set_controller_twist service; the setpoint persists until another command |

## Source and status

- Upstream: [mrpt/mvsim](https://github.com/mrpt/mvsim) at `cfaf9f28f57f` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/mrpt__mvsim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/mrpt__mvsim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/mrpt__mvsim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/mrpt__mvsim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/mrpt__mvsim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
