# TrackIMU ROS 2 IMU

`robots/klintan__ros2_track_imu` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence MIT

TrackIMU ROS 2 IMU, adapted from klintan/ros2_track_imu. It runs `read_imu`. `read_imu`: read linear acceleration, angular velocity and orientation from an inertial measurement unit, with the declared reference frame and timestamp. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/klintan__ros2_track_imu
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/klintan__ros2_track_imu --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros2_track_imu": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/klintan__ros2_track_imu",
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

- **Reads:** —
- **Sets:** —

| Action | What it does |
| --- | --- |
| `read_imu` | Read linear acceleration, angular velocity and orientation from an inertial measurement unit, with the declared reference frame and timestamp. |

## Source and status

- Upstream: [klintan/ros2_track_imu](https://github.com/klintan/ros2_track_imu) at `21741c413cee` (MIT); fetch it with `python3 scripts/add_device.py robots/klintan__ros2_track_imu` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/klintan__ros2_track_imu`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/klintan__ros2_track_imu) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/klintan__ros2_track_imu/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/klintan__ros2_track_imu/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
