# IDS uEye camera (pydcu ueye.camera)

`labs/bernardokyotoku__pydcu` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

IDS uEye camera (pydcu ueye.camera), adapted from bernardokyotoku/pydcu. It sets `width`, `height`, `image_x` and `image_y`; runs `capture`. `capture`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/bernardokyotoku__pydcu
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/bernardokyotoku__pydcu --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pydcu": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/bernardokyotoku__pydcu",
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
- **Sets:** `width`, `height`, `image_x`, `image_y`

| Action | What it does |
| --- | --- |
| `capture` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [bernardokyotoku/pydcu](https://github.com/bernardokyotoku/pydcu) at `ff9557e701e3` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/bernardokyotoku__pydcu` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/bernardokyotoku__pydcu`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/bernardokyotoku__pydcu) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/bernardokyotoku__pydcu/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/bernardokyotoku__pydcu/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
