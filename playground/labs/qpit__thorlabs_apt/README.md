# Thorlabs APT motor (thorlabs_apt.Motor)

`labs/qpit__thorlabs_apt` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-2.0

Thorlabs APT motor (thorlabs_apt.Motor), adapted from qpit/thorlabs_apt. It reads `position`, `serial_number`, `in_motion`, `homing_completed` and 9 more; sets `velocity_maximum`, `acceleration`, `reverse_limit_switch`, `forward_limit_switch` and 2 more; runs `move_to`, `move_by`, `move_home`, `move_velocity` and 3 more. `move_to`: move to an absolute position in the native stage units (mm or degrees). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/qpit__thorlabs_apt
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/qpit__thorlabs_apt --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "thorlabs_apt": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/qpit__thorlabs_apt",
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

- **Reads:** `position`, `serial_number`, `in_motion`, `homing_completed`, `settled`, `motion_error`, `enabled`, `forward_limit_active`, `reverse_limit_active`, `active_channel`, `stage_minimum`, `stage_maximum`, `stage_units`
- **Sets:** `velocity_maximum`, `acceleration`, `reverse_limit_switch`, `forward_limit_switch`, `move_home_direction`, `move_home_lim_switch`

| Action | What it does |
| --- | --- |
| `move_to` | Move to an absolute position in the native stage units (mm or degrees) |
| `move_by` | Move by a relative distance in the native stage units (mm or degrees) |
| `move_home` | Home the axis with the native homing move |
| `move_velocity` | Move at constant velocity in the given direction |
| `enable` | Enable the active motor channel |
| `disable` | Disable the active motor channel |
| `stop_profiled` | Stop the motor with the native profiled stop |

## Source and status

- Upstream: [qpit/thorlabs_apt](https://github.com/qpit/thorlabs_apt) at `7b5c84607c22` (GPL-2.0); fetch it with `python3 scripts/add_device.py labs/qpit__thorlabs_apt` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/qpit__thorlabs_apt`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/qpit__thorlabs_apt) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/qpit__thorlabs_apt/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/qpit__thorlabs_apt/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
