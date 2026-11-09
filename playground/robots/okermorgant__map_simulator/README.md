# map_simulator ROS 2 2-D simulator

`robots/okermorgant__map_simulator` · Simulation · mobile robots · simulation · risk R2 · licence MIT

map_simulator ROS 2 2-D simulator, adapted from okermorgant/map_simulator. It reads `odom_pose`, `odom_twist`, `read_odometry` and `read_scan`; runs `spawn_robot` and `publish_twist`. `spawn_robot`: call the upstream /simulator/spawn service to create a robot or reset an existing robot's pose. The Spawn response is empty, so the receipt confirms only that the service callback returned; it does not prove creation, URDF arrival, motion or a stopped robot. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/okermorgant__map_simulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/okermorgant__map_simulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "map_simulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/okermorgant__map_simulator",
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

- **Reads:** `odom_pose`, `odom_twist`, `read_odometry`, `read_scan`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `spawn_robot` | Call the upstream /simulator/spawn service to create a robot or reset an existing robot's pose. The Spawn response is empty, so the receipt confirms only that the service callback returned; it does not prove creation, URDF arrival, motion or a stopped robot. |
| `publish_twist` | Publish one geometry_msgs/Twist to the upstream /robot1/cmd_vel subscription. The callback copies linear.x, linear.y and angular.z into the robot odometry twist. The receipt proves only that rosbridge accepted the publication; it does not prove motion or a stopped robot. cmd_vel is a topic a physical mobile robot also consumes, so this action is R2 (REVIEW.md item 12). |

## Source and status

- Upstream: [okermorgant/map_simulator](https://github.com/okermorgant/map_simulator) at `537a06464d7f` (MIT); fetch it with `python3 scripts/add_device.py robots/okermorgant__map_simulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/okermorgant__map_simulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/okermorgant__map_simulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/okermorgant__map_simulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/okermorgant__map_simulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
