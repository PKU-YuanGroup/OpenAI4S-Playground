# SpectraMax plate reader (spectramax.Spectramax)

`labs/gormleylab__spectramax` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

SpectraMax plate reader (spectramax.Spectramax), adapted from gormleylab/spectramax. It reads `instrument_status` and `plate_data`; runs `set_incubator_temperature`, `read_uvvis` and `incubator_off`. `set_incubator_temperature`: set the incubator temperature through SoftMax Pro; 0 turns the incubator off. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/gormleylab__spectramax
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/gormleylab__spectramax --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "spectramax": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/gormleylab__spectramax",
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

- **Reads:** `instrument_status`, `plate_data`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_incubator_temperature` | Set the incubator temperature through SoftMax Pro; 0 turns the incubator off |
| `read_uvvis` | Run a UV-Vis read from a SoftMax Pro .spr method and export .sda, .csv and .xml files |
| `incubator_off` | Turn the incubator off with set_temperature(0), the documented off state; no input |

## Source and status

- Upstream: [gormleylab/spectramax](https://github.com/gormleylab/spectramax) at `7940d4064663` (MIT); fetch it with `python3 scripts/add_device.py labs/gormleylab__spectramax` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/gormleylab__spectramax`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/gormleylab__spectramax) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/gormleylab__spectramax/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/gormleylab__spectramax/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
