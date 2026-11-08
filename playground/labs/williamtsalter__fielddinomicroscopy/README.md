# Dino-Lite AM7515 USB microscope (dnx64.DNX64)

`labs/williamtsalter__fielddinomicroscopy` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Dino-Lite AM7515 USB microscope (dnx64.DNX64), adapted from williamtsalter/fielddinomicroscopy. It reads `device_name` and `device_id`; sets `exposure_value`, `ae_target` and `auto_exposure`; runs `set_led`, `set_flc_level` and `switch_off_illumination`. `set_led`: turn the microscope LED on or off (SetLEDState). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/williamtsalter__fielddinomicroscopy
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/williamtsalter__fielddinomicroscopy --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "fielddinomicroscopy": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/williamtsalter__fielddinomicroscopy",
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

- **Reads:** `device_name`, `device_id`
- **Sets:** `exposure_value`, `ae_target`, `auto_exposure`

| Action | What it does |
| --- | --- |
| `set_led` | Turn the microscope LED on or off (SetLEDState) |
| `set_flc_level` | Set the FLC level (SetFLCLevel) |
| `switch_off_illumination` | Turn the LED off (SetLEDState 0), the safe state; it takes no input |

## Source and status

- Upstream: [williamtsalter/fielddinomicroscopy](https://github.com/williamtsalter/fielddinomicroscopy) at `e67297f1822d` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/williamtsalter__fielddinomicroscopy` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/williamtsalter__fielddinomicroscopy`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/williamtsalter__fielddinomicroscopy) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/williamtsalter__fielddinomicroscopy/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/williamtsalter__fielddinomicroscopy/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
