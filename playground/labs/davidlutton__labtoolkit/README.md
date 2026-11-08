# Agilent PSA spectrum analyser (labtoolkit AgilentE44nn)

`labs/davidlutton__labtoolkit` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Agilent PSA spectrum analyser (labtoolkit AgilentE44nn), adapted from davidlutton/labtoolkit. It reads `identification`; sets `frequency_center`, `frequency_span`, `sweep_points`, `resolution_bandwidth` and 2 more; runs `stop_sweep`. `stop_sweep`: stop continuous sweeping (the native stop, INIT:CONTinuous OFF); it takes no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/davidlutton__labtoolkit
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/davidlutton__labtoolkit --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "labtoolkit": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/davidlutton__labtoolkit",
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

- **Reads:** `identification`
- **Sets:** `frequency_center`, `frequency_span`, `sweep_points`, `resolution_bandwidth`, `video_bandwidth`, `continuous`

| Action | What it does |
| --- | --- |
| `stop_sweep` | Stop continuous sweeping (the native stop, INIT:CONTinuous OFF); it takes no input |

## Source and status

- Upstream: [davidlutton/labtoolkit](https://github.com/davidlutton/labtoolkit) at `1c27b3549000` (MIT); fetch it with `python3 scripts/add_device.py labs/davidlutton__labtoolkit` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/davidlutton__labtoolkit`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/davidlutton__labtoolkit) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/davidlutton__labtoolkit/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/davidlutton__labtoolkit/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
