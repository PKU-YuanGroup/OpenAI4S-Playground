# ROS 2 USB camera images and calibration

`robots/klintan__ros2_usb_camera` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

ROS 2 USB camera images and calibration, adapted from klintan/ros2_usb_camera. It reads `frame_id`, `read_camera_calibration` and `read_camera_info`; runs `capture`. `capture`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/klintan__ros2_usb_camera
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/klintan__ros2_usb_camera --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros2_usb_camera": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/klintan__ros2_usb_camera",
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

- **Reads:** `frame_id`, `read_camera_calibration`, `read_camera_info`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `capture` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [klintan/ros2_usb_camera](https://github.com/klintan/ros2_usb_camera) at `146c5911ebcc` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/klintan__ros2_usb_camera` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/klintan__ros2_usb_camera`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/klintan__ros2_usb_camera) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/klintan__ros2_usb_camera/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/klintan__ros2_usb_camera/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
