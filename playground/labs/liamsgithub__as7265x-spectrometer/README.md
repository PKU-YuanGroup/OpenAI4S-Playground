# SparkFun Triad AS7265x spectrometer

`labs/liamsgithub__as7265x-spectrometer` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

SparkFun Triad AS7265x spectrometer, adapted from liamsgithub/as7265x-spectrometer. It reads `board_present`, `hardware_version`, `temperatures` and `measure_intensity`; sets `integration_time_register`, `gain`, `led_drive_current`, `blue_led` and 1 more; runs `read_spectrum`, `factory_reset` and `leds_off`. `read_spectrum`: read all 18 raw and all 18 calibrated channel values in the ascending-frequency order of the clone. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/liamsgithub__as7265x-spectrometer
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/liamsgithub__as7265x-spectrometer --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "as7265x-spectrometer": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/liamsgithub__as7265x-spectrometer",
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

- **Reads:** `board_present`, `hardware_version`, `temperatures`, `measure_intensity`
- **Sets:** `integration_time_register`, `gain`, `led_drive_current`, `blue_led`, `shutter_leds`

| Action | What it does |
| --- | --- |
| `read_spectrum` | Read all 18 raw and all 18 calibrated channel values in the ascending-frequency order of the clone |
| `factory_reset` | Reset all three AS7265x devices to their factory defaults with the native init and report whether the board is present afterwards |
| `leds_off` | Turn off the master blue LED and the shutter LEDs of all three devices (the safe state) and read them back; it takes no input |

## Source and status

- Upstream: [liamsgithub/as7265x-spectrometer](https://github.com/liamsgithub/as7265x-spectrometer) at `9b0ce11be6b9` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/liamsgithub__as7265x-spectrometer` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/liamsgithub__as7265x-spectrometer`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/liamsgithub__as7265x-spectrometer) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/liamsgithub__as7265x-spectrometer/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/liamsgithub__as7265x-spectrometer/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
