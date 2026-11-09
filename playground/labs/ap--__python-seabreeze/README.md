# Ocean Optics spectrometer (python-seabreeze Spectrometer)

`labs/ap--__python-seabreeze` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Ocean Optics spectrometer (python-seabreeze Spectrometer), adapted from ap--/python-seabreeze. It reads `pixel_count`, `max_intensity`, `serial_number` and `model_name`; runs `measure_intensity` and `set_integration_time`. `measure_intensity`: measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ap--__python-seabreeze
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ap--__python-seabreeze --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "python-seabreeze": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ap--__python-seabreeze",
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

- **Reads:** `pixel_count`, `max_intensity`, `serial_number`, `model_name`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `measure_intensity` | Measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. |
| `set_integration_time` | Set the detector integration time (Spectrometer.integration_time_micros); the value is given in whole microseconds after the conversion from milliseconds |

## Source and status

- Upstream: [ap--/python-seabreeze](https://github.com/ap--/python-seabreeze) at `3de4fdd6bbb5` (MIT); fetch it with `python3 scripts/add_device.py labs/ap--__python-seabreeze` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ap--__python-seabreeze`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ap--__python-seabreeze) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ap--__python-seabreeze/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ap--__python-seabreeze/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
