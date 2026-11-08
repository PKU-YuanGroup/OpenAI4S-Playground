# IKA RET Control Visc hotplate stirrer

`labs/croningp__chemputersoftware` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

IKA RET Control Visc hotplate stirrer, adapted from croningp/chemputersoftware. It reads `medium_temperature`, `stir_rate` and `ph`; sets `temperature_setpoint` and `stir_rate_setpoint`; runs `set_temperature`, `start_heating`, `stop_heating`, `start_stirring` and 2 more. `set_temperature`: set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/croningp__chemputersoftware
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/croningp__chemputersoftware --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "chemputersoftware": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/croningp__chemputersoftware",
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

- **Reads:** `medium_temperature`, `stir_rate`, `ph`
- **Sets:** `temperature_setpoint`, `stir_rate_setpoint`

| Action | What it does |
| --- | --- |
| `set_temperature` | Set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. |
| `start_heating` | Start the heater (START_1) |
| `stop_heating` | Stop the heater (STOP_1) |
| `start_stirring` | Start the stirrer (START_4) |
| `stop_stirring` | Stop the stirrer (STOP_4) |
| `stop_hotplate` | Safe state: stop the heater (STOP_1) and the stirrer (STOP_4); it takes no input |

## Source and status

- Upstream: [croningp/chemputersoftware](https://github.com/croningp/chemputersoftware) at `0f249ce8f7c3` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/croningp__chemputersoftware` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/croningp__chemputersoftware`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/croningp__chemputersoftware) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/croningp__chemputersoftware/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/croningp__chemputersoftware/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
