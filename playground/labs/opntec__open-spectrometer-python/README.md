# TCD1304 linear CCD on a PSLab (open-spectrometer-python)

`labs/opntec__open-spectrometer-python` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence Apache-2.0

TCD1304 linear CCD on a PSLab (open-spectrometer-python), adapted from opntec/open-spectrometer-python. It reads `master_clock_frequency`; sets `integration_time`; runs `measure_intensity` and `power_on`. `measure_intensity`: measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/opntec__open-spectrometer-python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/opntec__open-spectrometer-python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "open-spectrometer-python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/opntec__open-spectrometer-python",
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

- **Reads:** `master_clock_frequency`
- **Sets:** `integration_time`

| Action | What it does |
| --- | --- |
| `measure_intensity` | Measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. |
| `power_on` | Power the CCD on again after a safety reset (the declared re-enable): poweron() sets the PV1 supply to 5 V; it takes no input, is refused while the e-stop is latched and is never run by the reset |

## Source and status

- Upstream: [opntec/open-spectrometer-python](https://github.com/opntec/open-spectrometer-python) at `a15b67d9afb4` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/opntec__open-spectrometer-python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/opntec__open-spectrometer-python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/opntec__open-spectrometer-python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/opntec__open-spectrometer-python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/opntec__open-spectrometer-python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
