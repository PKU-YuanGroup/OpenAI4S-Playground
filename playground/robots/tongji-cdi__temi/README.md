# Temi robot (temi.api:Temi)

`robots/tongji-cdi__temi` · Mobile robots · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Temi robot (temi.api:Temi), adapted from tongji-cdi/temi. It runs `goto`, `speak`, `ask`, `interface` and 1 more. `goto`: go to a saved location and report whether Temi says it reached it. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/tongji-cdi__temi
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/tongji-cdi__temi --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "temi": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/tongji-cdi__temi",
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
- **Sets:** —

| Action | What it does |
| --- | --- |
| `goto` | Go to a saved location and report whether Temi says it reached it |
| `speak` | Say a sentence out loud |
| `ask` | Ask a question, wait for the recognized answer and return it |
| `interface` | Show a URL on Temi's screen |
| `stop_motion` | Stop all motion with the Temi stop command; it takes no input |

## Source and status

- Upstream: [tongji-cdi/temi](https://github.com/tongji-cdi/temi) at `ec0a395405df` (MIT); fetch it with `python3 scripts/add_device.py robots/tongji-cdi__temi` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/tongji-cdi__temi`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/tongji-cdi__temi) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/tongji-cdi__temi/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/tongji-cdi__temi/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
