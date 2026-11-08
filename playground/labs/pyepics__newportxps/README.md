# Newport XPS motion controller (newportxps.NewportXPS)

`labs/pyepics__newportxps` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Newport XPS motion controller (newportxps.NewportXPS), adapted from pyepics/newportxps. It reads `stage`, `group`, `position`, `group_status` and 3 more; runs `move_stage`, `move_stage_relative`, `home_group`, `enable_group` and 2 more. `move_stage`: move the bound stage to an absolute position in controller user units. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pyepics__newportxps
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pyepics__newportxps --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "newportxps": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pyepics__newportxps",
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

- **Reads:** `stage`, `group`, `position`, `group_status`, `hardware_status`, `positioner_errors`, `tuning`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_stage` | Move the bound stage to an absolute position in controller user units |
| `move_stage_relative` | Move the bound stage by a relative offset in controller user units |
| `home_group` | Run the native home search of the bound group (the stage moves to its reference) |
| `enable_group` | Enable motion on the bound group (the native GroupMotionEnable) |
| `disable_group` | Disable motion on the bound group (the native GroupMotionDisable) |
| `abort_group` | Abort the bound group's running move (the native GroupMoveAbort); the controller applies its configured deceleration and the call takes no profile |

## Source and status

- Upstream: [pyepics/newportxps](https://github.com/pyepics/newportxps) at `5ee41fced858` (MIT); fetch it with `python3 scripts/add_device.py labs/pyepics__newportxps` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pyepics__newportxps`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pyepics__newportxps) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pyepics__newportxps/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pyepics__newportxps/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
