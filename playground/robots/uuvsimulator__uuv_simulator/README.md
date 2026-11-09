# UUV Simulator underwater current environment

`robots/uuvsimulator__uuv_simulator` · Simulation · marine robotics · simulation · risk R1 · licence Apache-2.0

UUV Simulator underwater current environment, adapted from uuvsimulator/uuv_simulator. It reads `flow_velocity` and `read_current_velocity`; runs `set_current_velocity`, `set_horizontal_angle`, `set_vertical_angle` and `zero_current`. `set_current_velocity`: set the simulated current velocity and direction model means. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/uuvsimulator__uuv_simulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/uuvsimulator__uuv_simulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "uuv_simulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/uuvsimulator__uuv_simulator",
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

- **Reads:** `flow_velocity`, `read_current_velocity`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_current_velocity` | Set the simulated current velocity and direction model means |
| `set_horizontal_angle` | Set the horizontal current-angle model mean |
| `set_vertical_angle` | Set the vertical current-angle model mean |
| `zero_current` | Zero the three current model means through the fixed acknowledged service |

## Source and status

- Upstream: [uuvsimulator/uuv_simulator](https://github.com/uuvsimulator/uuv_simulator) at `bfb40cb15368` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/uuvsimulator__uuv_simulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/uuvsimulator__uuv_simulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/uuvsimulator__uuv_simulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/uuvsimulator__uuv_simulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/uuvsimulator__uuv_simulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
