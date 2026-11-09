# IKA RET control-visc hotplate stirrer

`labs/kist-csrc__batchsynthesismodule` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

IKA RET control-visc hotplate stirrer, adapted from kist-csrc/batchsynthesismodule. It reads `medium_temperature`, `hot_plate_temperature`, `heat_transfer_medium_setpoint`, `hot_plate_safety_setpoint` and 3 more; sets `medium_setpoint`, `hot_plate_setpoint` and `stir_rate_setpoint`; runs `heat_to`, `set_heater`, `set_stirrer`, `set_ph_meter` and 3 more. `heat_to`: set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/kist-csrc__batchsynthesismodule
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/kist-csrc__batchsynthesismodule --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "batchsynthesismodule": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/kist-csrc__batchsynthesismodule",
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

- **Reads:** `medium_temperature`, `hot_plate_temperature`, `heat_transfer_medium_setpoint`, `hot_plate_safety_setpoint`, `stir_rate`, `ph`, `weight`
- **Sets:** `medium_setpoint`, `hot_plate_setpoint`, `stir_rate_setpoint`

| Action | What it does |
| --- | --- |
| `heat_to` | Set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. |
| `set_heater` | Start or stop the hot plate heater |
| `set_stirrer` | Start or stop the stirrer |
| `set_ph_meter` | Start or stop the integrated pH meter |
| `set_weighing` | Start or stop the integrated weighing function |
| `reset_hot_plate` | Send RESET to the hot plate |
| `stop_heating_and_stirring` | Stop the heater and the stirrer (STOP_1 and STOP_4); the native safe state |

## Source and status

- Upstream: [kist-csrc/batchsynthesismodule](https://github.com/kist-csrc/batchsynthesismodule) at `5d0e9bb2ae49` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/kist-csrc__batchsynthesismodule` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/kist-csrc__batchsynthesismodule`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/kist-csrc__batchsynthesismodule) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/kist-csrc__batchsynthesismodule/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/kist-csrc__batchsynthesismodule/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
