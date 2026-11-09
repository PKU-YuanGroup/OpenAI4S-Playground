# Webots ROS 2 Spot simulation

`robots/maskor__webots_ros2_spot` · Mobile robots · simulation · risk R2 · licence AGPL-3.0

Webots ROS 2 Spot simulation, adapted from maskor/webots_ros2_spot. It reads `joint_positions`, `odom_position`, `odom_orientation` and `odom_twist`; runs `publish_velocity`, `stand_up`, `sit_down`, `lie_down` and 1 more. `publish_velocity`: publish one geometry_msgs/Twist to the upstream /cmd_vel subscription; the receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/maskor__webots_ros2_spot
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/maskor__webots_ros2_spot --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "webots_ros2_spot": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/maskor__webots_ros2_spot",
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

- **Reads:** `joint_positions`, `odom_position`, `odom_orientation`, `odom_twist`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_velocity` | Publish one geometry_msgs/Twist to the upstream /cmd_vel subscription; the receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping |
| `stand_up` | Call /Spot/stand_up and require the 'standing up' answer; the callback returns after starting a one-second joint-target transition, so the answer is not completion |
| `sit_down` | Call /Spot/sit_down and require the 'sitting down' answer; the callback returns after starting a one-second joint-target transition, so the answer is not completion |
| `lie_down` | Fixed /Spot/lie_down call with override=true; it sets fixed_motion and starts the fixed lie targets. It acknowledges the start only. The sensed stop sends this request and confirms on odometry; this command alone is not that stop |
| `set_height` | Call /Spot/set_height with a body height offset in the source range; the callback stores zd = -height and returns an empty answer on success |

## Source and status

- Upstream: [maskor/webots_ros2_spot](https://github.com/maskor/webots_ros2_spot) at `1245900385c5` (AGPL-3.0); fetch it with `python3 scripts/add_device.py robots/maskor__webots_ros2_spot` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/maskor__webots_ros2_spot`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/maskor__webots_ros2_spot) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/maskor__webots_ros2_spot/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/maskor__webots_ros2_spot/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
