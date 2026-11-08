# sjtu_drone Gazebo quadrotor simulation

`robots/novog93__sjtu_drone` · Simulation · UAVs · simulation · risk R2 · licence GPL-3.0

sjtu_drone Gazebo quadrotor simulation, adapted from novog93/sjtu_drone. It reads `read_last_cmd_vel`, `read_state`, `read_pose` and `read_mode`; runs `takeoff`, `land`, `reset`, `publish_cmd_vel` and 3 more. `takeoff`: publish one std_msgs/Empty on /simple_drone/takeoff. The callback only moves the state machine from LANDED_MODEL to TAKINGOFF_MODEL; the receipt proves the publication, not that the simulated drone left the ground. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/novog93__sjtu_drone
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/novog93__sjtu_drone --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sjtu_drone": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/novog93__sjtu_drone",
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

- **Reads:** `read_last_cmd_vel`, `read_state`, `read_pose`, `read_mode`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `takeoff` | Publish one std_msgs/Empty on /simple_drone/takeoff. The callback only moves the state machine from LANDED_MODEL to TAKINGOFF_MODEL; the receipt proves the publication, not that the simulated drone left the ground. |
| `land` | Publish one std_msgs/Empty on /simple_drone/land. The callback only moves the state machine to LANDING_MODEL; the receipt proves the publication, not that the simulated drone landed. |
| `reset` | Publish one std_msgs/Empty on /simple_drone/reset. The plugin's callback resets the attitude and velocity PID controllers and the current force and torque but keeps the flight state and stored cmd_vel; it is not an acknowledged stop or an operator safety reset. |
| `publish_cmd_vel` | Publish one geometry_msgs/Twist on /simple_drone/cmd_vel. The fields are position targets in position-control mode and velocity/tilt/rate otherwise; the receipt is a publication acknowledgement only. |
| `set_position_control` | Publish one std_msgs/Bool on /simple_drone/posctrl. The callback only stores the flag; the receipt proves the publication, not the resulting control mode. |
| `set_velocity_mode` | Publish one std_msgs/Bool on /simple_drone/dronevel_mode. The callback stores the flag and publishes the resulting cmd_mode String; the receipt proves the publication only. |
| `reset_world` | Call the /reset_world std_srvs/Empty service (gazebo_ros) that the clone's reset_sim.sh uses. It resets the simulated world, but the plugin keeps its flight state and stored cmd_vel, so a flying drone keeps flying; it is not a stop. |

## Source and status

- Upstream: [novog93/sjtu_drone](https://github.com/novog93/sjtu_drone) at `3f8627ebddf3` (GPL-3.0); fetch it with `python3 scripts/add_device.py robots/novog93__sjtu_drone` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/novog93__sjtu_drone`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/novog93__sjtu_drone) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/novog93__sjtu_drone/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/novog93__sjtu_drone/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
