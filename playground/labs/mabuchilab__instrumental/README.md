# Thorlabs DCx (UC480) camera (Instrumental UC480_Camera)

`labs/mabuchilab__instrumental` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Thorlabs DCx (UC480) camera (Instrumental UC480_Camera), adapted from mabuchilab/instrumental. It reads `trigger_mode`, `trigger_level`, `auto_gain`, `auto_framerate` and 9 more; sets `trigger_delay`, `exposure_time`, `gamma` and `auto_exposure`; runs `configure_trigger`, `capture`, `start_live_video`, `stop_live_video` and 1 more. `configure_trigger`: set the camera trigger mode and, for hardware triggering, the edge. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/mabuchilab__instrumental
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/mabuchilab__instrumental --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "instrumental": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/mabuchilab__instrumental",
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

- **Reads:** `trigger_mode`, `trigger_level`, `auto_gain`, `auto_framerate`, `auto_whitebalance`, `auto_sensor_exposure`, `auto_sensor_framerate`, `auto_sensor_gain`, `auto_sensor_whitebalance`, `bytes_per_line`, `width`, `height`, `is_open`
- **Sets:** `trigger_delay`, `exposure_time`, `gamma`, `auto_exposure`

| Action | What it does |
| --- | --- |
| `configure_trigger` | Set the camera trigger mode and, for hardware triggering, the edge |
| `capture` | Capture one finite sequence and report the frame dimensions; the pixel array is not carried |
| `start_live_video` | Start continuous acquisition |
| `stop_live_video` | Stop continuous acquisition |
| `close_camera` | Close the camera and release its image memory (the native safe state); it takes no input |

## Source and status

- Upstream: [mabuchilab/instrumental](https://github.com/mabuchilab/instrumental) at `642728325949` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/mabuchilab__instrumental` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/mabuchilab__instrumental`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/mabuchilab__instrumental) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/mabuchilab__instrumental/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/mabuchilab__instrumental/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
