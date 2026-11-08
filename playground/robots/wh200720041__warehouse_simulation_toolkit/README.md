# Warehouse Simulation Toolkit (Gazebo, Pioneer 3DX)

`robots/wh200720041__warehouse_simulation_toolkit` · Simulation · simulation · risk R2 · licence BSD-3-Clause

Warehouse Simulation Toolkit (Gazebo, Pioneer 3DX), adapted from wh200720041/warehouse_simulation_toolkit. It runs `publish_cmd_vel`. `publish_cmd_vel`: publish one geometry_msgs/Twist velocity setpoint on /cmd_vel for the Gazebo differential-drive subscription. The receipt is transmission evidence only, not motion, arrival or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/wh200720041__warehouse_simulation_toolkit
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/wh200720041__warehouse_simulation_toolkit --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "warehouse_simulation_toolkit": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/wh200720041__warehouse_simulation_toolkit",
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
| `publish_cmd_vel` | Publish one geometry_msgs/Twist velocity setpoint on /cmd_vel for the Gazebo differential-drive subscription. The receipt is transmission evidence only, not motion, arrival or stopping. |

## Source and status

- Upstream: [wh200720041/warehouse_simulation_toolkit](https://github.com/wh200720041/warehouse_simulation_toolkit) at `18df8ce6dde6` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/wh200720041__warehouse_simulation_toolkit` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/wh200720041__warehouse_simulation_toolkit`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/wh200720041__warehouse_simulation_toolkit) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/wh200720041__warehouse_simulation_toolkit/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/wh200720041__warehouse_simulation_toolkit/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
