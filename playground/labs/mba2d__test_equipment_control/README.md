# A2D electronic load

`labs/mba2d__test_equipment_control` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

A2D electronic load, adapted from mba2d/test_equipment_control. It reads `voltage`, `adc_voltage`, `current_reported` and `temperature`; sets `current`, `output`, `led` and `fan`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/mba2d__test_equipment_control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/mba2d__test_equipment_control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "test_equipment_control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/mba2d__test_equipment_control",
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

- **Reads:** `voltage`, `adc_voltage`, `current_reported`, `temperature`
- **Sets:** `current`, `output`, `led`, `fan`

## Source and status

- Upstream: [mba2d/test_equipment_control](https://github.com/mba2d/test_equipment_control) at `34bb54c13c76` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/mba2d__test_equipment_control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/mba2d__test_equipment_control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/mba2d__test_equipment_control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/mba2d__test_equipment_control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/mba2d__test_equipment_control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
