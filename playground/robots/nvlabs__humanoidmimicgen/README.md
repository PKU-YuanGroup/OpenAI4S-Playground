# Unitree G1 29-DOF loco-manipulation model (MuJoCo)

`robots/nvlabs__humanoidmimicgen` · Simulation · humanoid robots · simulation · risk R0 · licence Apache-2.0

Unitree G1 29-DOF loco-manipulation model (MuJoCo), adapted from nvlabs/humanoidmimicgen. It reads `time_ms`, `qpos`, `qvel`, `ctrl` and 4 more; runs `step` and `reset`. `step`: advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/nvlabs__humanoidmimicgen
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/nvlabs__humanoidmimicgen --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "humanoidmimicgen": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/nvlabs__humanoidmimicgen",
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

- **Reads:** `time_ms`, `qpos`, `qvel`, `ctrl`, `tick`, `timestep_ms`, `seed`, `native_checkpoint`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `step` | Advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. |
| `reset` | Reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. |

## Source and status

- Upstream: [nvlabs/humanoidmimicgen](https://github.com/nvlabs/humanoidmimicgen) at `d82844dcec24` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/nvlabs__humanoidmimicgen` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/nvlabs__humanoidmimicgen`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/nvlabs__humanoidmimicgen) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/nvlabs__humanoidmimicgen/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/nvlabs__humanoidmimicgen/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
