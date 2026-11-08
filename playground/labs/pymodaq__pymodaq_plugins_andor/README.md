# Andor SDK3 camera (pymodaq_plugins_andor AndorCamera)

`labs/pymodaq__pymodaq_plugins_andor` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Andor SDK3 camera (pymodaq_plugins_andor AndorCamera), adapted from pymodaq/pymodaq_plugins_andor. It reads `sensor_width`, `sensor_height`, `roi_width`, `roi_height` and 8 more; sets `integration_time`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pymodaq__pymodaq_plugins_andor
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pymodaq__pymodaq_plugins_andor --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymodaq_plugins_andor": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pymodaq__pymodaq_plugins_andor",
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

- **Reads:** `sensor_width`, `sensor_height`, `roi_width`, `roi_height`, `serial_number`, `actual_exposure_time`, `sensor_temperature`, `sensor_cooling`, `temperature_status`, `temperature_control`, `frame_rate`, `overlap`
- **Sets:** `integration_time`

## Source and status

- Upstream: [pymodaq/pymodaq_plugins_andor](https://github.com/pymodaq/pymodaq_plugins_andor) at `673a12ae4e9e` (MIT); fetch it with `python3 scripts/add_device.py labs/pymodaq__pymodaq_plugins_andor` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pymodaq__pymodaq_plugins_andor`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_andor) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_andor/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pymodaq__pymodaq_plugins_andor/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
