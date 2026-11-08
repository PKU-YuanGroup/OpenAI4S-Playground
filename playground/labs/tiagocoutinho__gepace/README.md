# GE Druck Pace pressure controller (gepace.Pace)

`labs/tiagocoutinho__gepace` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence LGPL-3.0

GE Druck Pace pressure controller (gepace.Pace), adapted from tiagocoutinho/gepace. It reads `idn`, `version`, `mac`, `task` and 11 more; runs `set_pressure_control`, `start_pressure_control` and `stop_pressure_control`. `set_pressure_control`: enable or disable the pressure control output of module 1 (OUTP1:STAT). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/tiagocoutinho__gepace
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/tiagocoutinho__gepace --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "gepace": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/tiagocoutinho__gepace",
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

- **Reads:** `idn`, `version`, `mac`, `task`, `world_area`, `hw_test`, `error`, `startup_mode`, `serial_numbers`, `pressure`, `barometric_pressure`, `pressure_control`, `pressure_unit`, `pressure_range`, `pressure_in_limits`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_pressure_control` | Enable or disable the pressure control output of module 1 (OUTP1:STAT) |
| `start_pressure_control` | Enable the pressure control output of module 1 (the native start, OUTP1:STAT 1) |
| `stop_pressure_control` | Disable the pressure control output of module 1 (the native stop, the safe state); it takes no input |

## Source and status

- Upstream: [tiagocoutinho/gepace](https://github.com/tiagocoutinho/gepace) at `4caa5f8c4042` (LGPL-3.0); fetch it with `python3 scripts/add_device.py labs/tiagocoutinho__gepace` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/tiagocoutinho__gepace`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/tiagocoutinho__gepace) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/tiagocoutinho__gepace/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/tiagocoutinho__gepace/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
