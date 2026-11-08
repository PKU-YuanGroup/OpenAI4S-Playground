# RP2DAQ board (rp2daq.Rp2daq)

`labs/filipdominec__rp2daq` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

RP2DAQ board (rp2daq.Rp2daq), adapted from filipdominec/rp2daq. It reads `adc_mean`, `stepper_position` and `stepper_moving`; sets `gpio_pin` and `gpio_level`; runs `adc_sample`, `pwm_set`, `stepper_init`, `stepper_move` and 1 more. `adc_sample`: capture one ADC block and return the mean raw count. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/filipdominec__rp2daq
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/filipdominec__rp2daq --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "rp2daq": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/filipdominec__rp2daq",
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

- **Reads:** `adc_mean`, `stepper_position`, `stepper_moving`
- **Sets:** `gpio_pin`, `gpio_level`

| Action | What it does |
| --- | --- |
| `adc_sample` | Capture one ADC block and return the mean raw count |
| `pwm_set` | Configure a PWM slice and set the duty value of one GPIO |
| `stepper_init` | Initialize one A4988-compatible stepper on two GPIO pins |
| `stepper_move` | Move one initialized stepper to an absolute or relative nanostep position |
| `drive_safe_state` | Stop every initialized stepper at its current position, zero PWM and drive configured GPIO outputs low |

## Source and status

- Upstream: [filipdominec/rp2daq](https://github.com/filipdominec/rp2daq) at `7744f34811d1` (MIT); fetch it with `python3 scripts/add_device.py labs/filipdominec__rp2daq` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/filipdominec__rp2daq`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/filipdominec__rp2daq) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/filipdominec__rp2daq/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/filipdominec__rp2daq/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
