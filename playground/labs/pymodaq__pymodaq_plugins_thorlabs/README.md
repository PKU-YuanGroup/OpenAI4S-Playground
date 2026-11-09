# Thorlabs Kinesis brushless DC motor controller channel

`labs/pymodaq__pymodaq_plugins_thorlabs` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Thorlabs Kinesis brushless DC motor controller channel, adapted from pymodaq/pymodaq_plugins_thorlabs. It reads `position`, `target_position`, `units`, `homed` and 1 more; runs `move_abs`, `move_rel`, `home` and `stop_motion`. `move_abs`: move the bound Kinesis channel to an absolute target with the controller's native MoveTo. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pymodaq__pymodaq_plugins_thorlabs
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pymodaq__pymodaq_plugins_thorlabs --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymodaq_plugins_thorlabs": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pymodaq__pymodaq_plugins_thorlabs",
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

- **Reads:** `position`, `target_position`, `units`, `homed`, `channel`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_abs` | Move the bound Kinesis channel to an absolute target with the controller's native MoveTo |
| `move_rel` | Move the bound Kinesis channel by a relative offset; the target is computed from the current position and issued through the native absolute move, as the PyMoDAQ plugin does |
| `home` | Start the native home move of the bound Kinesis channel; the controller performs the move asynchronously |
| `stop_motion` | Stop motion of the bound Kinesis channel with the native Stop(0); the call takes no deceleration profile |

## Source and status

- Upstream: [pymodaq/pymodaq_plugins_thorlabs](https://github.com/pymodaq/pymodaq_plugins_thorlabs) at `4aaf06acf6ea` (MIT); fetch it with `python3 scripts/add_device.py labs/pymodaq__pymodaq_plugins_thorlabs` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pymodaq__pymodaq_plugins_thorlabs`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_thorlabs) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_thorlabs/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pymodaq__pymodaq_plugins_thorlabs/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
