# RoboCam 3.1 camera (robocam.camera:Camera)

`labs/e-lab-sfsu__robocam3.1` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

RoboCam 3.1 camera (robocam.camera:Camera), adapted from e-lab-sfsu/robocam3.1. It reads `running`, `resolution`, `supported_resolutions`, `capture_lock_timeouts` and 2 more; sets `exposure_us`, `gain`, `ae_enabled`, `hqi` and 3 more; runs `reset_capture_stats`. `reset_capture_stats`: reset the capture failure counters and return the zeroed counts. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/e-lab-sfsu__robocam3.1
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/e-lab-sfsu__robocam3.1 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "robocam3.1": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/e-lab-sfsu__robocam3.1",
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

- **Reads:** `running`, `resolution`, `supported_resolutions`, `capture_lock_timeouts`, `capture_sdk_errors`, `dropped_frames`
- **Sets:** `exposure_us`, `gain`, `ae_enabled`, `hqi`, `usb_bandwidth_percent`, `offset`, `sensor_mode_index`

| Action | What it does |
| --- | --- |
| `reset_capture_stats` | Reset the capture failure counters and return the zeroed counts |

## Source and status

- Upstream: [e-lab-sfsu/robocam3.1](https://github.com/e-lab-sfsu/robocam3.1) at `cc402f32f7b7` (MIT); fetch it with `python3 scripts/add_device.py labs/e-lab-sfsu__robocam3.1` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/e-lab-sfsu__robocam3.1`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/e-lab-sfsu__robocam3.1) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/e-lab-sfsu__robocam3.1/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/e-lab-sfsu__robocam3.1/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
