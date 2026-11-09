# LIBERO coffee-table manipulation environment

`robots/huggingface__lerobot-libero` · Simulation · robot manipulation · simulation · risk R0 · licence MIT

LIBERO coffee-table manipulation environment, adapted from huggingface/lerobot-libero. It reads `observation`, `tick`, `seed`, `reward` and 1 more; runs `reset_world` and `step`. `reset_world`: reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/huggingface__lerobot-libero
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/huggingface__lerobot-libero --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "lerobot-libero": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/huggingface__lerobot-libero",
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

- **Reads:** `observation`, `tick`, `seed`, `reward`, `terminated`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `reset_world` | Reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. |
| `step` | Advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. |

## Source and status

- Upstream: [huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero) at `14fd6f022ff6` (MIT); fetch it with `python3 scripts/add_device.py robots/huggingface__lerobot-libero` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/huggingface__lerobot-libero`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/huggingface__lerobot-libero) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/huggingface__lerobot-libero/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/huggingface__lerobot-libero/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
