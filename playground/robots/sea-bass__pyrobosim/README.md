# PyRoboSim world simulator

`robots/sea-bass__pyrobosim` · Simulation · mobile robots · simulation · risk R1 · licence MIT

PyRoboSim world simulator, adapted from sea-bass/pyrobosim. It reads `world_state`; sets `inflation_radius`; runs `reset_world`, `open_location` and `close_location`. `reset_world`: reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/sea-bass__pyrobosim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/sea-bass__pyrobosim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pyrobosim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/sea-bass__pyrobosim",
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

- **Reads:** `world_state`
- **Sets:** `inflation_radius`

| Action | What it does |
| --- | --- |
| `reset_world` | Reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. |
| `open_location` | Open a storage location or hallway in the simulated world |
| `close_location` | Close a storage location or hallway in the simulated world |

## Source and status

- Upstream: [sea-bass/pyrobosim](https://github.com/sea-bass/pyrobosim) at `d33280a4de8f` (MIT); fetch it with `python3 scripts/add_device.py robots/sea-bass__pyrobosim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/sea-bass__pyrobosim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/sea-bass__pyrobosim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/sea-bass__pyrobosim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/sea-bass__pyrobosim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
