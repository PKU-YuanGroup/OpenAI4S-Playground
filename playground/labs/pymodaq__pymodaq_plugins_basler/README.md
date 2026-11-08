# Basler camera (pymodaq_plugins_basler.hardware.basler:BaslerCamera)

`labs/pymodaq__pymodaq_plugins_basler` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Basler camera (pymodaq_plugins_basler.hardware.basler:BaslerCamera), adapted from pymodaq/pymodaq_plugins_basler. It reads `model_name`, `detector_size`, `exposure_ms`, `gain` and 3 more; sets `roi_x0`, `roi_x1`, `roi_y0`, `roi_y1` and 2 more; runs `start_grabbing`, `stop_grabbing` and `clear_roi`. `start_grabbing`: start continuous acquisition with the camera's current frame rate (the native start_grabbing with None). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pymodaq__pymodaq_plugins_basler
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pymodaq__pymodaq_plugins_basler --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymodaq_plugins_basler": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pymodaq__pymodaq_plugins_basler",
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

- **Reads:** `model_name`, `detector_size`, `exposure_ms`, `gain`, `frame_rate`, `pixel_format`, `grabbing`
- **Sets:** `roi_x0`, `roi_x1`, `roi_y0`, `roi_y1`, `binning_x`, `binning_y`

| Action | What it does |
| --- | --- |
| `start_grabbing` | Start continuous acquisition with the camera's current frame rate (the native start_grabbing with None) |
| `stop_grabbing` | Stop continuous acquisition (the native stop, the safe state); it takes no input |
| `clear_roi` | Reset the ROI and binning to the full detector (the native set_roi with binning 1) |

## Source and status

- Upstream: [pymodaq/pymodaq_plugins_basler](https://github.com/pymodaq/pymodaq_plugins_basler) at `2bb80b0f2f1f` (MIT); fetch it with `python3 scripts/add_device.py labs/pymodaq__pymodaq_plugins_basler` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pymodaq__pymodaq_plugins_basler`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_basler) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_basler/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pymodaq__pymodaq_plugins_basler/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
