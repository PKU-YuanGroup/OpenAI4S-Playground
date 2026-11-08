# UR5 grasp and Kinect Gazebo simulation

`robots/zzy5510__ur5-grasp-and-kinect-demo-on-gazebo` · Simulation · robot arm manipulation · simulation · risk R2 · licence NOASSERTION

UR5 grasp and Kinect Gazebo simulation, adapted from zzy5510/ur5-grasp-and-kinect-demo-on-gazebo. It reads `read_sim_clock` and `read_joint_state`; runs `pause` and `resume`. `pause`: pause the Gazebo world with the acknowledged /gazebo/pause_physics service; the receipt is the service acknowledgement, not a stopped-state measurement. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/zzy5510__ur5-grasp-and-kinect-demo-on-gazebo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/zzy5510__ur5-grasp-and-kinect-demo-on-gazebo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ur5-grasp-and-kinect-demo-on-gazebo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/zzy5510__ur5-grasp-and-kinect-demo-on-gazebo",
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

- **Reads:** `read_sim_clock`, `read_joint_state`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `pause` | Pause the Gazebo world with the acknowledged /gazebo/pause_physics service; the receipt is the service acknowledgement, not a stopped-state measurement |
| `resume` | Resume the Gazebo world with the acknowledged /gazebo/unpause_physics service; an interrupted controller goal may continue after the unpause |

## Source and status

- Upstream: [zzy5510/ur5-grasp-and-kinect-demo-on-gazebo](https://github.com/zzy5510/ur5-grasp-and-kinect-demo-on-gazebo) at `a5b25d72fe76` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/zzy5510__ur5-grasp-and-kinect-demo-on-gazebo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/zzy5510__ur5-grasp-and-kinect-demo-on-gazebo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/zzy5510__ur5-grasp-and-kinect-demo-on-gazebo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/zzy5510__ur5-grasp-and-kinect-demo-on-gazebo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/zzy5510__ur5-grasp-and-kinect-demo-on-gazebo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
