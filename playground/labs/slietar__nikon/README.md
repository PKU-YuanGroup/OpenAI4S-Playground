# Nikon Ti2-E microscope (nikon.microscope:MicroscopeDevice)

`labs/slietar__nikon` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence EUPL-1.2

Nikon Ti2-E microscope (nikon.microscope:MicroscopeDevice), adapted from slietar/nikon. It reads `firmware_version` and `zoom`; sets `x`, `y`, `z`, `condenser` and 6 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/slietar__nikon
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/slietar__nikon --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "nikon": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/slietar__nikon",
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

- **Reads:** `firmware_version`, `zoom`
- **Sets:** `x`, `y`, `z`, `condenser`, `dia`, `filter`, `light`, `objective`, `optical_path`, `shutter`

## Source and status

- Upstream: [slietar/nikon](https://github.com/slietar/nikon) at `d53b4e261ae4` (EUPL-1.2); fetch it with `python3 scripts/add_device.py labs/slietar__nikon` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/slietar__nikon`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/slietar__nikon) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/slietar__nikon/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/slietar__nikon/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
