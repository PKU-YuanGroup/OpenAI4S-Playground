# ASI MS-2000-500-CP stage controller (asi_MS_2000_500_CP.Controller)

`labs/amsikking__asi_ms_2000_500_cp` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

ASI MS-2000-500-CP stage controller (asi_MS_2000_500_CP.Controller), adapted from amsikking/asi_ms_2000_500_cp. It reads `position_x`, `position_y`, `position_z` and `motor_moving`; sets `pwm_intensity` and `pwm_state`; runs `move_stage`. `move_stage`: move the X, Y and Z stage axes to absolute positions in micrometres and wait for the controller to verify the target. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/amsikking__asi_ms_2000_500_cp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/amsikking__asi_ms_2000_500_cp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "asi_ms_2000_500_cp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/amsikking__asi_ms_2000_500_cp",
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

- **Reads:** `position_x`, `position_y`, `position_z`, `motor_moving`
- **Sets:** `pwm_intensity`, `pwm_state`

| Action | What it does |
| --- | --- |
| `move_stage` | Move the X, Y and Z stage axes to absolute positions in micrometres and wait for the controller to verify the target |

## Source and status

- Upstream: [amsikking/asi_ms_2000_500_cp](https://github.com/amsikking/asi_ms_2000_500_cp) at `5f1f6d2cad54` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/amsikking__asi_ms_2000_500_cp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/amsikking__asi_ms_2000_500_cp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/amsikking__asi_ms_2000_500_cp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/amsikking__asi_ms_2000_500_cp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/amsikking__asi_ms_2000_500_cp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
