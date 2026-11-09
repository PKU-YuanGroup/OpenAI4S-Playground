# Runze ZSB-SY01B multichannel syringe pump

`labs/allenneuraldynamics__runze-control` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Runze ZSB-SY01B multichannel syringe pump, adapted from allenneuraldynamics/runze-control. It reads `position_steps`, `position_percent`, `position_ul`, `firmware_version` and 4 more; runs `move_to_percent`, `aspirate`, `dispense`, `select_valve_port` and 3 more. `move_to_percent`: move the plunger to an absolute position in percent of full travel. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/allenneuraldynamics__runze-control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/allenneuraldynamics__runze-control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "runze-control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/allenneuraldynamics__runze-control",
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

- **Reads:** `position_steps`, `position_percent`, `position_ul`, `firmware_version`, `address`, `rs232_baudrate`, `motor_status`, `busy`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_to_percent` | Move the plunger to an absolute position in percent of full travel |
| `aspirate` | Withdraw a volume from the current liquid path by moving the plunger |
| `dispense` | Dispense a volume into the current liquid path by moving the plunger |
| `select_valve_port` | Move the integrated rotary valve to one port |
| `reset_syringe` | Home the syringe at the optocoupler position and synchronize the step count to zero |
| `set_speed` | Set the plunger speed as a percentage of the maximum speed for the fitted syringe |
| `stop_pump` | Stop the plunger with the native ForceStop command; it takes no input |

## Source and status

- Upstream: [allenneuraldynamics/runze-control](https://github.com/allenneuraldynamics/runze-control) at `34392b3d9bc0` (MIT); fetch it with `python3 scripts/add_device.py labs/allenneuraldynamics__runze-control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/allenneuraldynamics__runze-control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/allenneuraldynamics__runze-control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/allenneuraldynamics__runze-control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/allenneuraldynamics__runze-control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
