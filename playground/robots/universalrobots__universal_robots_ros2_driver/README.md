# Universal Robots ROS 2 dashboard client

`robots/universalrobots__universal_robots_ros2_driver` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

Universal Robots ROS 2 dashboard client, adapted from universalrobots/universal_robots_ros2_driver. It reads `read_program_running`; runs `stop_dashboard_program`. `stop_dashboard_program`: stop the active dashboard program through the acknowledged UR dashboard stop service; this does not command joint motion or claim a physical emergency stop. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/universalrobots__universal_robots_ros2_driver
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/universalrobots__universal_robots_ros2_driver --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "universal_robots_ros2_driver": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/universalrobots__universal_robots_ros2_driver",
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

- **Reads:** `read_program_running`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `stop_dashboard_program` | Stop the active dashboard program through the acknowledged UR dashboard stop service; this does not command joint motion or claim a physical emergency stop |

## Source and status

- Upstream: [universalrobots/universal_robots_ros2_driver](https://github.com/universalrobots/universal_robots_ros2_driver) at `7e031424bc7a` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/universalrobots__universal_robots_ros2_driver` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/universalrobots__universal_robots_ros2_driver`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/universalrobots__universal_robots_ros2_driver) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/universalrobots__universal_robots_ros2_driver/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/universalrobots__universal_robots_ros2_driver/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
