# MuJoCo ROS simulator

`robots/ubi-agni__mujoco_ros_pkgs` · Simulation · simulation · risk R0 · licence BSD-3-Clause

MuJoCo ROS simulator, adapted from ubi-agni/mujoco_ros_pkgs. It reads `get_sim_info`; runs `pause`. `pause`: pause the MuJoCo ROS simulator with the acknowledged set_pause service. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/ubi-agni__mujoco_ros_pkgs
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/ubi-agni__mujoco_ros_pkgs --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "mujoco_ros_pkgs": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/ubi-agni__mujoco_ros_pkgs",
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

- **Reads:** `get_sim_info`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `pause` | Pause the MuJoCo ROS simulator with the acknowledged set_pause service |

## Source and status

- Upstream: [ubi-agni/mujoco_ros_pkgs](https://github.com/ubi-agni/mujoco_ros_pkgs) at `9304ca7ec254` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/ubi-agni__mujoco_ros_pkgs` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/ubi-agni__mujoco_ros_pkgs`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/ubi-agni__mujoco_ros_pkgs) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/ubi-agni__mujoco_ros_pkgs/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/ubi-agni__mujoco_ros_pkgs/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
