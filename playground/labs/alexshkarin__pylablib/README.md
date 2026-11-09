# Thorlabs Kinesis motor controller (pylablib KinesisMotor)

`labs/alexshkarin__pylablib` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Thorlabs Kinesis motor controller (pylablib KinesisMotor), adapted from alexshkarin/pylablib. It reads `position`, `moving`, `homed`, `status` and 2 more; sets `max_velocity`; runs `home_axis`, `stop_motion` and `move_to_absolute`. `home_axis`: home the axis with the native MOT_HOME and report the homed bit; it takes no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/alexshkarin__pylablib
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/alexshkarin__pylablib --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pylablib": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/alexshkarin__pylablib",
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

- **Reads:** `position`, `moving`, `homed`, `status`, `controller_model`, `channel_count`
- **Sets:** `max_velocity`

| Action | What it does |
| --- | --- |
| `home_axis` | Home the axis with the native MOT_HOME and report the homed bit; it takes no input |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |
| `move_to_absolute` | Move the axis to an absolute position in device encoder steps and wait until it stops |

## Source and status

- Upstream: [alexshkarin/pylablib](https://github.com/alexshkarin/pylablib) at `96d9504d3e66` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/alexshkarin__pylablib` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/alexshkarin__pylablib`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/alexshkarin__pylablib) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/alexshkarin__pylablib/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/alexshkarin__pylablib/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
