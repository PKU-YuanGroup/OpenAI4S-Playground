# Newport SMC100 single-axis motion controller

`labs/pymodaq__pymodaq_plugins_newport` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Newport SMC100 single-axis motion controller, adapted from pymodaq/pymodaq_plugins_newport. It reads `identity`, `position`, `is_moving`, `speed` and 1 more; runs `move_abs`, `move_rel`, `home` and `stop_motion`. `move_abs`: command an absolute move with PA; the controller reports completion through is_moving. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pymodaq__pymodaq_plugins_newport
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pymodaq__pymodaq_plugins_newport --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymodaq_plugins_newport": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pymodaq__pymodaq_plugins_newport",
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

- **Reads:** `identity`, `position`, `is_moving`, `speed`, `acceleration`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_abs` | Command an absolute move with PA; the controller reports completion through is_moving |
| `move_rel` | Command a relative move with PR; the controller reports completion through is_moving |
| `home` | Drive axes to their declared home position or reference switch, establishing the coordinate reference needed by other motion capabilities. |
| `stop_motion` | Stop motion with the controller's ST command |

## Source and status

- Upstream: [pymodaq/pymodaq_plugins_newport](https://github.com/pymodaq/pymodaq_plugins_newport) at `bad8a714aa07` (MIT); fetch it with `python3 scripts/add_device.py labs/pymodaq__pymodaq_plugins_newport` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pymodaq__pymodaq_plugins_newport`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_newport) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_newport/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pymodaq__pymodaq_plugins_newport/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
