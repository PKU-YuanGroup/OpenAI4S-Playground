# Anki Cozmo robot (cozmo.robot.Robot)

`robots/anki__cozmo-python-sdk` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence Apache-2.0

Anki Cozmo robot (cozmo.robot.Robot), adapted from anki/cozmo-python-sdk. It reads `head_angle`, `lift_ratio`, `lift_height`, `is_charging` and 1 more; runs `move_head`, `set_lift_ratio` and `stop_all`. `move_head`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/anki__cozmo-python-sdk
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/anki__cozmo-python-sdk --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "cozmo-python-sdk": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/anki__cozmo-python-sdk",
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

- **Reads:** `head_angle`, `lift_ratio`, `lift_height`, `is_charging`, `cliff_detected`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_head` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |
| `set_lift_ratio` | Move the lift to a ratio between 0.0 (bottom) and 1.0 (top) and wait until it is there |
| `stop_all` | Stop every motor of the robot at once (the native stop_all_motors); it takes no input |

## Source and status

- Upstream: [anki/cozmo-python-sdk](https://github.com/anki/cozmo-python-sdk) at `dd29edef1874` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/anki__cozmo-python-sdk` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/anki__cozmo-python-sdk`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/anki__cozmo-python-sdk) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/anki__cozmo-python-sdk/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/anki__cozmo-python-sdk/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
