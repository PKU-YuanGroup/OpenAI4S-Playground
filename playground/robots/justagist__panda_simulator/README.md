# Franka Emika Panda simulated hand

`robots/justagist__panda_simulator` · Robot arms and grippers · simulation · risk R2 · licence Apache-2.0

Franka Emika Panda simulated hand, adapted from justagist/panda_simulator. It reads `finger_positions`; runs `move_gripper`, `grasp_gripper` and `stop_gripper`. `move_gripper`: send one franka_gripper/MoveAction goal with a finger opening and speed; the receipt reports the upstream action's terminal success, not a separately measured contact force. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/justagist__panda_simulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/justagist__panda_simulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "panda_simulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/justagist__panda_simulator",
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

- **Reads:** `finger_positions`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_gripper` | Send one franka_gripper/MoveAction goal with a finger opening and speed; the receipt reports the upstream action's terminal success, not a separately measured contact force |
| `grasp_gripper` | Send one franka_gripper/GraspAction goal; the pinned handler performs the same position move as MoveAction and ignores force and epsilon |
| `stop_gripper` | Fixed, input-free franka_gripper/StopAction request; the upstream handler buffers a hold of the measured opening at zero speed and acknowledges success before the controller applies it |

## Source and status

- Upstream: [justagist/panda_simulator](https://github.com/justagist/panda_simulator) at `6cec91dcc739` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/justagist__panda_simulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/justagist__panda_simulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/justagist__panda_simulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/justagist__panda_simulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/justagist__panda_simulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
