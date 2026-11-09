# Anycubic i3 Mega pipettebot gantry

`labs/qte77__i3mega-pipettebot` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence Apache-2.0

Anycubic i3 Mega pipettebot gantry, adapted from qte77/i3mega-pipettebot. It reads `x`, `y` and `z`; runs `move_to`, `home` and `emergency_stop`. `move_to`: move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/qte77__i3mega-pipettebot
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/qte77__i3mega-pipettebot --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "i3mega-pipettebot": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/qte77__i3mega-pipettebot",
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

- **Reads:** `x`, `y`, `z`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_to` | Move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. |
| `home` | Drive axes to their declared home position or reference switch, establishing the coordinate reference needed by other motion capabilities. |
| `emergency_stop` | Send the firmware emergency stop M112; it takes no input and is the declared safe state |

## Source and status

- Upstream: [qte77/i3mega-pipettebot](https://github.com/qte77/i3mega-pipettebot) at `99dc2e0a8c15` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/qte77__i3mega-pipettebot` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/qte77__i3mega-pipettebot`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/qte77__i3mega-pipettebot) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/qte77__i3mega-pipettebot/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/qte77__i3mega-pipettebot/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
