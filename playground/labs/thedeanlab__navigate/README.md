# ASI MS-2000 motorised stage (navigate.MS2000Stage)

`labs/thedeanlab__navigate` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause-Clear

ASI MS-2000 motorised stage (navigate.MS2000Stage), adapted from thedeanlab/navigate. It reads `x_position`, `y_position` and `z_position`; runs `move_axis_absolute` and `stop_scan`. `move_axis_absolute`: move one stage axis to an absolute position in micrometres. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/thedeanlab__navigate
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/thedeanlab__navigate --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "navigate": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/thedeanlab__navigate",
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

- **Reads:** `x_position`, `y_position`, `z_position`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_axis_absolute` | Move one stage axis to an absolute position in micrometres |
| `stop_scan` | Stop a running line scan (the native scan stop); it takes no input |

## Source and status

- Upstream: [thedeanlab/navigate](https://github.com/thedeanlab/navigate) at `da14920d7b40` (BSD-3-Clause-Clear); fetch it with `python3 scripts/add_device.py labs/thedeanlab__navigate` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/thedeanlab__navigate`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/thedeanlab__navigate) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/thedeanlab__navigate/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/thedeanlab__navigate/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
