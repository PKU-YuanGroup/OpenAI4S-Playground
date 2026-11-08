# MRS Crazyflies cf_1 velocity interface

`robots/larics__mrs_crazyflies` · Mobile robots · simulation · risk R2 · licence NOASSERTION

MRS Crazyflies cf_1 velocity interface, adapted from larics/mrs_crazyflies. It reads `pose`; runs `publish_cmd_vel` and `request_emergency_stop`. `publish_cmd_vel`: publish one geometry_msgs/Twist velocity command on /cf_1/cmd_vel; transmission only. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/larics__mrs_crazyflies
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/larics__mrs_crazyflies --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "mrs_crazyflies": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/larics__mrs_crazyflies",
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

- **Reads:** `pose`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_cmd_vel` | Publish one geometry_msgs/Twist velocity command on /cf_1/cmd_vel; transmission only |
| `request_emergency_stop` | Call the swarm-wide /all/emergency Empty service, a motor-cut request whose response means only that the server callback returned; not a confirmed stop |

## Source and status

- Upstream: [larics/mrs_crazyflies](https://github.com/larics/mrs_crazyflies) at `234ac04745a5` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/larics__mrs_crazyflies` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/larics__mrs_crazyflies`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/larics__mrs_crazyflies) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/larics__mrs_crazyflies/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/larics__mrs_crazyflies/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
