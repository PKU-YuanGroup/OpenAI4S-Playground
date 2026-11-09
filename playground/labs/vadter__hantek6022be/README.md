# Hantek 6022BE USB oscilloscope (pyhantek6022BE.Hantek)

`labs/vadter__hantek6022be` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Hantek 6022BE USB oscilloscope (pyhantek6022BE.Hantek), adapted from vadter/hantek6022be. It reads `acquisition`; sets `sample_rate`, `ch1_vdiv` and `ch2_vdiv`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/vadter__hantek6022be
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/vadter__hantek6022be --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "hantek6022be": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/vadter__hantek6022be",
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

- **Reads:** `acquisition`
- **Sets:** `sample_rate`, `ch1_vdiv`, `ch2_vdiv`

## Source and status

- Upstream: [vadter/hantek6022be](https://github.com/vadter/hantek6022be) at `548ff2398404` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/vadter__hantek6022be` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/vadter__hantek6022be`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/vadter__hantek6022be) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/vadter__hantek6022be/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/vadter__hantek6022be/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
