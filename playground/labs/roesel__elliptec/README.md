# Thorlabs Elliptec shutter (elliptec.Shutter)

`labs/roesel__elliptec` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

Thorlabs Elliptec shutter (elliptec.Shutter), adapted from roesel/elliptec. It reads `is_open`, `is_closed` and `slot`; runs `set_state`, `home_shutter`, `move_to_slot` and `close_shutter`. `set_state`: open or close a mechanical or electronic shutter in the optical path, reporting the resulting state and, for an open shutter, the open duration. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/roesel__elliptec
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/roesel__elliptec --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "elliptec": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/roesel__elliptec",
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

- **Reads:** `is_open`, `is_closed`, `slot`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_state` | Open or close a mechanical or electronic shutter in the optical path, reporting the resulting state and, for an open shutter, the open duration. |
| `home_shutter` | Home the shutter slider (Shutter.home) so that its slot positions are referenced; the device drives to its home position |
| `move_to_slot` | Move the slider to a slot with Shutter.set_slot: slot 1 or slot 2 of a non-inverted shutter |
| `close_shutter` | Close the shutter (the native Shutter.close, the safe state of the optical path); it takes no input |

## Source and status

- Upstream: [roesel/elliptec](https://github.com/roesel/elliptec) at `5f86ca595f80` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/roesel__elliptec` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/roesel__elliptec`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/roesel__elliptec) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/roesel__elliptec/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/roesel__elliptec/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
