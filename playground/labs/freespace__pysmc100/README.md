# Newport SMC100 single-axis motion controller

`labs/freespace__pysmc100` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Newport SMC100 single-axis motion controller, adapted from freespace/pysmc100. It reads `position`, `error_code` and `state`; runs `home`, `move_absolute` and `move_relative`. `home`: home the stage and leave it at the origin. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/freespace__pysmc100
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/freespace__pysmc100 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pysmc100": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/freespace__pysmc100",
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

- **Reads:** `position`, `error_code`, `state`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `home` | Home the stage and leave it at the origin |
| `move_absolute` | Move the stage to an absolute position in millimetres |
| `move_relative` | Move the stage by a relative distance in millimetres |

## Source and status

- Upstream: [freespace/pysmc100](https://github.com/freespace/pysmc100) at `8c65638934ed` (MIT); fetch it with `python3 scripts/add_device.py labs/freespace__pysmc100` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/freespace__pysmc100`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/freespace__pysmc100) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/freespace__pysmc100/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/freespace__pysmc100/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
