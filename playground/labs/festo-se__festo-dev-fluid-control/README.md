# Festo pressure-over-liquid instrument (FluidControlSession)

`labs/festo-se__festo-dev-fluid-control` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence LicenseRef-proprietary

Festo pressure-over-liquid instrument (FluidControlSession), adapted from festo-se/festo-dev-fluid-control. It reads `channels`, `liquid_classes` and `fluid_status`; sets `pressure`; runs `aspirate`, `dispense`, `mix` and `deactivate`. `aspirate`: aspirate a volume on one valve channel with a configured liquid class. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/festo-se__festo-dev-fluid-control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/festo-se__festo-dev-fluid-control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "festo-dev-fluid-control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/festo-se__festo-dev-fluid-control",
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

- **Reads:** `channels`, `liquid_classes`, `fluid_status`
- **Sets:** `pressure`

| Action | What it does |
| --- | --- |
| `aspirate` | Aspirate a volume on one valve channel with a configured liquid class |
| `dispense` | Dispense a volume on one valve channel with a configured liquid class |
| `mix` | Mix by repeating aspirate and dispense on one valve channel |
| `deactivate` | Return the instrument to its safe state: release the pressure and deselect every valve |

## Source and status

- Upstream: [festo-se/festo-dev-fluid-control](https://github.com/festo-se/festo-dev-fluid-control) at `2da14c5d6b20` (LicenseRef-proprietary); fetch it with `python3 scripts/add_device.py labs/festo-se__festo-dev-fluid-control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/festo-se__festo-dev-fluid-control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/festo-se__festo-dev-fluid-control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/festo-se__festo-dev-fluid-control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/festo-se__festo-dev-fluid-control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
