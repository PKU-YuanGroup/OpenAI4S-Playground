# LTAMP simulated PR2 (PyBullet PBController)

`robots/caelan__ltamp` · Robot arms and grippers · simulation · risk R1 · licence GPL-3.0

LTAMP simulated PR2 (PyBullet PBController), adapted from caelan/ltamp. It reads `joint_positions`; sets `torso_position`; runs `move_arms`. `move_arms`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/caelan__ltamp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/caelan__ltamp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ltamp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/caelan__ltamp",
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

- **Reads:** `joint_positions`
- **Sets:** `torso_position`

| Action | What it does |
| --- | --- |
| `move_arms` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |

## Source and status

- Upstream: [caelan/ltamp](https://github.com/caelan/ltamp) at `7e0a28dca115` (GPL-3.0); fetch it with `python3 scripts/add_device.py robots/caelan__ltamp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/caelan__ltamp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/caelan__ltamp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/caelan__ltamp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/caelan__ltamp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
