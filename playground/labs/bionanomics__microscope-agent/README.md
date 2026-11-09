# Baumer VCXU-23C GenICam camera

`labs/bionanomics__microscope-agent` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Baumer VCXU-23C GenICam camera, adapted from bionanomics/microscope-agent. It reads `exposure_time_range_us`, `gain_range`, `pixel_format` and `balance_white_auto`; sets `exposure_time_us` and `gain`; runs `capture`. `capture`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/bionanomics__microscope-agent
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/bionanomics__microscope-agent --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "microscope-agent": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/bionanomics__microscope-agent",
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

- **Reads:** `exposure_time_range_us`, `gain_range`, `pixel_format`, `balance_white_auto`
- **Sets:** `exposure_time_us`, `gain`

| Action | What it does |
| --- | --- |
| `capture` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [bionanomics/microscope-agent](https://github.com/bionanomics/microscope-agent) at `3aef391397de` (MIT); fetch it with `python3 scripts/add_device.py labs/bionanomics__microscope-agent` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/bionanomics__microscope-agent`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/bionanomics__microscope-agent) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/bionanomics__microscope-agent/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/bionanomics__microscope-agent/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
