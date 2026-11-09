# K-Bot V2 feet (MuJoCo simulation)

`robots/kscalelabs__kbot` · Simulation · humanoid robots · simulation · risk R0 · licence MIT

K-Bot V2 feet (MuJoCo simulation), adapted from kscalelabs/kbot. It reads `time_ms`, `qpos`, `qvel`, `ctrl` and 4 more; runs `step` and `reset`. `step`: advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/kscalelabs__kbot
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/kscalelabs__kbot --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "kbot": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/kscalelabs__kbot",
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

- Upstream: [kscalelabs/kbot](https://github.com/kscalelabs/kbot) at `76aba70e3372` (MIT); fetch it with `python3 scripts/add_device.py robots/kscalelabs__kbot` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/kscalelabs__kbot`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/kscalelabs__kbot) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/kscalelabs__kbot/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/kscalelabs__kbot/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
