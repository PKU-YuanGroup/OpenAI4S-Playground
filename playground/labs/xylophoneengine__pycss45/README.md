# Gigahertz-Optik CSS45 spectral sensor (pycss45.CSS45)

`labs/xylophoneengine__pycss45` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence MIT

Gigahertz-Optik CSS45 spectral sensor (pycss45.CSS45), adapted from xylophoneengine/pycss45. It reads `serial_number`, `firmware_version`, `status`, `temperature` and 7 more; runs `measure_spectrum`. `measure_spectrum`: acquire an optical or mass spectrum over a declared wavelength or mass range and return the axis and intensity arrays, or an artifact reference for large spectra. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/xylophoneengine__pycss45
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/xylophoneengine__pycss45 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pycss45": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/xylophoneengine__pycss45",
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

- **Reads:** `serial_number`, `firmware_version`, `status`, `temperature`, `cct`, `photopic`, `par`, `radiometric_unit`, `last_integration_time`, `wavelength_start`, `wavelength_end`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `measure_spectrum` | Acquire an optical or mass spectrum over a declared wavelength or mass range and return the axis and intensity arrays, or an artifact reference for large spectra. |

## Source and status

- Upstream: [xylophoneengine/pycss45](https://github.com/xylophoneengine/pycss45) at `e4364bae4d88` (MIT); fetch it with `python3 scripts/add_device.py labs/xylophoneengine__pycss45` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/xylophoneengine__pycss45`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/xylophoneengine__pycss45) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/xylophoneengine__pycss45/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/xylophoneengine__pycss45/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
