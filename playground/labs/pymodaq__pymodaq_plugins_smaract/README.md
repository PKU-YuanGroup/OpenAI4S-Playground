# SmarAct MCS2 controller channel (pymodaq_plugins_smaract)

`labs/pymodaq__pymodaq_plugins_smaract` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

SmarAct MCS2 controller channel (pymodaq_plugins_smaract), adapted from pymodaq/pymodaq_plugins_smaract. It reads `position`, `units`, `base_resolution`, `positioner_type` and 3 more; runs `absolute_move`, `relative_move`, `find_reference` and `stop_motion`. `absolute_move`: move the bound MCS2 channel to an absolute position given in controller base units. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pymodaq__pymodaq_plugins_smaract
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pymodaq__pymodaq_plugins_smaract --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymodaq_plugins_smaract": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pymodaq__pymodaq_plugins_smaract",
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

- **Reads:** `position`, `units`, `base_resolution`, `positioner_type`, `device_name`, `number_of_channels`, `channel`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `absolute_move` | Move the bound MCS2 channel to an absolute position given in controller base units |
| `relative_move` | Move the bound MCS2 channel by a relative offset given in controller base units |
| `find_reference` | Start the reference search of the bound MCS2 channel (the native find_reference); the search itself is asynchronous |
| `stop_motion` | Stop motion on the bound MCS2 channel (the native stop); the controller applies its configured stop profile and the call takes no profile |

## Source and status

- Upstream: [pymodaq/pymodaq_plugins_smaract](https://github.com/pymodaq/pymodaq_plugins_smaract) at `eeb3fa8ced4c` (MIT); fetch it with `python3 scripts/add_device.py labs/pymodaq__pymodaq_plugins_smaract` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pymodaq__pymodaq_plugins_smaract`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_smaract) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_smaract/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pymodaq__pymodaq_plugins_smaract/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
