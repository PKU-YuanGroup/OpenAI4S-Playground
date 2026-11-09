# PI GCS2 stage controller (PyMoDAQ PIWrapper)

`labs/pymodaq__pymodaq_plugins_physik_instrumente` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

PI GCS2 stage controller (PyMoDAQ PIWrapper), adapted from pymodaq/pymodaq_plugins_physik_instrumente. It reads `identity`, `axis_names`, `axis_units`, `positions` and 2 more; runs `move_absolute`, `move_relative`, `home_axis` and `stop_motion`. `move_absolute`: move one axis to an absolute position with the native move_absolute() and report the position the controller reads back. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pymodaq__pymodaq_plugins_physik_instrumente
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pymodaq__pymodaq_plugins_physik_instrumente --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymodaq_plugins_physik_instrumente": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pymodaq__pymodaq_plugins_physik_instrumente",
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

- **Reads:** `identity`, `axis_names`, `axis_units`, `positions`, `referenced`, `servo_enabled`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_absolute` | Move one axis to an absolute position with the native move_absolute() and report the position the controller reads back |
| `move_relative` | Move one axis by a relative step with the native move_relative() and report the position the controller reads back |
| `home_axis` | Home one axis with the native move_home() and report whether the controller then reports it as referenced |
| `stop_motion` | Stop all motion with the native stop() (the controller's StopAll command). It takes no input because the native stop takes no profile or position |

## Source and status

- Upstream: [pymodaq/pymodaq_plugins_physik_instrumente](https://github.com/pymodaq/pymodaq_plugins_physik_instrumente) at `6fb8d954c432` (MIT); fetch it with `python3 scripts/add_device.py labs/pymodaq__pymodaq_plugins_physik_instrumente` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pymodaq__pymodaq_plugins_physik_instrumente`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_physik_instrumente) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_physik_instrumente/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pymodaq__pymodaq_plugins_physik_instrumente/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
