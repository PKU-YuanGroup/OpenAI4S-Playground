# SDL Gazebo mobile manipulator (UR5e arm)

`labs/ad-sdl__sdl-simulation` · Robot arms and grippers · simulation · risk R2 · licence NOASSERTION

SDL Gazebo mobile manipulator (UR5e arm), adapted from ad-sdl/sdl-simulation. It reads `read_arm_status` and `read_nav_status`; runs `arm_pose_goal`, `base_pose_goal`, `left_gripper_position` and `right_gripper_position`. `arm_pose_goal`: publish one geometry_msgs/Pose arm target; the receipt reports the values sent and no execution acknowledgement is available. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ad-sdl__sdl-simulation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ad-sdl__sdl-simulation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sdl-simulation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ad-sdl__sdl-simulation",
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

- **Reads:** `read_arm_status`, `read_nav_status`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `arm_pose_goal` | Publish one geometry_msgs/Pose arm target; the receipt reports the values sent and no execution acknowledgement is available |
| `base_pose_goal` | Publish one PoseStamped navigation goal; the receipt reports the values sent and no execution acknowledgement is available |
| `left_gripper_position` | Publish one Float64 position to the left gripper controller; the receipt reports the value sent |
| `right_gripper_position` | Publish one Float64 position to the right gripper controller; the receipt reports the value sent |

## Source and status

- Upstream: [ad-sdl/sdl-simulation](https://github.com/ad-sdl/sdl-simulation) at `7ae7b7ac5581` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/ad-sdl__sdl-simulation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ad-sdl__sdl-simulation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ad-sdl__sdl-simulation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ad-sdl__sdl-simulation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ad-sdl__sdl-simulation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
