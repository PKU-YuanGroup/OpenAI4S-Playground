# fibsem-os remote fluorescence microscope

`labs/fibsem-os__fibsem-os` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

fibsem-os remote fluorescence microscope, adapted from fibsem-os/fibsem-os. It reads `is_acquiring`, `is_interactive` and `acquiring_reason`; sets `exposure_time`, `binning`, `gain`, `channel_name` and 1 more; runs `start_acquisition` and `stop_acquisition`. `start_acquisition`: start continuous live acquisition of the fluorescence microscope. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/fibsem-os__fibsem-os
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/fibsem-os__fibsem-os --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "fibsem-os": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/fibsem-os__fibsem-os",
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

- **Reads:** `is_acquiring`, `is_interactive`, `acquiring_reason`
- **Sets:** `exposure_time`, `binning`, `gain`, `channel_name`, `channel_color`

| Action | What it does |
| --- | --- |
| `start_acquisition` | Start continuous live acquisition of the fluorescence microscope |
| `stop_acquisition` | Stop continuous live acquisition (the native stop and the safe state) |

## Source and status

- Upstream: [fibsem-os/fibsem-os](https://github.com/fibsem-os/fibsem-os) at `8bd5dc731f52` (MIT); fetch it with `python3 scripts/add_device.py labs/fibsem-os__fibsem-os` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/fibsem-os__fibsem-os`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/fibsem-os__fibsem-os) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/fibsem-os__fibsem-os/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/fibsem-os__fibsem-os/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
