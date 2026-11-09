# Thorlabs MTD415T temperature controller

`labs/nelsond__thorlabs-mtd415t` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence MIT

Thorlabs MTD415T temperature controller, adapted from nelsond/thorlabs-mtd415t. It reads `temperature`, `setpoint`, `tec_current`, `tec_voltage` and 6 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/nelsond__thorlabs-mtd415t
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/nelsond__thorlabs-mtd415t --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "thorlabs-mtd415t": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/nelsond__thorlabs-mtd415t",
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

- **Reads:** `temperature`, `setpoint`, `tec_current`, `tec_voltage`, `tec_current_limit`, `errors`, `idn`, `uid`, `is_open`, `measure_temperature`
- **Sets:** —

## Source and status

- Upstream: [nelsond/thorlabs-mtd415t](https://github.com/nelsond/thorlabs-mtd415t) at `c53ec5c7db67` (MIT); fetch it with `python3 scripts/add_device.py labs/nelsond__thorlabs-mtd415t` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/nelsond__thorlabs-mtd415t`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/nelsond__thorlabs-mtd415t) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/nelsond__thorlabs-mtd415t/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/nelsond__thorlabs-mtd415t/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
