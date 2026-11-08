# NSLS-II CHX syringe pump controller

`labs/nsls-ii-chx__syringe_pump_controller` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

NSLS-II CHX syringe pump controller, adapted from nsls-ii-chx/syringe_pump_controller. It reads `direction` and `dispensed_volume`; sets `flow_rate` and `volume`; runs `dispense` and `stop_pump`. `dispense`: run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/nsls-ii-chx__syringe_pump_controller
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/nsls-ii-chx__syringe_pump_controller --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "syringe_pump_controller": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/nsls-ii-chx__syringe_pump_controller",
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

- **Reads:** `direction`, `dispensed_volume`
- **Sets:** `flow_rate`, `volume`

| Action | What it does |
| --- | --- |
| `dispense` | Run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. |
| `stop_pump` | Stop every pump with the CR-terminated STP command; takes no input |

## Source and status

- Upstream: [nsls-ii-chx/syringe_pump_controller](https://github.com/nsls-ii-chx/syringe_pump_controller) at `cbda9ca1c201` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/nsls-ii-chx__syringe_pump_controller` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/nsls-ii-chx__syringe_pump_controller`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/nsls-ii-chx__syringe_pump_controller) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/nsls-ii-chx__syringe_pump_controller/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/nsls-ii-chx__syringe_pump_controller/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
