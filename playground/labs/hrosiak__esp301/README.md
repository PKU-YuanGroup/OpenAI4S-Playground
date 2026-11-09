# Newport ESP 301 stepper motion controller (esp.esp)

`labs/hrosiak__esp301` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Newport ESP 301 stepper motion controller (esp.esp), adapted from hrosiak/esp301. It reads `position` and `last_error`; sets `target_position`; runs `reset_axis`. `reset_axis`: reset the served axis with the upstream reset (OR, WS0) and report whether the controller returns no error afterwards. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/hrosiak__esp301
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/hrosiak__esp301 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "esp301": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/hrosiak__esp301",
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

- **Reads:** `position`, `last_error`
- **Sets:** `target_position`

| Action | What it does |
| --- | --- |
| `reset_axis` | Reset the served axis with the upstream reset (OR, WS0) and report whether the controller returns no error afterwards |

## Source and status

- Upstream: [hrosiak/esp301](https://github.com/hrosiak/esp301) at `b0d1921faf37` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/hrosiak__esp301` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/hrosiak__esp301`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/hrosiak__esp301) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/hrosiak__esp301/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/hrosiak__esp301/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
