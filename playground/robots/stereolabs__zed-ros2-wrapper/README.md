# Stereolabs ZED ROS 2 wrapper

`robots/stereolabs__zed-ros2-wrapper` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

Stereolabs ZED ROS 2 wrapper, adapted from stereolabs/zed-ros2-wrapper. It runs `cap_sensing_image_v1`. `cap_sensing_image_v1`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/stereolabs__zed-ros2-wrapper
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/stereolabs__zed-ros2-wrapper --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "zed-ros2-wrapper": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/stereolabs__zed-ros2-wrapper",
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
| `cap_sensing_image_v1` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [stereolabs/zed-ros2-wrapper](https://github.com/stereolabs/zed-ros2-wrapper) at `b19902daf013` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/stereolabs__zed-ros2-wrapper` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/stereolabs__zed-ros2-wrapper`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/stereolabs__zed-ros2-wrapper) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/stereolabs__zed-ros2-wrapper/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/stereolabs__zed-ros2-wrapper/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
