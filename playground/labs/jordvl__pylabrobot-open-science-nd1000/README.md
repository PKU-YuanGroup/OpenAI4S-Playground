# Thermo Fisher NanoDrop 1000 spectrophotometer (Code/nanodrop.py:NanoDrop1000)

`labs/jordvl__pylabrobot-open-science-nd1000` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Thermo Fisher NanoDrop 1000 spectrophotometer (Code/nanodrop.py:NanoDrop1000), adapted from jordvl/pylabrobot-open-science-nd1000. It reads `raw_spectrum`; sets `lamp`, `magnet` and `integration_time`; runs `measure_spectrum` and `take_blank`. `measure_spectrum`: acquire an optical or mass spectrum over a declared wavelength or mass range and return the axis and intensity arrays, or an artifact reference for large spectra. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/jordvl__pylabrobot-open-science-nd1000
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/jordvl__pylabrobot-open-science-nd1000 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pylabrobot-open-science-nd1000": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/jordvl__pylabrobot-open-science-nd1000",
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

- **Reads:** `raw_spectrum`
- **Sets:** `lamp`, `magnet`, `integration_time`

| Action | What it does |
| --- | --- |
| `measure_spectrum` | Acquire an optical or mass spectrum over a declared wavelength or mass range and return the axis and intensity arrays, or an artifact reference for large spectra. |
| `take_blank` | Acquire the dark and blank baselines the absorbance measurement needs |

## Source and status

- Upstream: [jordvl/pylabrobot-open-science-nd1000](https://github.com/jordvl/pylabrobot-open-science-nd1000) at `db60b6649423` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/jordvl__pylabrobot-open-science-nd1000` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/jordvl__pylabrobot-open-science-nd1000`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/jordvl__pylabrobot-open-science-nd1000) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/jordvl__pylabrobot-open-science-nd1000/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/jordvl__pylabrobot-open-science-nd1000/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
