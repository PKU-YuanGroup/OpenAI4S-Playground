# Wasatch Photonics FID spectrometer (wasatch.FeatureIdentificationDevice)

`labs/wasatchphotonics__wasatch.py` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Wasatch Photonics FID spectrometer (wasatch.FeatureIdentificationDevice), adapted from wasatchphotonics/wasatch.py. It reads `detector_temperature_degC`, `detector_tec_setpoint_degC`, `tec_enabled`, `ambient_temperature_degC` and 1 more; sets `integration_time_ms`; runs `acquire_spectrum` and `laser_off`. `acquire_spectrum`: acquire one spectrum with the current integration time. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/wasatchphotonics__wasatch.py
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/wasatchphotonics__wasatch.py --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "wasatch.py": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/wasatchphotonics__wasatch.py",
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

- **Reads:** `detector_temperature_degC`, `detector_tec_setpoint_degC`, `tec_enabled`, `ambient_temperature_degC`, `laser_enabled`
- **Sets:** `integration_time_ms`

| Action | What it does |
| --- | --- |
| `acquire_spectrum` | Acquire one spectrum with the current integration time |
| `laser_off` | Disable the laser (the safe state); it takes no input |

## Source and status

- Upstream: [wasatchphotonics/wasatch.py](https://github.com/wasatchphotonics/wasatch.py) at `c3ea52bde83d` (MIT); fetch it with `python3 scripts/add_device.py labs/wasatchphotonics__wasatch.py` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/wasatchphotonics__wasatch.py`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/wasatchphotonics__wasatch.py) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/wasatchphotonics__wasatch.py/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/wasatchphotonics__wasatch.py/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
