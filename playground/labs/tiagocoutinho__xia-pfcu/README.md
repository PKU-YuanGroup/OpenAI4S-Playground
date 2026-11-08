# XIA PFCU-4 filter set and shutter controller

`labs/tiagocoutinho__xia-pfcu` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence LGPL-3.0

XIA PFCU-4 filter set and shutter controller, adapted from tiagocoutinho/xia-pfcu. It reads `status`, `identity`, `shutter_state` and `remote_control_enabled`; sets `filter_a`, `filter_b`, `filter_c`, `filter_d` and 3 more; runs `set_state`, `start_exposure` and `close_shutter`. `set_state`: open or close a mechanical or electronic shutter in the optical path, reporting the resulting state and, for an open shutter, the open duration. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/tiagocoutinho__xia-pfcu
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/tiagocoutinho__xia-pfcu --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "xia-pfcu": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/tiagocoutinho__xia-pfcu",
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

- **Reads:** `status`, `identity`, `shutter_state`, `remote_control_enabled`
- **Sets:** `filter_a`, `filter_b`, `filter_c`, `filter_d`, `decimation`, `shutter_enabled`, `remote_control_only`

| Action | What it does |
| --- | --- |
| `set_state` | Open or close a mechanical or electronic shutter in the optical path, reporting the resulting state and, for an open shutter, the open duration. |
| `start_exposure` | Start a fixed-length exposure with the native start_exposure; the duration is in seconds |
| `close_shutter` | Close the shutter (the native close_shutter, the safe state of the optical path); it takes no input |

## Source and status

- Upstream: [tiagocoutinho/xia-pfcu](https://github.com/tiagocoutinho/xia-pfcu) at `ed95e031f718` (LGPL-3.0); fetch it with `python3 scripts/add_device.py labs/tiagocoutinho__xia-pfcu` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/tiagocoutinho__xia-pfcu`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/tiagocoutinho__xia-pfcu) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/tiagocoutinho__xia-pfcu/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/tiagocoutinho__xia-pfcu/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
