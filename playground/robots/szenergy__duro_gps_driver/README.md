# Duro Inertial GPS ROS 1 driver

`robots/szenergy__duro_gps_driver` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence BSD-3-Clause

Duro Inertial GPS ROS 1 driver, adapted from szenergy/duro_gps_driver. It reads `read_fix`, `read_imu`, `read_mag`, `read_time_reference` and 5 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/szenergy__duro_gps_driver
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/szenergy__duro_gps_driver --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "duro_gps_driver": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/szenergy__duro_gps_driver",
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

- **Reads:** `read_fix`, `read_imu`, `read_mag`, `read_time_reference`, `read_fix_status`, `read_fix_status_text`, `read_pose`, `read_odometry`, `read_attitude`
- **Sets:** —

## Source and status

- Upstream: [szenergy/duro_gps_driver](https://github.com/szenergy/duro_gps_driver) at `d09c1f33aa07` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/szenergy__duro_gps_driver` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/szenergy__duro_gps_driver`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/szenergy__duro_gps_driver) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/szenergy__duro_gps_driver/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/szenergy__duro_gps_driver/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
