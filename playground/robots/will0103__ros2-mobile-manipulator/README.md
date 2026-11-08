# will0103 ROS 2 mobile manipulator simulation

`robots/will0103__ros2-mobile-manipulator` · Mobile robots · simulation · risk R2 · licence NOASSERTION

will0103 ROS 2 mobile manipulator simulation, adapted from will0103/ros2-mobile-manipulator. It runs `move_robot`. `move_robot`: send one MoveRobot velocity/duration goal to the ROS 2 /move_robot action server. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/will0103__ros2-mobile-manipulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/will0103__ros2-mobile-manipulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros2-mobile-manipulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/will0103__ros2-mobile-manipulator",
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
| `move_robot` | Send one MoveRobot velocity/duration goal to the ROS 2 /move_robot action server. |

## Source and status

- Upstream: [will0103/ros2-mobile-manipulator](https://github.com/will0103/ros2-mobile-manipulator) at `6f49e8f3b306` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/will0103__ros2-mobile-manipulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/will0103__ros2-mobile-manipulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/will0103__ros2-mobile-manipulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/will0103__ros2-mobile-manipulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/will0103__ros2-mobile-manipulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
