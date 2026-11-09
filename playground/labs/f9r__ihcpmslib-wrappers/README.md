# INHECO SCILA CO2 incubator (ihcWrappers.scila.ScilaWrapper)

`labs/f9r__ihcpmslib-wrappers` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-2-Clause

INHECO SCILA CO2 incubator (ihcWrappers.scila.ScilaWrapper), adapted from f9r/ihcpmslib-wrappers. It reads `device_name`, `firmware_version`, `state`, `current_temperature` and 8 more; sets `auto_boost_co2`; runs `set_temperature` and `stop_incubation`. `set_temperature`: set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/f9r__ihcpmslib-wrappers
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/f9r__ihcpmslib-wrappers --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ihcpmslib-wrappers": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/f9r__ihcpmslib-wrappers",
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

- **Reads:** `device_name`, `firmware_version`, `state`, `current_temperature`, `target_temperature`, `temperature_control`, `boost_state`, `co2_flow_status`, `liquid_level`, `door_status`, `valve_status`, `measure_temperature`
- **Sets:** `auto_boost_co2`

| Action | What it does |
| --- | --- |
| `set_temperature` | Set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. |
| `stop_incubation` | Stop temperature control and both CO2 flow paths (the safe state); it takes no input |

## Source and status

- Upstream: [f9r/ihcpmslib-wrappers](https://github.com/f9r/ihcpmslib-wrappers) at `3e6bd4c47f39` (BSD-2-Clause); fetch it with `python3 scripts/add_device.py labs/f9r__ihcpmslib-wrappers` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/f9r__ihcpmslib-wrappers`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/f9r__ihcpmslib-wrappers) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/f9r__ihcpmslib-wrappers/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/f9r__ihcpmslib-wrappers/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
