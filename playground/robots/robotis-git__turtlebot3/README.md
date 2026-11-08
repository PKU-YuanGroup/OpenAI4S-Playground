# ROBOTIS TurtleBot3 mobile base

`robots/robotis-git__turtlebot3` · Mobile robots · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence Apache-2.0

ROBOTIS TurtleBot3 mobile base, adapted from robotis-git/turtlebot3. It reads `battery_voltage`, `battery_percentage`, `battery_present`, `odom_pose` and 3 more; runs `publish_velocity`, `set_motor_power` and `disable_torque`. `publish_velocity`: publish one geometry_msgs/TwistStamped velocity setpoint to the upstream cmd_vel topic; the receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/robotis-git__turtlebot3
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/robotis-git__turtlebot3 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "turtlebot3": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/robotis-git__turtlebot3",
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

- **Reads:** `battery_voltage`, `battery_percentage`, `battery_present`, `odom_pose`, `odom_twist`, `wheel_velocity`, `torque_enabled`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_velocity` | Publish one geometry_msgs/TwistStamped velocity setpoint to the upstream cmd_vel topic; the receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping |
| `set_motor_power` | Call the upstream std_srvs/SetBool motor_power service to enable or disable motor torque; enabling does not clear a stale cmd_vel setpoint published by another ROS client |
| `disable_torque` | Fixed, input-free std_srvs/SetBool(false) request to the upstream motor_power service; it disables motor torque and reports only the upstream write acknowledgement |

## Source and status

- Upstream: [robotis-git/turtlebot3](https://github.com/robotis-git/turtlebot3) at `fc817ce3073a` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/robotis-git__turtlebot3` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/robotis-git__turtlebot3`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/robotis-git__turtlebot3) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/robotis-git__turtlebot3/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/robotis-git__turtlebot3/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
