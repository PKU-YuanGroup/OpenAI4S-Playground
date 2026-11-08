# Newport 1918-C optical power meter (newport_1918c.Newport_1918c)

`labs/plasmon360__python_newport_1918_powermeter` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Newport 1918-C optical power meter (newport_1918c.Newport_1918c), adapted from plasmon360/python_newport_1918_powermeter. It reads `serial_number` and `model_number`; sets `wavelength_nm`; runs `measure_intensity`. `measure_intensity`: measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/plasmon360__python_newport_1918_powermeter
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/plasmon360__python_newport_1918_powermeter --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "python_newport_1918_powermeter": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/plasmon360__python_newport_1918_powermeter",
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

- **Reads:** `serial_number`, `model_number`
- **Sets:** `wavelength_nm`

| Action | What it does |
| --- | --- |
| `measure_intensity` | Measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. |

## Source and status

- Upstream: [plasmon360/python_newport_1918_powermeter](https://github.com/plasmon360/python_newport_1918_powermeter) at `5c8ae02c1f9d` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/plasmon360__python_newport_1918_powermeter` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/plasmon360__python_newport_1918_powermeter`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/plasmon360__python_newport_1918_powermeter) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/plasmon360__python_newport_1918_powermeter/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/plasmon360__python_newport_1918_powermeter/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
