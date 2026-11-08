# Astrobee free-flyer (ROS 1)

`robots/nasa__astrobee` · Mobile robots · simulation · risk R2 · licence Apache-2.0

Astrobee free-flyer (ROS 1), adapted from nasa/astrobee. It reads `commanded_segment_stamp_nsecs`; runs `move` and `stop`. `move`: move through world-frame poses; return the Motion action's application result. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/nasa__astrobee
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/nasa__astrobee --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "astrobee": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/nasa__astrobee",
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

- **Reads:** `commanded_segment_stamp_nsecs`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move` | Move through world-frame poses; return the Motion action's application result |
| `stop` | Command the GNC controller's STOP and confirm only after the native Control action reports SUCCESS |

## Source and status

- Upstream: [nasa/astrobee](https://github.com/nasa/astrobee) at `bf43a42d5f89` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/nasa__astrobee` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/nasa__astrobee`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/nasa__astrobee) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/nasa__astrobee/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/nasa__astrobee/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
