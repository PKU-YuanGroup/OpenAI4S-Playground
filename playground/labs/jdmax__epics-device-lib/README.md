# Lake Shore 336 temperature controller (epics-device-lib ls336 DeviceConnection)

`labs/jdmax__epics-device-lib` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Lake Shore 336 temperature controller (epics-device-lib ls336 DeviceConnection), adapted from jdmax/epics-device-lib. It reads `temperature`, `temperatures`, `heater_output`, `pid` and 1 more; sets `setpoint`, `manual_heater` and `heater_range`; runs `set_temperature`, `heater_off` and `enable_heater`. `set_temperature`: set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/jdmax__epics-device-lib
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/jdmax__epics-device-lib --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "epics-device-lib": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/jdmax__epics-device-lib",
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

- **Reads:** `temperature`, `temperatures`, `heater_output`, `pid`, `output_mode`
- **Sets:** `setpoint`, `manual_heater`, `heater_range`

| Action | What it does |
| --- | --- |
| `set_temperature` | Set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. |
| `heater_off` | Command the configured heater output off (OUTMODE <channel>,0,<channel>,0) and confirm mode 0 with a fresh OUTMODE? read; it takes no input |
| `enable_heater` | Command the configured output back to the reenable_mode option's control mode (default Closed Loop) with OUTMODE <channel>,<mode>,<channel>,0 and confirm it with OUTMODE?; heating resumes toward the setpoint or manual output stored in the controller; it takes no input |

## Source and status

- Upstream: [jdmax/epics-device-lib](https://github.com/jdmax/epics-device-lib) at `370b8e3d9422` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/jdmax__epics-device-lib` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/jdmax__epics-device-lib`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/jdmax__epics-device-lib) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/jdmax__epics-device-lib/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/jdmax__epics-device-lib/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
