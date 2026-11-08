# FastSwarmSim lock-step time coordinator

`robots/shupx__fastswarmsim` · Simulation · UAVs · simulation · risk R0 · licence BSD-3-Clause

FastSwarmSim lock-step time coordinator, adapted from shupx/fastswarmsim. It reads `clock_running`, `clock_factor`, `read_sim_clock` and `read_clock_status`; runs `pause` and `resume`. `pause`: pause clock advancement with the acknowledged fss/clock_control service. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/shupx__fastswarmsim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/shupx__fastswarmsim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "fastswarmsim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/shupx__fastswarmsim",
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

- **Reads:** `clock_running`, `clock_factor`, `read_sim_clock`, `read_clock_status`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `pause` | Pause clock advancement with the acknowledged fss/clock_control service |
| `resume` | Resume clock advancement at an operator-selected real-time factor |

## Source and status

- Upstream: [shupx/fastswarmsim](https://github.com/shupx/fastswarmsim) at `56a6380fcd40` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/shupx__fastswarmsim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/shupx__fastswarmsim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/shupx__fastswarmsim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/shupx__fastswarmsim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/shupx__fastswarmsim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
