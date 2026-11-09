# Kinect v2 depth camera (iai_kinect2)

`robots/code-iai__iai_kinect2` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

Kinect v2 depth camera (iai_kinect2), adapted from code-iai/iai_kinect2. It reads `frame_id`, `width` and `height`; runs `capture_image`. `capture_image`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/code-iai__iai_kinect2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/code-iai__iai_kinect2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "iai_kinect2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/code-iai__iai_kinect2",
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

- Upstream: [code-iai/iai_kinect2](https://github.com/code-iai/iai_kinect2) at `0e2c5f63134a` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/code-iai__iai_kinect2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/code-iai__iai_kinect2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/code-iai__iai_kinect2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/code-iai__iai_kinect2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/code-iai__iai_kinect2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
