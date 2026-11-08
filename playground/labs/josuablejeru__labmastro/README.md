# Hanmatek HM bench supply (labmastro Modbus RTU)

`labs/josuablejeru__labmastro` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

Hanmatek HM bench supply (labmastro Modbus RTU), adapted from josuablejeru/labmastro. It reads `output_enabled`, `voltage` and `current`; sets `voltage_setpoint`, `current_setpoint`, `over_voltage_protection` and `over_current_protection`; runs `output_on` and `output_off`. `output_on`: enable the output (0x0001 = 1, confirmed by read-back) at the supply's live setpoints, which this package cannot read or bound: set and verify them on the supply first. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/josuablejeru__labmastro
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/josuablejeru__labmastro --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "labmastro": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/josuablejeru__labmastro",
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

- **Reads:** `output_enabled`, `voltage`, `current`
- **Sets:** `voltage_setpoint`, `current_setpoint`, `over_voltage_protection`, `over_current_protection`

| Action | What it does |
| --- | --- |
| `output_on` | Enable the output (0x0001 = 1, confirmed by read-back) at the supply's live setpoints, which this package cannot read or bound: set and verify them on the supply first |
| `output_off` | Disable the supply output (register 0x0001 = 0) and confirm it by read-back |

## Source and status

- Upstream: [josuablejeru/labmastro](https://github.com/josuablejeru/labmastro) at `86db05e8dd4e` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/josuablejeru__labmastro` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/josuablejeru__labmastro`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/josuablejeru__labmastro) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/josuablejeru__labmastro/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/josuablejeru__labmastro/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
