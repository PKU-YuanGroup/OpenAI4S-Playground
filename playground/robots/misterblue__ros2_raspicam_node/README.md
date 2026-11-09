# Raspberry Pi camera JPEG stream (ros2_raspicam_node)

`robots/misterblue__ros2_raspicam_node` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

Raspberry Pi camera JPEG stream (ros2_raspicam_node), adapted from misterblue/ros2_raspicam_node. It runs `capture_image`. `capture_image`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/misterblue__ros2_raspicam_node
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/misterblue__ros2_raspicam_node --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros2_raspicam_node": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/misterblue__ros2_raspicam_node",
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
| `capture_image` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [misterblue/ros2_raspicam_node](https://github.com/misterblue/ros2_raspicam_node) at `cebf5fdacd18` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/misterblue__ros2_raspicam_node` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/misterblue__ros2_raspicam_node`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/misterblue__ros2_raspicam_node) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/misterblue__ros2_raspicam_node/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/misterblue__ros2_raspicam_node/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
