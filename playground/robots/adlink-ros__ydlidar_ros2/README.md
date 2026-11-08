# YDLIDAR ROS 2 laser scanner

`robots/adlink-ros__ydlidar_ros2` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence NOASSERTION

YDLIDAR ROS 2 laser scanner, adapted from adlink-ros/ydlidar_ros2. It reads `read_scan`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/adlink-ros__ydlidar_ros2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/adlink-ros__ydlidar_ros2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ydlidar_ros2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/adlink-ros__ydlidar_ros2",
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

- **Reads:** `read_scan`
- **Sets:** —

## Source and status

- Upstream: [adlink-ros/ydlidar_ros2](https://github.com/adlink-ros/ydlidar_ros2) at `482c76acf5c0` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/adlink-ros__ydlidar_ros2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/adlink-ros__ydlidar_ros2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/adlink-ros__ydlidar_ros2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/adlink-ros__ydlidar_ros2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/adlink-ros__ydlidar_ros2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
