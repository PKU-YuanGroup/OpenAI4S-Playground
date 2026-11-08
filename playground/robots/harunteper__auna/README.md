# AuNa Gazebo Ackermann race car

`robots/harunteper__auna` · Mobile robots · simulation · risk R2 · licence MIT

AuNa Gazebo Ackermann race car, adapted from harunteper/auna. It reads `read_velocity_source`; runs `select_velocity_source`, `publish_teleop_velocity` and `stop_velocity_source`. `select_velocity_source`: select one configured multiplexer input source. Selecting OFF stops forwarding and makes the timer publish zero commands; selecting a motion source can immediately re-publish that source's cached last command. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/harunteper__auna
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/harunteper__auna --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "auna": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/harunteper__auna",
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

- **Reads:** `read_velocity_source`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `select_velocity_source` | Select one configured multiplexer input source. Selecting OFF stops forwarding and makes the timer publish zero commands; selecting a motion source can immediately re-publish that source's cached last command. |
| `publish_teleop_velocity` | Publish one speed and steering-angle command on the teleop multiplexer input. The multiplexer caches it and repeats it at its timer rate only while the teleop source is selected. The receipt confirms transmission to rosbridge, not motion, arrival or stopping. |
| `stop_velocity_source` | Set the multiplexer velocity source to OFF, making its timer publish zero speed and steering commands. Input-free, acknowledged service call; no input is accepted during the latch. |

## Source and status

- Upstream: [harunteper/auna](https://github.com/harunteper/auna) at `1d8bb13d574d` (MIT); fetch it with `python3 scripts/add_device.py robots/harunteper__auna` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/harunteper__auna`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/harunteper__auna) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/harunteper__auna/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/harunteper__auna/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
