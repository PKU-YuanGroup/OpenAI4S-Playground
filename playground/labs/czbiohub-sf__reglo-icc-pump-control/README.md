# Masterflex Ismatec Reglo ICC peristaltic pump

`labs/czbiohub-sf__reglo-icc-pump-control` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

Masterflex Ismatec Reglo ICC peristaltic pump, adapted from czbiohub-sf/reglo-icc-pump-control. It reads `max_flow_rate`, `running`, `channel_count`, `pump_address` and 4 more; sets `tubing_id`; runs `pump` and `stop_pump`. `pump`: run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/czbiohub-sf__reglo-icc-pump-control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/czbiohub-sf__reglo-icc-pump-control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "reglo-icc-pump-control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/czbiohub-sf__reglo-icc-pump-control",
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

- **Reads:** `max_flow_rate`, `running`, `channel_count`, `pump_address`, `serial_number`, `model_number`, `software_version`, `head_code`
- **Sets:** `tubing_id`

| Action | What it does |
| --- | --- |
| `pump` | Run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. |
| `stop_pump` | Stop every channel of the pump (the native stop, the safe state); it takes no input |

## Source and status

- Upstream: [czbiohub-sf/reglo-icc-pump-control](https://github.com/czbiohub-sf/reglo-icc-pump-control) at `af0f8648a565` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/czbiohub-sf__reglo-icc-pump-control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/czbiohub-sf__reglo-icc-pump-control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/czbiohub-sf__reglo-icc-pump-control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/czbiohub-sf__reglo-icc-pump-control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/czbiohub-sf__reglo-icc-pump-control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
