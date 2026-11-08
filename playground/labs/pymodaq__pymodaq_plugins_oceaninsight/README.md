# Ocean Insight spectrometer (PyMoDAQ Omnidriver plugin)

`labs/pymodaq__pymodaq_plugins_oceaninsight` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Ocean Insight spectrometer (PyMoDAQ Omnidriver plugin), adapted from pymodaq/pymodaq_plugins_oceaninsight. It reads `wavelength_min_nm`, `wavelength_max_nm` and `pixel_count`; sets `integration_time_ms`; runs `measure_intensity`. `measure_intensity`: measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pymodaq__pymodaq_plugins_oceaninsight
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pymodaq__pymodaq_plugins_oceaninsight --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymodaq_plugins_oceaninsight": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pymodaq__pymodaq_plugins_oceaninsight",
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

- **Reads:** `wavelength_min_nm`, `wavelength_max_nm`, `pixel_count`
- **Sets:** `integration_time_ms`

| Action | What it does |
| --- | --- |
| `measure_intensity` | Measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. |

## Source and status

- Upstream: [pymodaq/pymodaq_plugins_oceaninsight](https://github.com/pymodaq/pymodaq_plugins_oceaninsight) at `298f768a2f2c` (MIT); fetch it with `python3 scripts/add_device.py labs/pymodaq__pymodaq_plugins_oceaninsight` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pymodaq__pymodaq_plugins_oceaninsight`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_oceaninsight) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_oceaninsight/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pymodaq__pymodaq_plugins_oceaninsight/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
