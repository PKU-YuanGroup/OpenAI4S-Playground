# UR5 vacuum gripper array (Gazebo)

`robots/lihuang3__ur5_ros-gazebo` · Robot arms and grippers · simulation · risk R2 · licence NOASSERTION

UR5 vacuum gripper array (Gazebo), adapted from lihuang3/ur5_ros-gazebo. It reads `read_grasping`, `read_tracker` and `read_block_poses`; runs `vacuum_gripper_0_on`, `vacuum_gripper_1_on`, `vacuum_gripper_2_on`, `vacuum_gripper_3_on` and 14 more. `vacuum_gripper_0_on`: call the acknowledged /ur5/vacuum_gripper/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/lihuang3__ur5_ros-gazebo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/lihuang3__ur5_ros-gazebo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ur5_ros-gazebo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/lihuang3__ur5_ros-gazebo",
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

- **Reads:** `read_grasping`, `read_tracker`, `read_block_poses`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `vacuum_gripper_0_on` | Call the acknowledged /ur5/vacuum_gripper/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned |
| `vacuum_gripper_1_on` | Call the acknowledged /ur5/vacuum_gripper1/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned |
| `vacuum_gripper_2_on` | Call the acknowledged /ur5/vacuum_gripper2/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned |
| `vacuum_gripper_3_on` | Call the acknowledged /ur5/vacuum_gripper3/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned |
| `vacuum_gripper_4_on` | Call the acknowledged /ur5/vacuum_gripper4/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned |
| `vacuum_gripper_5_on` | Call the acknowledged /ur5/vacuum_gripper5/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned |
| `vacuum_gripper_6_on` | Call the acknowledged /ur5/vacuum_gripper6/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned |
| `vacuum_gripper_7_on` | Call the acknowledged /ur5/vacuum_gripper7/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned |
| `vacuum_gripper_8_on` | Call the acknowledged /ur5/vacuum_gripper8/on std_srvs/Empty service; the empty reply confirms only that the plugin handler returned |
| `vacuum_gripper_0_off` | Release vacuum channel 0 through the /ur5/vacuum_gripper/off std_srvs/Empty service; a held object may drop, the arm is not stopped, and this is not a safe state |
| `vacuum_gripper_1_off` | Release vacuum channel 1 through the /ur5/vacuum_gripper1/off std_srvs/Empty service; a held object may drop, the arm is not stopped, and this is not a safe state |
| `vacuum_gripper_2_off` | Release vacuum channel 2 through the /ur5/vacuum_gripper2/off std_srvs/Empty service; a held object may drop, the arm is not stopped, and this is not a safe state |
| `vacuum_gripper_3_off` | Release vacuum channel 3 through the /ur5/vacuum_gripper3/off std_srvs/Empty service; a held object may drop, the arm is not stopped, and this is not a safe state |
| `vacuum_gripper_4_off` | Release vacuum channel 4 through the /ur5/vacuum_gripper4/off std_srvs/Empty service; a held object may drop, the arm is not stopped, and this is not a safe state |
| `vacuum_gripper_5_off` | Release vacuum channel 5 through the /ur5/vacuum_gripper5/off std_srvs/Empty service; a held object may drop, the arm is not stopped, and this is not a safe state |
| `vacuum_gripper_6_off` | Release vacuum channel 6 through the /ur5/vacuum_gripper6/off std_srvs/Empty service; a held object may drop, the arm is not stopped, and this is not a safe state |
| `vacuum_gripper_7_off` | Release vacuum channel 7 through the /ur5/vacuum_gripper7/off std_srvs/Empty service; a held object may drop, the arm is not stopped, and this is not a safe state |
| `vacuum_gripper_8_off` | Release vacuum channel 8 through the /ur5/vacuum_gripper8/off std_srvs/Empty service; a held object may drop, the arm is not stopped, and this is not a safe state |

## Source and status

- Upstream: [lihuang3/ur5_ros-gazebo](https://github.com/lihuang3/ur5_ros-gazebo) at `2f7b9b056bb4` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/lihuang3__ur5_ros-gazebo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/lihuang3__ur5_ros-gazebo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/lihuang3__ur5_ros-gazebo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/lihuang3__ur5_ros-gazebo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/lihuang3__ur5_ros-gazebo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
