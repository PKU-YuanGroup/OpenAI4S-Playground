# Festo FPosBAPI gantry (FPosBAPIClient)

`labs/festo-se__festo-dev-applied-motion` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Festo FPosBAPI gantry (FPosBAPIClient), adapted from festo-se/festo-dev-applied-motion. It reads `position`, `sys_status`, `error_active`, `error_text` and 1 more; sets `global_speed`; runs `home`, `cartesian_pose` and `stop`. `home`: home all axes with one PLC HOME command; the PLC homes X, Y and Z together. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/festo-se__festo-dev-applied-motion
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/festo-se__festo-dev-applied-motion --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "festo-dev-applied-motion": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/festo-se__festo-dev-applied-motion",
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

- **Reads:** `position`, `sys_status`, `error_active`, `error_text`, `fieldbus_error`
- **Sets:** `global_speed`

| Action | What it does |
| --- | --- |
| `home` | Home all axes with one PLC HOME command; the PLC homes X, Y and Z together |
| `cartesian_pose` | Move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. |
| `stop` | Halt the current motion with the PLC HALT command (the safe state); it takes no input |

## Source and status

- Upstream: [festo-se/festo-dev-applied-motion](https://github.com/festo-se/festo-dev-applied-motion) at `c1926f02d8e6` (MIT); fetch it with `python3 scripts/add_device.py labs/festo-se__festo-dev-applied-motion` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/festo-se__festo-dev-applied-motion`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/festo-se__festo-dev-applied-motion) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/festo-se__festo-dev-applied-motion/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/festo-se__festo-dev-applied-motion/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
