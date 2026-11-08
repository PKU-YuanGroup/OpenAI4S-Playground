# LIBERO OffScreenRenderEnv tabletop manipulation

`robots/lifelong-robot-learning__libero` · Simulation · robot manipulation · simulation · risk R0 · licence MIT

LIBERO OffScreenRenderEnv tabletop manipulation, adapted from lifelong-robot-learning/libero. It reads `observation`, `reward`, `terminated`, `truncated` and 3 more; runs `reset` and `step`. `reset`: reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/lifelong-robot-learning__libero
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/lifelong-robot-learning__libero --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "libero": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/lifelong-robot-learning__libero",
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

- **Reads:** `observation`, `reward`, `terminated`, `truncated`, `tick`, `episode`, `seed`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `reset` | Reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. |
| `step` | Advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. |

## Source and status

- Upstream: [lifelong-robot-learning/libero](https://github.com/lifelong-robot-learning/libero) at `8f1084e3132a` (MIT); fetch it with `python3 scripts/add_device.py robots/lifelong-robot-learning__libero` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/lifelong-robot-learning__libero`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/lifelong-robot-learning__libero) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/lifelong-robot-learning__libero/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/lifelong-robot-learning__libero/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
