# Warehouse robot simulation (ROS 1 / Gazebo)

`robots/rodriguesrenato__warehouse_robot_simulation` · Simulation · mobile robots · simulation · risk R2 · licence MIT

Warehouse robot simulation (ROS 1 / Gazebo), adapted from rodriguesrenato/warehouse_robot_simulation. It runs `submit_order`. `submit_order`: publish one std_msgs/String order on /warehouse/order/add. The receipt reports the string handed to rosbridge and is transmission evidence only: the upstream callback has no acknowledgement, and this action does not report queueing, robot motion, arrival or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/rodriguesrenato__warehouse_robot_simulation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/rodriguesrenato__warehouse_robot_simulation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "warehouse_robot_simulation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/rodriguesrenato__warehouse_robot_simulation",
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
| `submit_order` | Publish one std_msgs/String order on /warehouse/order/add. The receipt reports the string handed to rosbridge and is transmission evidence only: the upstream callback has no acknowledgement, and this action does not report queueing, robot motion, arrival or stopping. |

## Source and status

- Upstream: [rodriguesrenato/warehouse_robot_simulation](https://github.com/rodriguesrenato/warehouse_robot_simulation) at `c8fe89a8501b` (MIT); fetch it with `python3 scripts/add_device.py robots/rodriguesrenato__warehouse_robot_simulation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/rodriguesrenato__warehouse_robot_simulation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/rodriguesrenato__warehouse_robot_simulation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/rodriguesrenato__warehouse_robot_simulation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/rodriguesrenato__warehouse_robot_simulation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
