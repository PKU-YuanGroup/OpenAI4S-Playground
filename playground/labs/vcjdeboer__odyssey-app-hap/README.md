# LI-COR Odyssey Classic 9120 infrared imager (CGI over HTTP)

`labs/vcjdeboer__odyssey-app-hap` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

LI-COR Odyssey Classic 9120 infrared imager (CGI over HTTP), adapted from vcjdeboer/odyssey-app-hap. It reads `state`, `progress_percent`, `time_remaining`, `current_user` and 2 more; sets `scan_name`, `scan_group`, `resolution`, `quality` and 9 more; runs `control_scan`, `safe_stop` and `capture`. `control_scan`: start, pause, stop or cancel the configured scan through command.pl. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/vcjdeboer__odyssey-app-hap
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/vcjdeboer__odyssey-app-hap --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "odyssey-app-hap": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/vcjdeboer__odyssey-app-hap",
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

- **Reads:** `state`, `progress_percent`, `time_remaining`, `current_user`, `lid_open`, `instrument_info`
- **Sets:** `scan_name`, `scan_group`, `resolution`, `quality`, `intensity_700`, `intensity_800`, `channel_700`, `channel_800`, `origin_x_cm`, `origin_y_cm`, `width_cm`, `height_cm`, `focus_offset_mm`

| Action | What it does |
| --- | --- |
| `control_scan` | Start, pause, stop or cancel the configured scan through command.pl |
| `safe_stop` | Send the status-page Stop and confirm the status page then reports Idle or Stopped |
| `capture` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [vcjdeboer/odyssey-app-hap](https://github.com/vcjdeboer/odyssey-app-hap) at `4dffe3a3ed0b` (MIT); fetch it with `python3 scripts/add_device.py labs/vcjdeboer__odyssey-app-hap` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/vcjdeboer__odyssey-app-hap`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/vcjdeboer__odyssey-app-hap) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/vcjdeboer__odyssey-app-hap/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/vcjdeboer__odyssey-app-hap/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
