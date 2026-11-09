# quad_sim indoor quadcopter simulation

`robots/rumaisaabdulhai__quad_sim` · Simulation · UAVs · simulation · risk R1 · licence MIT

quad_sim indoor quadcopter simulation, adapted from rumaisaabdulhai/quad_sim. It reads `read_ground_truth_pose` and `read_goal_status`. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/rumaisaabdulhai__quad_sim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/rumaisaabdulhai__quad_sim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "quad_sim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/rumaisaabdulhai__quad_sim",
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

- **Reads:** `read_ground_truth_pose`, `read_goal_status`
- **Sets:** —

## Source and status

- Upstream: [rumaisaabdulhai/quad_sim](https://github.com/rumaisaabdulhai/quad_sim) at `01d02f6e2fad` (MIT); fetch it with `python3 scripts/add_device.py robots/rumaisaabdulhai__quad_sim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/rumaisaabdulhai__quad_sim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/rumaisaabdulhai__quad_sim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/rumaisaabdulhai__quad_sim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/rumaisaabdulhai__quad_sim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
