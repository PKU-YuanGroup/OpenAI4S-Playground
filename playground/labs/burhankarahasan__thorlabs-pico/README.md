# Pi Pico W stepper rotation axis (stepper_controller.PicoStepperController)

`labs/burhankarahasan__thorlabs-pico` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Pi Pico W stepper rotation axis (stepper_controller.PicoStepperController), adapted from burhankarahasan/thorlabs-pico. It reads `current_rps` and `position_steps`; sets `target_rps`; runs `stop_motion`, `enable_motor`, `disable_motor` and `set_ramp_rate`. `stop_motion`: stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/burhankarahasan__thorlabs-pico
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/burhankarahasan__thorlabs-pico --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "thorlabs-pico": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/burhankarahasan__thorlabs-pico",
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

- **Reads:** `current_rps`, `position_steps`
- **Sets:** `target_rps`

| Action | What it does |
| --- | --- |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |
| `enable_motor` | Enable the stepper motor driver (the native ENABLE) |
| `disable_motor` | Disable the stepper motor driver; the upstream docstring says this cuts power (DISABLE) |
| `set_ramp_rate` | Set the acceleration/deceleration rate in steps/sec^2 (the native RAMP) |

## Source and status

- Upstream: [burhankarahasan/thorlabs-pico](https://github.com/burhankarahasan/thorlabs-pico) at `91898e3a55a9` (MIT); fetch it with `python3 scripts/add_device.py labs/burhankarahasan__thorlabs-pico` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/burhankarahasan__thorlabs-pico`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/burhankarahasan__thorlabs-pico) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/burhankarahasan__thorlabs-pico/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/burhankarahasan__thorlabs-pico/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
