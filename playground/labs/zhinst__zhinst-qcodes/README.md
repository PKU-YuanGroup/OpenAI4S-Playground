# Zurich Instruments PQSC trigger distributor (zhinst-qcodes)

`labs/zhinst__zhinst-qcodes` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Zurich Instruments PQSC trigger distributor (zhinst-qcodes), adapted from zhinst/zhinst-qcodes. It reads `device_type`, `serial`, `firmware`, `streaming_nodes` and 1 more; runs `trigger` and `wait_done`. `trigger`: arm, run, stop or factory-reset the PQSC trigger generation. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/zhinst__zhinst-qcodes
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/zhinst__zhinst-qcodes --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "zhinst-qcodes": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/zhinst__zhinst-qcodes",
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

- **Reads:** `device_type`, `serial`, `firmware`, `streaming_nodes`, `ref_clock_locked`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `trigger` | Arm, run, stop or factory-reset the PQSC trigger generation |
| `wait_done` | Wait until trigger generation and feedback processing is done |

## Source and status

- Upstream: [zhinst/zhinst-qcodes](https://github.com/zhinst/zhinst-qcodes) at `042dd17a5bf4` (MIT); fetch it with `python3 scripts/add_device.py labs/zhinst__zhinst-qcodes` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/zhinst__zhinst-qcodes`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/zhinst__zhinst-qcodes) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/zhinst__zhinst-qcodes/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/zhinst__zhinst-qcodes/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
