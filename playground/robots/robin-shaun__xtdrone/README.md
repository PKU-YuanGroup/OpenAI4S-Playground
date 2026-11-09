# XTDrone typhoon_h480_0 position bridge

`robots/robin-shaun__xtdrone` · Mobile robots · simulation · risk R2 · licence MIT

XTDrone typhoon_h480_0 position bridge, adapted from robin-shaun/xtdrone. It reads `read_target` and `read_position`; runs `publish_position_setpoint`. `publish_position_setpoint`: publish one map-frame local position setpoint to MAVROS; the receipt reports the values handed to rosbridge and is transmission only, not arrival or a stop. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/robin-shaun__xtdrone
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/robin-shaun__xtdrone --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "xtdrone": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/robin-shaun__xtdrone",
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

- **Reads:** `read_target`, `read_position`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_position_setpoint` | Publish one map-frame local position setpoint to MAVROS; the receipt reports the values handed to rosbridge and is transmission only, not arrival or a stop |

## Source and status

- Upstream: [robin-shaun/xtdrone](https://github.com/robin-shaun/xtdrone) at `671f3d45b22b` (MIT); fetch it with `python3 scripts/add_device.py robots/robin-shaun__xtdrone` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/robin-shaun__xtdrone`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/robin-shaun__xtdrone) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/robin-shaun__xtdrone/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/robin-shaun__xtdrone/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
