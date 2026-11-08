# Dino-Lite UVC LED control (dinoliteuvccontrol.DinoLiteUVCControl)

`labs/miked63017__dinolite_uvc_led_control` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Dino-Lite UVC LED control (dinoliteuvccontrol.DinoLiteUVCControl), adapted from miked63017/dinolite_uvc_led_control. It reads `main_led_on`, `flc_on`, `flc_brightness`, `auto_exposure` and 3 more; runs `set_illumination`, `set_flc_brightness`, `toggle_flc_led`, `toggle_auto_exposure` and 2 more. `set_illumination`: turn the main LED or the FLC illumination on or off. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/miked63017__dinolite_uvc_led_control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/miked63017__dinolite_uvc_led_control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "dinolite_uvc_led_control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/miked63017__dinolite_uvc_led_control",
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

- **Reads:** `main_led_on`, `flc_on`, `flc_brightness`, `auto_exposure`, `exposure_time`, `video_device`, `product_id`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_illumination` | Turn the main LED or the FLC illumination on or off |
| `set_flc_brightness` | Set the FLC brightness level (0 to 6); FLC is switched on first when it is off |
| `toggle_flc_led` | Toggle one of the four FLC LEDs; FLC is switched on first when it is off |
| `toggle_auto_exposure` | Toggle automatic exposure on the microscope |
| `step_exposure` | Move one step in the device's exposure table; auto exposure is switched off first |
| `illumination_off` | Switch all illumination off (the safe state); it takes no input |

## Source and status

- Upstream: [miked63017/dinolite_uvc_led_control](https://github.com/miked63017/dinolite_uvc_led_control) at `f70a4cedfa1f` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/miked63017__dinolite_uvc_led_control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/miked63017__dinolite_uvc_led_control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/miked63017__dinolite_uvc_led_control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/miked63017__dinolite_uvc_led_control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/miked63017__dinolite_uvc_led_control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
