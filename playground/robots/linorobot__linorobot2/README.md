# linorobot2 Gazebo mobile-base environment

`robots/linorobot__linorobot2` · Mobile robots · simulation · risk R2 · licence Apache-2.0

linorobot2 Gazebo mobile-base environment, adapted from linorobot/linorobot2. It reads `read_odometry`, `read_sim_clock`, `read_imu` and `read_laser_scan`; runs `publish_cmd_vel` and `resume_simulation`. `publish_cmd_vel`: publish one geometry_msgs/Twist velocity setpoint to /cmd_vel for the gz-sim DiffDrive plugin. The receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/linorobot__linorobot2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/linorobot__linorobot2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "linorobot2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/linorobot__linorobot2",
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

- **Reads:** `read_odometry`, `read_sim_clock`, `read_imu`, `read_laser_scan`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_cmd_vel` | Publish one geometry_msgs/Twist velocity setpoint to /cmd_vel for the gz-sim DiffDrive plugin. The receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. |
| `resume_simulation` | The declared re-enable after a safety reset: publish a zero Twist on /cmd_vel, then unpause the world with a WorldControl request (pause false) on /world/turtlebot3_world/control. DiffDrive keeps the last Twist it received and applies it as soon as the world runs; the zero replaces it, but it is an unacknowledged publication, so a stored command can still act for a few world steps. |

## Source and status

- Upstream: [linorobot/linorobot2](https://github.com/linorobot/linorobot2) at `f6b0bd0350c4` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/linorobot__linorobot2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/linorobot__linorobot2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/linorobot__linorobot2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/linorobot__linorobot2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/linorobot__linorobot2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
