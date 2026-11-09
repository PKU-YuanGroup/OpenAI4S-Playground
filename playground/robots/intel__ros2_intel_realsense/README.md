# Intel RealSense D400 series camera

`robots/intel__ros2_intel_realsense` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

Intel RealSense D400 series camera, adapted from intel/ros2_intel_realsense. It reads `frame_id`, `width` and `height`; runs `capture_image`. `capture_image`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/intel__ros2_intel_realsense
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/intel__ros2_intel_realsense --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros2_intel_realsense": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/intel__ros2_intel_realsense",
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

- **Reads:** `frame_id`, `width`, `height`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `capture_image` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [intel/ros2_intel_realsense](https://github.com/intel/ros2_intel_realsense) at `74efb28ba4c4` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/intel__ros2_intel_realsense` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/intel__ros2_intel_realsense`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/intel__ros2_intel_realsense) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/intel__ros2_intel_realsense/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/intel__ros2_intel_realsense/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
