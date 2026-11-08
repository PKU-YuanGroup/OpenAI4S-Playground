# ManiSkill-ViTac 2025 Track 1 peg insertion (tactile-vision simulation)

`robots/chuanyune__maniskill-vitac2025` · Simulation · robot arm manipulation · simulation · risk R0 · licence Apache-2.0

ManiSkill-ViTac 2025 Track 1 peg insertion (tactile-vision simulation), adapted from chuanyune/maniskill-vitac2025. It reads `observation`, `reward`, `terminated`, `truncated` and 4 more; runs `step`, `reset` and `seed`. `step`: advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/chuanyune__maniskill-vitac2025
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/chuanyune__maniskill-vitac2025 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "maniskill-vitac2025": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/chuanyune__maniskill-vitac2025",
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

- **Reads:** `observation`, `reward`, `terminated`, `truncated`, `tick`, `episode`, `seed`, `info`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `step` | Advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. |
| `reset` | Reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. |
| `seed` | Set the seed used by the simulated world's random number generators for subsequent steps, without resetting the world. The accepted seed is echoed in the receipt. |

## Source and status

- Upstream: [chuanyune/maniskill-vitac2025](https://github.com/chuanyune/maniskill-vitac2025) at `a3d7df54bca9` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/chuanyune__maniskill-vitac2025` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/chuanyune__maniskill-vitac2025`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/chuanyune__maniskill-vitac2025) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/chuanyune__maniskill-vitac2025/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/chuanyune__maniskill-vitac2025/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
