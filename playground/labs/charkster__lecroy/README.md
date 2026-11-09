# LeCroy oscilloscope (lecroy.lecroy)

`labs/charkster__lecroy` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

LeCroy oscilloscope (lecroy.lecroy), adapted from charkster/lecroy. It reads `trigger_source`, `trigger_type`, `analog_channels`, `digital_channels` and 1 more; sets `horizontal_scale`, `trigger_level`, `trigger_horizontal_offset`, `trigger_slope` and 1 more; runs `trigger`, `force`, `reset_instrument`, `measure` and 1 more. `trigger`: configure the edge trigger level, horizontal offset, slope and mode. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/charkster__lecroy
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/charkster__lecroy --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "lecroy": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/charkster__lecroy",
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

- **Reads:** `trigger_source`, `trigger_type`, `analog_channels`, `digital_channels`, `measurement_setup`
- **Sets:** `horizontal_scale`, `trigger_level`, `trigger_horizontal_offset`, `trigger_slope`, `trigger_mode`

| Action | What it does |
| --- | --- |
| `trigger` | Configure the edge trigger level, horizontal offset, slope and mode |
| `force` | Force a trigger event (FORCE_TRIGGER) |
| `reset_instrument` | Reset the instrument to its power-on defaults (*RST) |
| `measure` | Read one numeric measurement result |
| `set_grid` | Set the display grid mode (app.Display.GridMode) |

## Source and status

- Upstream: [charkster/lecroy](https://github.com/charkster/lecroy) at `da08c5168d8c` (MIT); fetch it with `python3 scripts/add_device.py labs/charkster__lecroy` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/charkster__lecroy`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/charkster__lecroy) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/charkster__lecroy/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/charkster__lecroy/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
