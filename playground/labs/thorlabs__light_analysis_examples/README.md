# Thorlabs BC207/BC210 beam profiler (TLBC2.py)

`labs/thorlabs__light_analysis_examples` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Thorlabs BC207/BC210 beam profiler (TLBC2.py), adapted from thorlabs/light_analysis_examples. It reads `sensor_pixels_x`, `sensor_pixels_y`, `pixel_pitch_horizontal`, `pixel_pitch_vertical` and 5 more; sets `exposure_time`, `wavelength`, `precision_mode` and `binning`; runs `capture` and `measure_beam`. `capture`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/thorlabs__light_analysis_examples
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/thorlabs__light_analysis_examples --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "light_analysis_examples": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/thorlabs__light_analysis_examples",
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

- **Reads:** `sensor_pixels_x`, `sensor_pixels_y`, `pixel_pitch_horizontal`, `pixel_pitch_vertical`, `roi_left`, `roi_top`, `roi_width`, `roi_height`, `sensor_temperature`
- **Sets:** `exposure_time`, `wavelength`, `precision_mode`, `binning`

| Action | What it does |
| --- | --- |
| `capture` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |
| `measure_beam` | Request a new measurement and return the 4-sigma beam widths, centroid, peak, saturation and total power the instrument calculated |

## Source and status

- Upstream: [thorlabs/light_analysis_examples](https://github.com/thorlabs/light_analysis_examples) at `1e7f3aa6fe29` (MIT); fetch it with `python3 scripts/add_device.py labs/thorlabs__light_analysis_examples` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/thorlabs__light_analysis_examples`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/thorlabs__light_analysis_examples) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/thorlabs__light_analysis_examples/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/thorlabs__light_analysis_examples/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
