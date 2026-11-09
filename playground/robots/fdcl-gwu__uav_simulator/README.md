# FDCL-GWU UAV Gazebo simulator

`robots/fdcl-gwu__uav_simulator` · Simulation · simulation · risk R2 · licence MIT

FDCL-GWU UAV Gazebo simulator, adapted from fdcl-gwu/uav_simulator. It reads `mode`, `motors_on`, `read_state` and `read_imu`; runs `set_flight_mode` and `motors_off`. `set_flight_mode`: publish one ModeData flight-mode request on /uav/mode; the receipt confirms transmission only, not mode execution, and the publication does not turn the motors on. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/fdcl-gwu__uav_simulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/fdcl-gwu__uav_simulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "uav_simulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/fdcl-gwu__uav_simulator",
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

- **Reads:** `mode`, `motors_on`, `read_state`, `read_imu`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_flight_mode` | Publish one ModeData flight-mode request on /uav/mode; the receipt confirms transmission only, not mode execution, and the publication does not turn the motors on |
| `motors_off` | Publish one std_msgs/Bool false on /uav/motors_on, the same publication the e-stop sends; the receipt confirms transmission only, not the sensed confirmation, and repeating it does not turn the motors on |

## Source and status

- Upstream: [fdcl-gwu/uav_simulator](https://github.com/fdcl-gwu/uav_simulator) at `7270fe4e274f` (MIT); fetch it with `python3 scripts/add_device.py robots/fdcl-gwu__uav_simulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/fdcl-gwu__uav_simulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/fdcl-gwu__uav_simulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/fdcl-gwu__uav_simulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/fdcl-gwu__uav_simulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
