# eeUVsim U-CAT AUV simulator

`robots/centre-for-biorobotics__eeuvsim_gazebo` · Simulation · underwater robotics · simulation · risk R2 · licence NOASSERTION

eeUVsim U-CAT AUV simulator, adapted from centre-for-biorobotics/eeuvsim_gazebo. It reads `name`, `pose`, `twist`, `reference_frame` and 6 more; runs `set_fin_oscillation` and `publish_reset`. `set_fin_oscillation`: publish one Flippers message with the four fin oscillation commands on /hw/flippers_cmd. The receipt confirms only that rosbridge accepted the publication, not that moveFins applied it or that the AUV moved or stopped. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/centre-for-biorobotics__eeuvsim_gazebo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/centre-for-biorobotics__eeuvsim_gazebo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "eeuvsim_gazebo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/centre-for-biorobotics__eeuvsim_gazebo",
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

- **Reads:** `name`, `pose`, `twist`, `reference_frame`, `flipper_fr`, `flipper_br`, `flipper_bl`, `flipper_fl`, `read_auv_state`, `read_fin_feedback`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_fin_oscillation` | Publish one Flippers message with the four fin oscillation commands on /hw/flippers_cmd. The receipt confirms only that rosbridge accepted the publication, not that moveFins applied it or that the AUV moved or stopped. |
| `publish_reset` | Publish one std_msgs/Bool data=true reset request on /ucat/reset. This is an unacknowledged publication: AUVMotion's reset callback and moveFins' reset_joints may be triggered, but the driver receives no completion, and the fin timer is not stopped. |

## Source and status

- Upstream: [centre-for-biorobotics/eeuvsim_gazebo](https://github.com/centre-for-biorobotics/eeuvsim_gazebo) at `7276ed34215c` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/centre-for-biorobotics__eeuvsim_gazebo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/centre-for-biorobotics__eeuvsim_gazebo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/centre-for-biorobotics__eeuvsim_gazebo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/centre-for-biorobotics__eeuvsim_gazebo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/centre-for-biorobotics__eeuvsim_gazebo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
