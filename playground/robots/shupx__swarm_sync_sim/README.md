# swarm_sync_sim lock-step simulation clock

`robots/shupx__swarm_sync_sim` · Simulation · multi-robot systems · simulation · risk R0 · licence BSD-3-Clause

swarm_sync_sim lock-step simulation clock, adapted from shupx/swarm_sync_sim. It reads `read_sim_clock` and `read_clock_online`; runs `pause` and `resume`. `pause`: pause the simulation clock with /sss_clock_control; /clock holds after at most the regulator's pending 0.01 s step until a client resumes it. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/shupx__swarm_sync_sim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/shupx__swarm_sync_sim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "swarm_sync_sim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/shupx__swarm_sync_sim",
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

- **Reads:** `read_sim_clock`, `read_clock_online`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `pause` | Pause the simulation clock with /sss_clock_control; /clock holds after at most the regulator's pending 0.01 s step until a client resumes it |
| `resume` | Resume clock advancement at an operator-selected speed ratio |

## Source and status

- Upstream: [shupx/swarm_sync_sim](https://github.com/shupx/swarm_sync_sim) at `4837b511c3d2` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/shupx__swarm_sync_sim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/shupx__swarm_sync_sim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/shupx__swarm_sync_sim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/shupx__swarm_sync_sim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/shupx__swarm_sync_sim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
