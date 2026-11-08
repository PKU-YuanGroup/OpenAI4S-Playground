# Thorlabs camera (pymodaq_plugins_pylablib_camera DAQ_2DViewer_ThorlabsPLL)

`labs/attolab__pymodaq_plugins_pylablib_camera` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence CECILL-B

Thorlabs camera (pymodaq_plugins_pylablib_camera DAQ_2DViewer_ThorlabsPLL), adapted from attolab/pymodaq_plugins_pylablib_camera. It reads `camera_list`, `camera_info` and `detector_size`; sets `exposure`, `roi_x0`, `roi_x1`, `roi_y0` and 3 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/attolab__pymodaq_plugins_pylablib_camera
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/attolab__pymodaq_plugins_pylablib_camera --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymodaq_plugins_pylablib_camera": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/attolab__pymodaq_plugins_pylablib_camera",
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

- **Reads:** `camera_list`, `camera_info`, `detector_size`
- **Sets:** `exposure`, `roi_x0`, `roi_x1`, `roi_y0`, `roi_y1`, `binning_x`, `binning_y`

## Source and status

- Upstream: [attolab/pymodaq_plugins_pylablib_camera](https://github.com/attolab/pymodaq_plugins_pylablib_camera) at `ff1e71510bc1` (CECILL-B); fetch it with `python3 scripts/add_device.py labs/attolab__pymodaq_plugins_pylablib_camera` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/attolab__pymodaq_plugins_pylablib_camera`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/attolab__pymodaq_plugins_pylablib_camera) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/attolab__pymodaq_plugins_pylablib_camera/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/attolab__pymodaq_plugins_pylablib_camera/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
