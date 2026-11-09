# Tecan SparkControl microplate reader (spark_control_automation.SparkControlClient)

`labs/aaronslaff__tecan_sparkcontrol` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Tecan SparkControl microplate reader (spark_control_automation.SparkControlClient), adapted from aaronslaff/tecan_sparkcontrol. It reads `instrument_status`, `available_apps`, `instrument_settings`, `plate_geometry` and 2 more; runs `calibrate`, `start_method`, `stop_method` and `stop_active_method`. `calibrate`: run the native calibration procedure for a calibration type. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/aaronslaff__tecan_sparkcontrol
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/aaronslaff__tecan_sparkcontrol --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tecan_sparkcontrol": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/aaronslaff__tecan_sparkcontrol",
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

- **Reads:** `instrument_status`, `available_apps`, `instrument_settings`, `plate_geometry`, `method_status`, `measurement_results`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `calibrate` | Run the native calibration procedure for a calibration type |
| `start_method` | Start a method and remember its id for the stop path |
| `stop_method` | Stop the method with the given id and remember it for the safe-state action |
| `stop_active_method` | Stop the tracked method (the safe state); it takes no input |

## Source and status

- Upstream: [aaronslaff/tecan_sparkcontrol](https://github.com/aaronslaff/tecan_sparkcontrol) at `d2272c6d0e0d` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/aaronslaff__tecan_sparkcontrol` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/aaronslaff__tecan_sparkcontrol`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/aaronslaff__tecan_sparkcontrol) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/aaronslaff__tecan_sparkcontrol/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/aaronslaff__tecan_sparkcontrol/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
