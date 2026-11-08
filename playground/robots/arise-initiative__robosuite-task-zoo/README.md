# robosuite Task Zoo HammerPlace environment

`robots/arise-initiative__robosuite-task-zoo` · Simulation · robot manipulation · simulation · risk R1 · licence MIT

robosuite Task Zoo HammerPlace environment, adapted from arise-initiative/robosuite-task-zoo. It reads `observation`, `tick`, `episode`, `seed` and 2 more; runs `reset_world` and `step`. `reset_world`: reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/arise-initiative__robosuite-task-zoo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/arise-initiative__robosuite-task-zoo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "robosuite-task-zoo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/arise-initiative__robosuite-task-zoo",
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

- **Reads:** `observation`, `tick`, `episode`, `seed`, `reward`, `terminated`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `reset_world` | Reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. |
| `step` | Advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. |

## Source and status

- Upstream: [arise-initiative/robosuite-task-zoo](https://github.com/arise-initiative/robosuite-task-zoo) at `74eab7f88214` (MIT); fetch it with `python3 scripts/add_device.py robots/arise-initiative__robosuite-task-zoo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/arise-initiative__robosuite-task-zoo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/arise-initiative__robosuite-task-zoo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/arise-initiative__robosuite-task-zoo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/arise-initiative__robosuite-task-zoo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
