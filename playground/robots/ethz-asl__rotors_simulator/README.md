# RotorS Gazebo MAV simulator

`robots/ethz-asl__rotors_simulator` · Simulation · UAVs · simulation · risk R0 · licence NOASSERTION

RotorS Gazebo MAV simulator, adapted from ethz-asl/rotors_simulator. It reads `read_odometry` and `read_imu`. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/ethz-asl__rotors_simulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/ethz-asl__rotors_simulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "rotors_simulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/ethz-asl__rotors_simulator",
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

- **Reads:** `read_odometry`, `read_imu`
- **Sets:** —

## Source and status

- Upstream: [ethz-asl/rotors_simulator](https://github.com/ethz-asl/rotors_simulator) at `cd813b7a8c37` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/ethz-asl__rotors_simulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/ethz-asl__rotors_simulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/ethz-asl__rotors_simulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/ethz-asl__rotors_simulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/ethz-asl__rotors_simulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
