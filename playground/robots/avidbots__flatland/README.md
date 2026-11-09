# Flatland 2-D simulator

`robots/avidbots__flatland` · Simulation · mobile navigation · simulation · risk R0 · licence BSD-3-Clause

Flatland 2-D simulator, adapted from avidbots/flatland. It reads `read_sim_clock`; runs `pause` and `resume`. `pause`: pause the simulated world with the acknowledged pause service. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/avidbots__flatland
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/avidbots__flatland --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "flatland": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/avidbots__flatland",
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

- **Reads:** `read_sim_clock`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `pause` | Pause the simulated world with the acknowledged pause service |
| `resume` | Resume the simulated world with the acknowledged resume service |

## Source and status

- Upstream: [avidbots/flatland](https://github.com/avidbots/flatland) at `fd636eea6c28` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/avidbots__flatland` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/avidbots__flatland`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/avidbots__flatland) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/avidbots__flatland/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/avidbots__flatland/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
