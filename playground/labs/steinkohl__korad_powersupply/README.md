# Korad KC3405P power supply (korad.KC3405P)

`labs/steinkohl__korad_powersupply` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Korad KC3405P power supply (korad.KC3405P), adapted from steinkohl/korad_powersupply. It reads `channel`, `voltage`, `current`, `regulation_mode` and 4 more; sets `voltage_setpoint`, `current_setpoint`, `overvoltage_protection_setpoint`, `overcurrent_protection_setpoint` and 3 more; runs `output_off`. `output_off`: send OUT1234:0 to all four outputs through the native send path (the safe state); it takes no input and does not wait for a status reply. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/steinkohl__korad_powersupply
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/steinkohl__korad_powersupply --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "korad_powersupply": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/steinkohl__korad_powersupply",
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

- **Reads:** `channel`, `voltage`, `current`, `regulation_mode`, `device_info`, `status`, `measure_voltage`, `measure_current`
- **Sets:** `voltage_setpoint`, `current_setpoint`, `overvoltage_protection_setpoint`, `overcurrent_protection_setpoint`, `overvoltage_protection_enabled`, `overcurrent_protection_enabled`, `output_enabled`

| Action | What it does |
| --- | --- |
| `output_off` | Send OUT1234:0 to all four outputs through the native send path (the safe state); it takes no input and does not wait for a status reply |

## Source and status

- Upstream: [steinkohl/korad_powersupply](https://github.com/steinkohl/korad_powersupply) at `fd2e8b7c59a4` (MIT); fetch it with `python3 scripts/add_device.py labs/steinkohl__korad_powersupply` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/steinkohl__korad_powersupply`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/steinkohl__korad_powersupply) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/steinkohl__korad_powersupply/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/steinkohl__korad_powersupply/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
