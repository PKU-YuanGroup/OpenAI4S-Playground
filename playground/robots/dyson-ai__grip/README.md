# Grip PickAndPlaceEnvironment (pybullet)

`robots/dyson-ai__grip` · Simulation · robot arm manipulation · simulation · risk R0 · licence MIT

Grip PickAndPlaceEnvironment (pybullet), adapted from dyson-ai/grip. It reads `observation`, `reward`, `terminated`, `truncated` and 4 more; runs `step`, `reset_world` and `fence`. `step`: advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/dyson-ai__grip
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/dyson-ai__grip --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "grip": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/dyson-ai__grip",
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
| `reset_world` | Reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. |
| `fence` | Fence future environment calls and confirm the non-realtime world is idle |

## Source and status

- Upstream: [dyson-ai/grip](https://github.com/dyson-ai/grip) at `eee9f38f86ac` (MIT); fetch it with `python3 scripts/add_device.py robots/dyson-ai__grip` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/dyson-ai__grip`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/dyson-ai__grip) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/dyson-ai__grip/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/dyson-ai__grip/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
