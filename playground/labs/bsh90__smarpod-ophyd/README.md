# SmarAct SmarPod hexapod (gh.bsh90/smarpod-ophyd SmarSignal)

`labs/bsh90__smarpod-ophyd` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

SmarAct SmarPod hexapod (gh.bsh90/smarpod-ophyd SmarSignal), adapted from bsh90/smarpod-ophyd. It sets `pose`; runs `move_pose` and `stop_motion`. `move_pose`: move the hexapod to a six-component pose and return the pose read after the controller reports STOPPED. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/bsh90__smarpod-ophyd
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/bsh90__smarpod-ophyd --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "smarpod-ophyd": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/bsh90__smarpod-ophyd",
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

- **Reads:** —
- **Sets:** `pose`

| Action | What it does |
| --- | --- |
| `move_pose` | Move the hexapod to a six-component pose and return the pose read after the controller reports STOPPED |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [bsh90/smarpod-ophyd](https://github.com/bsh90/smarpod-ophyd) at `a3d50e67618b` (MIT); fetch it with `python3 scripts/add_device.py labs/bsh90__smarpod-ophyd` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/bsh90__smarpod-ophyd`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/bsh90__smarpod-ophyd) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/bsh90__smarpod-ophyd/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/bsh90__smarpod-ophyd/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
