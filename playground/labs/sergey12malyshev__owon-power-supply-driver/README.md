# OWON power supply (owon_ps.OwonPowerSupply)

`labs/sergey12malyshev__owon-power-supply-driver` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence Apache-2.0

OWON power supply (owon_ps.OwonPowerSupply), adapted from sergey12malyshev/owon-power-supply-driver. It reads `voltage`, `current`, `power`, `identity` and 1 more; sets `voltage_setpoint`, `current_setpoint`, `voltage_limit`, `current_limit` and 1 more; runs `reset_config` and `output_off`. `reset_config`: reset the instrument to its factory configuration (*RST); it takes no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/sergey12malyshev__owon-power-supply-driver
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/sergey12malyshev__owon-power-supply-driver --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "owon-power-supply-driver": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/sergey12malyshev__owon-power-supply-driver",
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

- **Reads:** `voltage`, `current`, `power`, `identity`, `all_parameters`
- **Sets:** `voltage_setpoint`, `current_setpoint`, `voltage_limit`, `current_limit`, `output_enabled`

| Action | What it does |
| --- | --- |
| `reset_config` | Reset the instrument to its factory configuration (*RST); it takes no input |
| `output_off` | Disable the output (OUTPut OFF); it takes no input and is the declared safe state |

## Source and status

- Upstream: [sergey12malyshev/owon-power-supply-driver](https://github.com/sergey12malyshev/owon-power-supply-driver) at `37ec9d93df28` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/sergey12malyshev__owon-power-supply-driver` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/sergey12malyshev__owon-power-supply-driver`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/sergey12malyshev__owon-power-supply-driver) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/sergey12malyshev__owon-power-supply-driver/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/sergey12malyshev__owon-power-supply-driver/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
