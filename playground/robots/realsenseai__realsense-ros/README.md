# RealSense ROS 2 camera

`robots/realsenseai__realsense-ros` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

RealSense ROS 2 camera, adapted from realsenseai/realsense-ros. It reads `frame_id`, `width`, `height`, `device_name` and 9 more; runs `capture_image` and `capture_point_cloud`. `capture_image`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/realsenseai__realsense-ros
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/realsenseai__realsense-ros --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "realsense-ros": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/realsenseai__realsense-ros",
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

- **Reads:** `frame_id`, `width`, `height`, `device_name`, `serial_number`, `firmware_version`, `read_camera_info`, `read_device_info`, `read_frame_metadata`, `read_color_camera_info`, `read_depth_camera_info`, `read_color_metadata`, `read_depth_metadata`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `capture_image` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |
| `capture_point_cloud` | Capture a depth point cloud over a declared range and return a point-cloud artifact reference with the point count and coordinate frame. |

## Source and status

- Upstream: [realsenseai/realsense-ros](https://github.com/realsenseai/realsense-ros) at `7a87097c499e` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/realsenseai__realsense-ros` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/realsenseai__realsense-ros`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/realsenseai__realsense-ros) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/realsenseai__realsense-ros/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/realsenseai__realsense-ros/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
