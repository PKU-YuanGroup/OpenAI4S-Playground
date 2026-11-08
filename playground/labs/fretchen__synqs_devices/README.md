# Andor Solis camera (synqs_devices)

`labs/fretchen__synqs_devices` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Andor Solis camera (synqs_devices), adapted from fretchen/synqs_devices. It reads `frame_width`, `frame_height`, `x_binning`, `y_binning` and 2 more; sets `exposure_time`, `acquisition_mode`, `trigger_mode`, `trigger_edge` and 2 more; runs `snap`. `snap`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/fretchen__synqs_devices
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/fretchen__synqs_devices --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "synqs_devices": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/fretchen__synqs_devices",
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

- **Reads:** `frame_width`, `frame_height`, `x_binning`, `y_binning`, `accumulations`, `kinetics`
- **Sets:** `exposure_time`, `acquisition_mode`, `trigger_mode`, `trigger_edge`, `cooldown`, `temperature_setpoint`

| Action | What it does |
| --- | --- |
| `snap` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [fretchen/synqs_devices](https://github.com/fretchen/synqs_devices) at `ec4bb24639e9` (MIT); fetch it with `python3 scripts/add_device.py labs/fretchen__synqs_devices` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/fretchen__synqs_devices`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/fretchen__synqs_devices) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/fretchen__synqs_devices/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/fretchen__synqs_devices/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
