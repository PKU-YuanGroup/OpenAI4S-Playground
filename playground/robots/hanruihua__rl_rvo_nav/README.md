# rl_rvo_nav multi-robot navigation (mrnav-v1)

`robots/hanruihua__rl_rvo_nav` · Simulation · multi-robot systems · simulation · risk R0 · licence MIT

rl_rvo_nav multi-robot navigation (mrnav-v1), adapted from hanruihua/rl_rvo_nav. It reads `observation` and `tick`; runs `step_world` and `reset_world`. `step_world`: advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/hanruihua__rl_rvo_nav
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/hanruihua__rl_rvo_nav --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "rl_rvo_nav": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/hanruihua__rl_rvo_nav",
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

- **Reads:** `observation`, `tick`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `step_world` | Advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. |
| `reset_world` | Reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. |

## Source and status

- Upstream: [hanruihua/rl_rvo_nav](https://github.com/hanruihua/rl_rvo_nav) at `6cdb70c73129` (MIT); fetch it with `python3 scripts/add_device.py robots/hanruihua__rl_rvo_nav` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/hanruihua__rl_rvo_nav`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/hanruihua__rl_rvo_nav) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/hanruihua__rl_rvo_nav/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/hanruihua__rl_rvo_nav/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
