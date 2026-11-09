# Toptica DLCpro laser controller (dlccontrol.DLCcontrol)

`labs/asvela__dlc-control` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence MIT

Toptica DLCpro laser controller (dlccontrol.DLCcontrol), adapted from asvela/dlc-control. It reads `emission`, `emission_button`, `wavelength_actual`, `temp_actual` and 3 more; sets `current_enabled`, `wavelength_setpoint`, `temp_setpoint`, `scan_enabled` and 5 more; runs `emission_off`. `emission_off`: disable the laser diode current (the documented emission off control). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/asvela__dlc-control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/asvela__dlc-control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "dlc-control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/asvela__dlc-control",
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

- **Reads:** `emission`, `emission_button`, `wavelength_actual`, `temp_actual`, `scan_output_channel`, `user_level`, `device_limits`
- **Sets:** `current_enabled`, `wavelength_setpoint`, `temp_setpoint`, `scan_enabled`, `scan_frequency`, `scan_amplitude`, `scan_offset`, `scan_start`, `scan_end`

| Action | What it does |
| --- | --- |
| `emission_off` | Disable the laser diode current (the documented emission off control) |

## Source and status

- Upstream: [asvela/dlc-control](https://github.com/asvela/dlc-control) at `eba98c139581` (MIT); fetch it with `python3 scripts/add_device.py labs/asvela__dlc-control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/asvela__dlc-control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/asvela__dlc-control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/asvela__dlc-control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/asvela__dlc-control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
