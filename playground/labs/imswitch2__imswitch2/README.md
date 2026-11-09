# ImSwitch2 Standa rotation mount

`labs/imswitch2__imswitch2` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

ImSwitch2 Standa rotation mount, adapted from imswitch2/imswitch2. It reads `position`; runs `move_absolute` and `stop_motion`. `move_absolute`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/imswitch2__imswitch2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/imswitch2__imswitch2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "imswitch2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/imswitch2__imswitch2",
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

- Upstream: [imswitch2/imswitch2](https://github.com/imswitch2/imswitch2) at `86763f7ba89f` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/imswitch2__imswitch2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/imswitch2__imswitch2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/imswitch2__imswitch2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/imswitch2__imswitch2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/imswitch2__imswitch2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
