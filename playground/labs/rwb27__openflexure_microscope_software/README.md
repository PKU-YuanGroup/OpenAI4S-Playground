# OpenFlexure Microscope (openflexure_microscope.microscope:Microscope)

`labs/rwb27__openflexure_microscope_software` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

OpenFlexure Microscope (openflexure_microscope.microscope:Microscope), adapted from rwb27/openflexure_microscope_software. It reads `resolution`, `shutter_speed` and `awb_mode`; sets `zoom`; runs `autofocus_scan`. `autofocus_scan`: run the microscope's autofocus over stage z positions and report the sharpness at each. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/rwb27__openflexure_microscope_software
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/rwb27__openflexure_microscope_software --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "openflexure_microscope_software": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/rwb27__openflexure_microscope_software",
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

- **Reads:** `resolution`, `shutter_speed`, `awb_mode`
- **Sets:** `zoom`

| Action | What it does |
| --- | --- |
| `autofocus_scan` | Run the microscope's autofocus over stage z positions and report the sharpness at each |

## Source and status

- Upstream: [rwb27/openflexure_microscope_software](https://github.com/rwb27/openflexure_microscope_software) at `991e1b72b94d` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/rwb27__openflexure_microscope_software` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/rwb27__openflexure_microscope_software`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/rwb27__openflexure_microscope_software) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/rwb27__openflexure_microscope_software/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/rwb27__openflexure_microscope_software/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
