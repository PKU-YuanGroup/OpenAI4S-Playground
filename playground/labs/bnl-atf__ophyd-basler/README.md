# Basler camera (ophyd-basler)

`labs/bnl-atf__ophyd-basler` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

Basler camera (ophyd-basler), adapted from bnl-atf/ophyd-basler. It reads `camera_model`, `serial_number`, `user_defined_name`, `image_shape` and 6 more; sets `exposure_time`; runs `capture`. `capture`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/bnl-atf__ophyd-basler
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/bnl-atf__ophyd-basler --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ophyd-basler": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/bnl-atf__ophyd-basler",
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

- **Reads:** `camera_model`, `serial_number`, `user_defined_name`, `image_shape`, `pixel_level_min`, `pixel_level_max`, `active_format`, `payload_size`, `grab_timeout`, `mean`
- **Sets:** `exposure_time`

| Action | What it does |
| --- | --- |
| `capture` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [bnl-atf/ophyd-basler](https://github.com/bnl-atf/ophyd-basler) at `5573459ca330` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/bnl-atf__ophyd-basler` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/bnl-atf__ophyd-basler`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/bnl-atf__ophyd-basler) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/bnl-atf__ophyd-basler/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/bnl-atf__ophyd-basler/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
