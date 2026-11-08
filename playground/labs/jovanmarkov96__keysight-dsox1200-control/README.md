# Keysight InfiniiVision 1200 X-Series oscilloscope (keysight_dsox1200.DSOX1200)

`labs/jovanmarkov96__keysight-dsox1200-control` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Keysight InfiniiVision 1200 X-Series oscilloscope (keysight_dsox1200.DSOX1200), adapted from jovanmarkov96/keysight-dsox1200-control. It reads `identity`, `channel1_probe_ratio`, `channel1_invert`, `timebase_mode` and 7 more; sets `channel1_display`, `channel1_coupling`, `channel1_scale_v_per_div`, `channel1_offset_v` and 4 more; runs `measure`, `run`, `single`, `autoscale` and 1 more. `measure`: read one scalar automatic measurement from the scope's current measurement source. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/jovanmarkov96__keysight-dsox1200-control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/jovanmarkov96__keysight-dsox1200-control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "keysight-dsox1200-control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/jovanmarkov96__keysight-dsox1200-control",
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

- **Reads:** `identity`, `channel1_probe_ratio`, `channel1_invert`, `timebase_mode`, `timebase_position_s`, `trigger_slope`, `trigger_sweep`, `acquire_count`, `acquire_points`, `sample_rate_hz`, `acquire_complete`
- **Sets:** `channel1_display`, `channel1_coupling`, `channel1_scale_v_per_div`, `channel1_offset_v`, `timebase_scale_s_per_div`, `trigger_source`, `trigger_level_v`, `acquire_type`

| Action | What it does |
| --- | --- |
| `measure` | Read one scalar automatic measurement from the scope's current measurement source |
| `run` | Start continuous acquisitions (:RUN) |
| `single` | Arm one acquisition (:SINGle) |
| `autoscale` | Auto-configure the vertical, timebase and trigger settings (:AUToscale) |
| `stop_acquisition` | Stop acquisitions (:STOP, the safe state); it takes no input |

## Source and status

- Upstream: [jovanmarkov96/keysight-dsox1200-control](https://github.com/jovanmarkov96/keysight-dsox1200-control) at `34ba50a758b9` (MIT); fetch it with `python3 scripts/add_device.py labs/jovanmarkov96__keysight-dsox1200-control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/jovanmarkov96__keysight-dsox1200-control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/jovanmarkov96__keysight-dsox1200-control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/jovanmarkov96__keysight-dsox1200-control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/jovanmarkov96__keysight-dsox1200-control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
