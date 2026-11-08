# Standa rotation mount via ImSwitch (StandaMotor)

`labs/imswitch__imswitch` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Standa rotation mount via ImSwitch (StandaMotor), adapted from imswitch/imswitch. It reads `position`; runs `move_absolute` and `stop_motion`. `move_absolute`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/imswitch__imswitch
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/imswitch__imswitch --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "imswitch": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/imswitch__imswitch",
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

- **Reads:** `position`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_absolute` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [imswitch/imswitch](https://github.com/imswitch/imswitch) at `37bf1df6de0e` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/imswitch__imswitch` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/imswitch__imswitch`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/imswitch__imswitch) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/imswitch__imswitch/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/imswitch__imswitch/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
