# OpenFlexure Motor Board stage

`labs/rwb27__openflexure_nano_motor_controller` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

OpenFlexure Motor Board stage, adapted from rwb27/openflexure_nano_motor_controller. It reads `firmware`, `position`, `step_time`, `ramp_time` and 2 more; runs `move_relative`, `move_absolute`, `focus_relative`, `home` and 1 more. `move_relative`: move the stage by a relative displacement in integer motor steps. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/rwb27__openflexure_nano_motor_controller
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/rwb27__openflexure_nano_motor_controller --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "openflexure_nano_motor_controller": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/rwb27__openflexure_nano_motor_controller",
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

- **Reads:** `firmware`, `position`, `step_time`, `ramp_time`, `endstop_status`, `endstop_maxima`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_relative` | Move the stage by a relative displacement in integer motor steps |
| `move_absolute` | Move the stage to an absolute position in integer motor steps |
| `focus_relative` | Move the focus axis (Z) by a relative displacement in integer motor steps |
| `home` | Home the selected axes to their minimum, maximum or both endstops |
| `release_motors` | De-energise the stepper motor coils with the firmware release command |

## Source and status

- Upstream: [rwb27/openflexure_nano_motor_controller](https://github.com/rwb27/openflexure_nano_motor_controller) at `18a19977dde0` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/rwb27__openflexure_nano_motor_controller` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/rwb27__openflexure_nano_motor_controller`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/rwb27__openflexure_nano_motor_controller) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/rwb27__openflexure_nano_motor_controller/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/rwb27__openflexure_nano_motor_controller/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
