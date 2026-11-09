# Princeton Instruments PICam camera (ScopeFoundryHW.picam)

`labs/scopefoundry__hw_picam` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

Princeton Instruments PICam camera (ScopeFoundryHW.picam), adapted from scopefoundry/hw_picam. It reads `adc_speed`, `sensor_temperature_status` and `readout_stride`; sets `exposure_time`, `roi_x`, `roi_width`, `roi_x_binning` and 3 more; runs `capture`. `capture`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/scopefoundry__hw_picam
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/scopefoundry__hw_picam --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "hw_picam": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/scopefoundry__hw_picam",
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

- **Reads:** `adc_speed`, `sensor_temperature_status`, `readout_stride`
- **Sets:** `exposure_time`, `roi_x`, `roi_width`, `roi_x_binning`, `roi_y`, `roi_height`, `roi_y_binning`

| Action | What it does |
| --- | --- |
| `capture` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [scopefoundry/hw_picam](https://github.com/scopefoundry/hw_picam) at `fab5d61440b3` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/scopefoundry__hw_picam` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/scopefoundry__hw_picam`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/scopefoundry__hw_picam) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/scopefoundry__hw_picam/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/scopefoundry__hw_picam/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
