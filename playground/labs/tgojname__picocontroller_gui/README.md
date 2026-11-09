# Newport 8742 picomotor controller

`labs/tgojname__picocontroller_gui` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Newport 8742 picomotor controller, adapted from tgojname/picocontroller_gui. It reads `version`, `motor_types` and `motion_done`; runs `jog_axis` and `stop_motion`. `jog_axis`: set one channel's velocity and start a continuous jog when the channel is motion done. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/tgojname__picocontroller_gui
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/tgojname__picocontroller_gui --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "picocontroller_gui": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/tgojname__picocontroller_gui",
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

- **Reads:** `version`, `motor_types`, `motion_done`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `jog_axis` | Set one channel's velocity and start a continuous jog when the channel is motion done |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [tgojname/picocontroller_gui](https://github.com/tgojname/picocontroller_gui) at `82a5f65663c9` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/tgojname__picocontroller_gui` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/tgojname__picocontroller_gui`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/tgojname__picocontroller_gui) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/tgojname__picocontroller_gui/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/tgojname__picocontroller_gui/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
