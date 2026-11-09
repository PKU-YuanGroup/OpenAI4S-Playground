# Rohde & Schwarz FSWP phase noise analyzer (rssd PNA class)

`labs/mclim9__rssd` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Rohde & Schwarz FSWP phase noise analyzer (rssd PNA class), adapted from mclim9/rssd. It reads `channels`, `sweep_time_s`, `sweep_type` and `reference_level_db`; sets `attenuation_db`, `center_freq_hz` and `sweep_points`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/mclim9__rssd
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/mclim9__rssd --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "rssd": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/mclim9__rssd",
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

- **Reads:** `channels`, `sweep_time_s`, `sweep_type`, `reference_level_db`
- **Sets:** `attenuation_db`, `center_freq_hz`, `sweep_points`

## Source and status

- Upstream: [mclim9/rssd](https://github.com/mclim9/rssd) at `7b040ee12841` (MIT); fetch it with `python3 scripts/add_device.py labs/mclim9__rssd` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/mclim9__rssd`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/mclim9__rssd) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/mclim9__rssd/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/mclim9__rssd/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
