# Thorlabs Elliptec rotation stage (elliptec.rotation.Motor)

`labs/cdbaird__tl-rotation-control` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Thorlabs Elliptec rotation stage (elliptec.rotation.Motor), adapted from cdbaird/tl-rotation-control. It reads `status_code` and `serial_number`; sets `position` and `step_size`; runs `home`. `home`: home the rotation stage. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/cdbaird__tl-rotation-control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/cdbaird__tl-rotation-control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tl-rotation-control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/cdbaird__tl-rotation-control",
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

- **Reads:** `status_code`, `serial_number`
- **Sets:** `position`, `step_size`

| Action | What it does |
| --- | --- |
| `home` | Home the rotation stage |

## Source and status

- Upstream: [cdbaird/tl-rotation-control](https://github.com/cdbaird/tl-rotation-control) at `759dc3fc58ef` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/cdbaird__tl-rotation-control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/cdbaird__tl-rotation-control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/cdbaird__tl-rotation-control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/cdbaird__tl-rotation-control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/cdbaird__tl-rotation-control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
