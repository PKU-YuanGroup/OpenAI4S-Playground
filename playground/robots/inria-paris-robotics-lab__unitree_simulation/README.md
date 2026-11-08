# Unitree Go2 ROS 2 pybullet simulation

`robots/inria-paris-robotics-lab__unitree_simulation` · Simulation · legged robots · simulation · risk R2 · licence NOASSERTION

Unitree Go2 ROS 2 pybullet simulation, adapted from inria-paris-robotics-lab/unitree_simulation. It reads `pose`, `twist`, `motor_state` and `read_lowstate`; runs `publish_lowcmd`, `reset_simulation` and `unlock_base`. `publish_lowcmd`: publish one unitree_go/LowCmd on /lowcmd; the node applies it on its next timer tick. Transmission only: no execution, arrival or stop acknowledgement. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/inria-paris-robotics-lab__unitree_simulation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/inria-paris-robotics-lab__unitree_simulation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "unitree_simulation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/inria-paris-robotics-lab__unitree_simulation",
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

- **Reads:** `pose`, `twist`, `motor_state`, `read_lowstate`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_lowcmd` | Publish one unitree_go/LowCmd on /lowcmd; the node applies it on its next timer tick. Transmission only: no execution, arrival or stop acknowledgement. |
| `reset_simulation` | Publish Empty on /reset; the node calls simulator.reset() and may unlock the base. A reset is not a stop: last_cmd_msg is kept and the timer keeps stepping. |
| `unlock_base` | Publish Empty on /unlock_base; the callback releases the fixed base constraint. Not a stop and has no acknowledgement. |

## Source and status

- Upstream: [inria-paris-robotics-lab/unitree_simulation](https://github.com/inria-paris-robotics-lab/unitree_simulation) at `b53b31bc0757` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/inria-paris-robotics-lab__unitree_simulation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/inria-paris-robotics-lab__unitree_simulation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/inria-paris-robotics-lab__unitree_simulation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/inria-paris-robotics-lab__unitree_simulation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/inria-paris-robotics-lab__unitree_simulation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
