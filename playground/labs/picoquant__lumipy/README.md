# PicoQuant Luminosa through LumiPy Measurement

`labs/picoquant__lumipy` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

PicoQuant Luminosa through LumiPy Measurement, adapted from picoquant/lumipy. It reads `version`, `analysis_names`, `running`, `elapsed_meas_time` and 16 more; sets `scan_range_left`, `scan_range_top`, `scan_range_width`, `scan_range_height` and 2 more; runs `configure_image_stop`, `configure_point_stop`, `set_ptu_output`, `start_measurement` and 7 more. `configure_image_stop`: configure the image stop conditions (frame count, photon threshold, time). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/picoquant__lumipy
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/picoquant__lumipy --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "lumipy": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/picoquant__lumipy",
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

- **Reads:** `version`, `analysis_names`, `running`, `elapsed_meas_time`, `scan_range_min_x`, `scan_range_max_x`, `scan_range_min_y`, `scan_range_max_y`, `stop_on_num_frames`, `num_frames`, `stop_on_photons_in_brightest_px`, `photons_in_brightest_px`, `img_stop_on_meas_time`, `img_meas_time`, `point_stop_on_photons`, `point_num_photons`, `point_stop_on_meas_time`, `point_meas_time`, `write_ptu_file`, `path_to_ptu`
- **Sets:** `scan_range_left`, `scan_range_top`, `scan_range_width`, `scan_range_height`, `scan_speed`, `image_size`

| Action | What it does |
| --- | --- |
| `configure_image_stop` | Configure the image stop conditions (frame count, photon threshold, time). |
| `configure_point_stop` | Configure the point stop conditions (photon threshold and time). |
| `set_ptu_output` | Enable or disable PTU output during the next scan. |
| `start_measurement` | Start an image, line or point measurement (the native start_meas). |
| `stop_measurement` | Stop the measurement (native stop_meas) and confirm meas_status reads False; safe state. |
| `set_measurement_name` | Set the name of the next measurement (the native set_next_measurement_name). |
| `get_analysis_curve` | Read one live analysis curve and its optional fit arrays. |
| `get_analysis_curve_types` | List the curve types available for one live analysis. |
| `get_analysis_image_types` | List the image types available for one live analysis. |
| `get_analysis_param` | Read one live analysis parameter; its keys depend on the analysis and parameter type. |
| `get_analysis_param_types` | List the parameter types available for one live analysis. |

## Source and status

- Upstream: [picoquant/lumipy](https://github.com/picoquant/lumipy) at `dc0fe266a552` (MIT); fetch it with `python3 scripts/add_device.py labs/picoquant__lumipy` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/picoquant__lumipy`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/picoquant__lumipy) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/picoquant__lumipy/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/picoquant__lumipy/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
