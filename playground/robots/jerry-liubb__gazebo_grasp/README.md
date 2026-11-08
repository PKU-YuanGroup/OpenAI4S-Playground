# Gazebo object state (gazebo_grasp)

`robots/jerry-liubb__gazebo_grasp` · Sensors and cameras · simulation · risk R0 · licence NOASSERTION

Gazebo object state (gazebo_grasp), adapted from jerry-liubb/gazebo_grasp. It reads `read_object`; runs `object_info`. `object_info`: request one object's pose from the Gazebo object-info service. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/jerry-liubb__gazebo_grasp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/jerry-liubb__gazebo_grasp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "gazebo_grasp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/jerry-liubb__gazebo_grasp",
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

- **Reads:** `read_object`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `object_info` | Request one object's pose from the Gazebo object-info service |

## Source and status

- Upstream: [jerry-liubb/gazebo_grasp](https://github.com/jerry-liubb/gazebo_grasp) at `0bd506d52c7e` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/jerry-liubb__gazebo_grasp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/jerry-liubb__gazebo_grasp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/jerry-liubb__gazebo_grasp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/jerry-liubb__gazebo_grasp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/jerry-liubb__gazebo_grasp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
