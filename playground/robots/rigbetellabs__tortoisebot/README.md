# TortoiseBot Ignition simulation environment

`robots/rigbetellabs__tortoisebot` · Simulation · mobile robots · simulation · risk R2 · licence NOASSERTION

TortoiseBot Ignition simulation environment, adapted from rigbetellabs/tortoisebot. It reads `read_odometry`, `read_clock` and `read_scan`; runs `publish_velocity` and `resume_simulation`. `publish_velocity`: publish one geometry_msgs/Twist velocity command on /cmd_vel; the publication is transmission only and returns no motion or stop confirmation. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/rigbetellabs__tortoisebot
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/rigbetellabs__tortoisebot --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tortoisebot": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/rigbetellabs__tortoisebot",
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

- **Reads:** `read_odometry`, `read_clock`, `read_scan`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_velocity` | Publish one geometry_msgs/Twist velocity command on /cmd_vel; the publication is transmission only and returns no motion or stop confirmation |
| `resume_simulation` | The declared re-enable after a safety reset: publish a zero Twist on /cmd_vel, then unpause the world with a WorldControl request (pause false) on /world/default/control. DiffDrive keeps the last Twist it received and applies it as soon as the world runs; the zero replaces it, but it is an unacknowledged publication, so a stored command can still act for a few world steps. |

## Source and status

- Upstream: [rigbetellabs/tortoisebot](https://github.com/rigbetellabs/tortoisebot) at `eae9f74a1721` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/rigbetellabs__tortoisebot` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/rigbetellabs__tortoisebot`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/rigbetellabs__tortoisebot) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/rigbetellabs__tortoisebot/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/rigbetellabs__tortoisebot/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
