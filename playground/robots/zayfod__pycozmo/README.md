# Digital Dream Labs Cozmo (pycozmo.Client)

`robots/zayfod__pycozmo` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Digital Dream Labs Cozmo (pycozmo.Client), adapted from zayfod/pycozmo. It reads `head_angle`, `lift_height`, `lift_angle`, `battery_voltage` and 2 more; runs `move_joints`. `move_joints`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/zayfod__pycozmo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/zayfod__pycozmo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pycozmo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/zayfod__pycozmo",
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

- **Reads:** `head_angle`, `lift_height`, `lift_angle`, `battery_voltage`, `is_picked_up`, `is_moving`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_joints` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |

## Source and status

- Upstream: [zayfod/pycozmo](https://github.com/zayfod/pycozmo) at `1b6dcd9b869a` (MIT); fetch it with `python3 scripts/add_device.py robots/zayfod__pycozmo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/zayfod__pycozmo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/zayfod__pycozmo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/zayfod__pycozmo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/zayfod__pycozmo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
