# ADAMSim ADAM mobile base

`robots/mobile-robots-group-uc3m__adamsim` · Mobile robots · simulation · risk R2 · licence NOASSERTION

ADAMSim ADAM mobile base, adapted from mobile-robots-group-uc3m/adamsim. It reads `camera_angle`, `left_arm_joint_positions` and `right_arm_joint_positions`; runs `drive` and `stop_motion`. `drive`: drive a mobile base with a commanded linear and angular velocity for a bounded duration, or to a target pose. Obstacle and zone limits are enforced by the binding safety envelope. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/mobile-robots-group-uc3m__adamsim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/mobile-robots-group-uc3m__adamsim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "adamsim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/mobile-robots-group-uc3m__adamsim",
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

- **Reads:** `camera_angle`, `left_arm_joint_positions`, `right_arm_joint_positions`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `drive` | Drive a mobile base with a commanded linear and angular velocity for a bounded duration, or to a target pose. Obstacle and zone limits are enforced by the binding safety envelope. |
| `stop_motion` | Command both wheel targets to zero through Navigation.move_wheels. The upstream exposes no wheel-velocity readback and no deceleration profile, so the receipt reports that the zero command was applied, not that the simulated base was measured at rest. |

## Source and status

- Upstream: [mobile-robots-group-uc3m/adamsim](https://github.com/mobile-robots-group-uc3m/adamsim) at `85a9b1fce83a` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/mobile-robots-group-uc3m__adamsim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/mobile-robots-group-uc3m__adamsim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/mobile-robots-group-uc3m__adamsim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/mobile-robots-group-uc3m__adamsim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/mobile-robots-group-uc3m__adamsim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
