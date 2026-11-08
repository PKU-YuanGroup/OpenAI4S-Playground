# MRS FlightForge simulator endpoint

`robots/ctu-mrs__mrs_uav_flightforge_simulator` · Simulation · UAVs · simulation · risk R0 · licence GPL-2.0

MRS FlightForge simulator endpoint, adapted from ctu-mrs/mrs_uav_flightforge_simulator. It reads `read_sim_clock` and `read_uav_poses`. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/ctu-mrs__mrs_uav_flightforge_simulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/ctu-mrs__mrs_uav_flightforge_simulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "mrs_uav_flightforge_simulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/ctu-mrs__mrs_uav_flightforge_simulator",
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

- **Reads:** `read_sim_clock`, `read_uav_poses`
- **Sets:** —

## Source and status

- Upstream: [ctu-mrs/mrs_uav_flightforge_simulator](https://github.com/ctu-mrs/mrs_uav_flightforge_simulator) at `e4715a8c75aa` (GPL-2.0); fetch it with `python3 scripts/add_device.py robots/ctu-mrs__mrs_uav_flightforge_simulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/ctu-mrs__mrs_uav_flightforge_simulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/ctu-mrs__mrs_uav_flightforge_simulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/ctu-mrs__mrs_uav_flightforge_simulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/ctu-mrs__mrs_uav_flightforge_simulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
