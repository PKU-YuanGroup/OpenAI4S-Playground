# Ouster OS-x lidar ROS 2 driver

`robots/stevemacenski__ros2_ouster_drivers` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

Ouster OS-x lidar ROS 2 driver, adapted from stevemacenski/ros2_ouster_drivers. It runs `capture_point_cloud`. `capture_point_cloud`: capture a depth point cloud over a declared range and return a point-cloud artifact reference with the point count and coordinate frame. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/stevemacenski__ros2_ouster_drivers
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/stevemacenski__ros2_ouster_drivers --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros2_ouster_drivers": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/stevemacenski__ros2_ouster_drivers",
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
| `capture_point_cloud` | Capture a depth point cloud over a declared range and return a point-cloud artifact reference with the point count and coordinate frame. |

## Source and status

- Upstream: [stevemacenski/ros2_ouster_drivers](https://github.com/stevemacenski/ros2_ouster_drivers) at `19c2523025e3` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/stevemacenski__ros2_ouster_drivers` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/stevemacenski__ros2_ouster_drivers`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/stevemacenski__ros2_ouster_drivers) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/stevemacenski__ros2_ouster_drivers/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/stevemacenski__ros2_ouster_drivers/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
