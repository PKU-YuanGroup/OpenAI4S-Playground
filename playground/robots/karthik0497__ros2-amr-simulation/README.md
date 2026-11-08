# ros2-amr-simulation differential-drive base

`robots/karthik0497__ros2-amr-simulation` · Mobile robots · simulation · risk R2 · licence MIT

ros2-amr-simulation differential-drive base, adapted from karthik0497/ros2-amr-simulation. It reads `pose`, `twist`, `read_sim_clock` and `read_joint_states`; runs `publish_cmd_vel`. `publish_cmd_vel`: publish one geometry_msgs/Twist velocity setpoint to /cmd_vel for the gz-sim DiffDrive plugin. The receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/karthik0497__ros2-amr-simulation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/karthik0497__ros2-amr-simulation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ros2-amr-simulation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/karthik0497__ros2-amr-simulation",
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

- **Reads:** `pose`, `twist`, `read_sim_clock`, `read_joint_states`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_cmd_vel` | Publish one geometry_msgs/Twist velocity setpoint to /cmd_vel for the gz-sim DiffDrive plugin. The receipt confirms only that rosbridge accepted the publication, not motion, arrival or stopping. |

## Source and status

- Upstream: [karthik0497/ros2-amr-simulation](https://github.com/karthik0497/ros2-amr-simulation) at `202aad5cac88` (MIT); fetch it with `python3 scripts/add_device.py robots/karthik0497__ros2-amr-simulation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/karthik0497__ros2-amr-simulation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/karthik0497__ros2-amr-simulation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/karthik0497__ros2-amr-simulation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/karthik0497__ros2-amr-simulation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
