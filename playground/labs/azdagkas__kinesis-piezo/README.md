# Thorlabs TPZ001 piezo controller (piezo.PiezoController)

`labs/azdagkas__kinesis-piezo` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

Thorlabs TPZ001 piezo controller (piezo.PiezoController), adapted from azdagkas/kinesis-piezo. It reads `units`, `reader_reading`, `reader_units` and `zeroing`; sets `value` and `closed_loop`; runs `move_to_home`, `jog_up`, `jog_down`, `calibrate_position` and 2 more. `move_to_home`: drive the piezo travel to zero with the native move_to_home (the safe state). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/azdagkas__kinesis-piezo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/azdagkas__kinesis-piezo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "kinesis-piezo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/azdagkas__kinesis-piezo",
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

- **Reads:** `units`, `reader_reading`, `reader_units`, `zeroing`
- **Sets:** `value`, `closed_loop`

| Action | What it does |
| --- | --- |
| `move_to_home` | Drive the piezo travel to zero with the native move_to_home (the safe state) |
| `jog_up` | Step the controller value up by one configured jog step (the native moveup) |
| `jog_down` | Step the controller value down by one configured jog step (the native movedown) |
| `calibrate_position` | Run the native calibration: drive 10 and 70 percent and fit percentage travel to the strain gauge reader |
| `move_to_position` | Move to a strain gauge reader position with the stored calibration (the native move_to_pos) |
| `zero_reader` | Zero the strain gauge reader with the native reader set_zero |

## Source and status

- Upstream: [azdagkas/kinesis-piezo](https://github.com/azdagkas/kinesis-piezo) at `ecfe0586cef3` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/azdagkas__kinesis-piezo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/azdagkas__kinesis-piezo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/azdagkas__kinesis-piezo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/azdagkas__kinesis-piezo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/azdagkas__kinesis-piezo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
