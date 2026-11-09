# Chilas Atlas/Comet tunable laser (pychilaslasers.laser:Laser)

`labs/chilaslasers__pychilaslasers` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence Apache-2.0

Chilas Atlas/Comet tunable laser (pychilaslasers.laser:Laser), adapted from chilaslasers/pychilaslasers. It reads `model`, `calibrated`, `diode_enabled`, `diode_current` and 4 more; sets `system_state`; runs `turn_on`, `turn_off`, `trigger_pulse`, `set_diode_current` and 1 more. `turn_on`: enable the laser system output (SYST:STAT 1). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/chilaslasers__pychilaslasers
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/chilaslasers__pychilaslasers --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pychilaslasers": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/chilaslasers__pychilaslasers",
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

- **Reads:** `model`, `calibrated`, `diode_enabled`, `diode_current`, `diode_max_current`, `tec_temperature`, `tec_target`, `tec_current`
- **Sets:** `system_state`

| Action | What it does |
| --- | --- |
| `turn_on` | Enable the laser system output (SYST:STAT 1) |
| `turn_off` | Disable the laser system output and the diode emission (SYST:STAT 0, LSR:STAT 0); takes no input |
| `trigger_pulse` | Send one trigger pulse (DRV:CYC:TRIG 1 then DRV:CYC:TRIG 0); takes no input |
| `set_diode_current` | Set the diode drive current in mA (LSR:ILEV) |
| `set_tec_target` | Set the TEC target temperature in degrees Celsius (TEC:TTGT) |

## Source and status

- Upstream: [chilaslasers/pychilaslasers](https://github.com/chilaslasers/pychilaslasers) at `ec9470e0042c` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/chilaslasers__pychilaslasers` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/chilaslasers__pychilaslasers`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/chilaslasers__pychilaslasers) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/chilaslasers__pychilaslasers/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/chilaslasers__pychilaslasers/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
