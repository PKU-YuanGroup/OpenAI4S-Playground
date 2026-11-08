# Crazyflie 2.x (CrazyFlyt DroneController)

`robots/jjshoots__crazyflyt` · Mobile robots · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Crazyflie 2.x (CrazyFlyt DroneController), adapted from jjshoots/crazyflyt. It reads `position_estimate`, `setpoint` and `running`; sets `pos_control`; runs `set_position_setpoint`, `set_velocity_setpoint` and `halt`. `set_position_setpoint`: store an (x, y, z, yaw) setpoint in m and rad, select position control and start the control thread. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/jjshoots__crazyflyt
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/jjshoots__crazyflyt --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "crazyflyt": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/jjshoots__crazyflyt",
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

- **Reads:** `position_estimate`, `setpoint`, `running`
- **Sets:** `pos_control`

| Action | What it does |
| --- | --- |
| `set_position_setpoint` | Store an (x, y, z, yaw) setpoint in m and rad, select position control and start the control thread |
| `set_velocity_setpoint` | Store a (vx, vy, vz, vyaw) world-frame velocity setpoint, select velocity control and start the control thread; the clone states no velocity unit, so vx, vy and vz are dimensionless upstream values |
| `halt` | Stop commanding motion: call the native stop, so the control thread sends the stop setpoint |

## Source and status

- Upstream: [jjshoots/crazyflyt](https://github.com/jjshoots/crazyflyt) at `85d99afa21cb` (MIT); fetch it with `python3 scripts/add_device.py robots/jjshoots__crazyflyt` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/jjshoots__crazyflyt`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/jjshoots__crazyflyt) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/jjshoots__crazyflyt/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/jjshoots__crazyflyt/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
