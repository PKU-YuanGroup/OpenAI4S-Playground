# HAMEG HM1507 oscilloscope (serial remote control)

`labs/aakafosfor__hameg_hm1507` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

HAMEG HM1507 oscilloscope (serial remote control), adapted from aakafosfor/hameg_hm1507. It sets `timebase` and `channel`; runs `autoset`. `autoset`: run the scope's automatic setup (the upstream AUTOSET command). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/aakafosfor__hameg_hm1507
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/aakafosfor__hameg_hm1507 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "hameg_hm1507": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/aakafosfor__hameg_hm1507",
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

- **Reads:** —
- **Sets:** `timebase`, `channel`

| Action | What it does |
| --- | --- |
| `autoset` | Run the scope's automatic setup (the upstream AUTOSET command) |

## Source and status

- Upstream: [aakafosfor/hameg_hm1507](https://github.com/aakafosfor/hameg_hm1507) at `0a03fdc25414` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/aakafosfor__hameg_hm1507` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/aakafosfor__hameg_hm1507`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/aakafosfor__hameg_hm1507) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/aakafosfor__hameg_hm1507/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/aakafosfor__hameg_hm1507/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
