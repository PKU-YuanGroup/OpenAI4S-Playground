# ALBA EM2 four-channel electrometer

`labs/maxiv-kitscontrols__sardana-albaem` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

ALBA EM2 four-channel electrometer, adapted from maxiv-kitscontrols/sardana-albaem. It reads `identity`, `acquisition_state`, `nb_points_ready`, `current_ch1` and 11 more; sets `acquisition_mode`, `integration_time`, `nb_points`, `trigger_mode` and 5 more; runs `measure_current`, `configure_channel`, `start_acquisition`, `software_trigger` and 1 more. `measure_current`: measure current on a declared channel and return the value with its timestamp and range. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/maxiv-kitscontrols__sardana-albaem
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/maxiv-kitscontrols__sardana-albaem --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sardana-albaem": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/maxiv-kitscontrols__sardana-albaem",
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

- **Reads:** `identity`, `acquisition_state`, `nb_points_ready`, `current_ch1`, `current_ch2`, `current_ch3`, `current_ch4`, `range_ch1`, `range_ch2`, `range_ch3`, `range_ch4`, `inversion_ch1`, `inversion_ch2`, `inversion_ch3`, `inversion_ch4`
- **Sets:** `acquisition_mode`, `integration_time`, `nb_points`, `trigger_mode`, `trigger_input`, `trigger_polarity`, `trigger_precision`, `trigger_delay`, `timestamp_data`

| Action | What it does |
| --- | --- |
| `measure_current` | Measure current on a declared channel and return the value with its timestamp and range. |
| `configure_channel` | Read or set the amplifier range and digital inversion of one channel |
| `start_acquisition` | Start an acquisition with the current settings |
| `software_trigger` | Send a software trigger to the electrometer |
| `stop_acquisition` | Stop the acquisition and the streaming receiver (the native stop, the safe state) |

## Source and status

- Upstream: [maxiv-kitscontrols/sardana-albaem](https://github.com/maxiv-kitscontrols/sardana-albaem) at `99e701a51017` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/maxiv-kitscontrols__sardana-albaem` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/maxiv-kitscontrols__sardana-albaem`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/maxiv-kitscontrols__sardana-albaem) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/maxiv-kitscontrols__sardana-albaem/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/maxiv-kitscontrols__sardana-albaem/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
