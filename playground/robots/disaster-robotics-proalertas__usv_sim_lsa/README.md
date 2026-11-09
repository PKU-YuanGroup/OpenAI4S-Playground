# USV_SIM_LSA differential USV simulator

`robots/disaster-robotics-proalertas__usv_sim_lsa` · Simulation · underwater robotics · simulation · risk R2 · licence Apache-2.0

USV_SIM_LSA differential USV simulator, adapted from disaster-robotics-proalertas/usv_sim_lsa. It reads `read_simulator_state`, `read_goal_result` and `read_thruster_command`; runs `move_usv_goal`, `pause_physics` and `unpause_physics`. `move_usv_goal`: publish one nav_msgs/Odometry goal to the heading controller's move_usv/goal subscription; the controller publishes the two thruster commands without an acknowledgement. The receipt proves only that rosbridge accepted the publication, not that the boat moved or reached the goal. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/disaster-robotics-proalertas__usv_sim_lsa
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/disaster-robotics-proalertas__usv_sim_lsa --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "usv_sim_lsa": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/disaster-robotics-proalertas__usv_sim_lsa",
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

- **Reads:** `read_simulator_state`, `read_goal_result`, `read_thruster_command`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_usv_goal` | Publish one nav_msgs/Odometry goal to the heading controller's move_usv/goal subscription; the controller publishes the two thruster commands without an acknowledgement. The receipt proves only that rosbridge accepted the publication, not that the boat moved or reached the goal. |
| `pause_physics` | Call the acknowledged /gazebo/pause_physics std_srvs/Empty service; this is the declared simulated safe state and the native e-stop binding |
| `unpause_physics` | Call the acknowledged /gazebo/unpause_physics std_srvs/Empty service; an ordinary command, refused while the e-stop latch is engaged |

## Source and status

- Upstream: [disaster-robotics-proalertas/usv_sim_lsa](https://github.com/disaster-robotics-proalertas/usv_sim_lsa) at `61e8f4a5f78f` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/disaster-robotics-proalertas__usv_sim_lsa` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/disaster-robotics-proalertas__usv_sim_lsa`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/disaster-robotics-proalertas__usv_sim_lsa) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/disaster-robotics-proalertas__usv_sim_lsa/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/disaster-robotics-proalertas__usv_sim_lsa/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
