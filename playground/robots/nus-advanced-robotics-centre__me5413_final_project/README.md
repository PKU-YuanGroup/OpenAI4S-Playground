# ME5413 Gazebo course world

`robots/nus-advanced-robotics-centre__me5413_final_project` · Simulation · simulation · risk R0 · licence MIT

ME5413 Gazebo course world, adapted from nus-advanced-robotics-centre/me5413_final_project. It runs `remove_moving_obstacle`, `clear_objects`, `regenerate_objects`, `open_exit` and 3 more. `remove_moving_obstacle`: delete the moving planar_box obstacle once with the acknowledged DeleteModel service; this is not a stop. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/nus-advanced-robotics-centre__me5413_final_project
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/nus-advanced-robotics-centre__me5413_final_project --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "me5413_final_project": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/nus-advanced-robotics-centre__me5413_final_project",
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
| `remove_moving_obstacle` | Delete the moving planar_box obstacle once with the acknowledged DeleteModel service; this is not a stop |
| `clear_objects` | Publish Int16 0 on the RViz panel's respawn topic to delete the random objects |
| `regenerate_objects` | Publish Int16 1 on the RViz panel's respawn topic to regenerate the random objects |
| `open_exit` | Publish Bool true on /cmd_unblock to request the one-time exit removal |
| `delete_model` | Delete one named Gazebo model through the acknowledged DeleteModel service |
| `read_box_odom` | Read one fresh /box_odom sample published by the object spawner plugin |
| `read_box_markers` | Read one fresh /gazebo/ground_truth/box_markers sample |

## Source and status

- Upstream: [nus-advanced-robotics-centre/me5413_final_project](https://github.com/nus-advanced-robotics-centre/me5413_final_project) at `9fd6ce2643f7` (MIT); fetch it with `python3 scripts/add_device.py robots/nus-advanced-robotics-centre__me5413_final_project` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/nus-advanced-robotics-centre__me5413_final_project`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/nus-advanced-robotics-centre__me5413_final_project) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/nus-advanced-robotics-centre__me5413_final_project/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/nus-advanced-robotics-centre__me5413_final_project/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
