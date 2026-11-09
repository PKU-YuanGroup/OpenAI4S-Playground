# Panda active-inference simulation

`robots/cpezzato__panda_simulation` · Robot arms and grippers · simulation · risk R2 · licence Apache-2.0

Panda active-inference simulation, adapted from cpezzato/panda_simulation. It reads `read_joint_state` and `read_free_energy`; runs `set_joint1_effort`, `set_joint2_effort`, `set_joint3_effort`, `set_joint4_effort` and 3 more. `set_joint1_effort`: publish one effort command for panda_joint1 on /robot1/panda_joint1_controller/command; the AIC node may overwrite it, and while the world is paused no effort reaches the joint. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/cpezzato__panda_simulation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/cpezzato__panda_simulation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "panda_simulation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/cpezzato__panda_simulation",
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

- **Reads:** `read_joint_state`, `read_free_energy`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_joint1_effort` | Publish one effort command for panda_joint1 on /robot1/panda_joint1_controller/command; the AIC node may overwrite it, and while the world is paused no effort reaches the joint |
| `set_joint2_effort` | Publish one effort command for panda_joint2 on /robot1/panda_joint2_controller/command; the AIC node may overwrite it, and while the world is paused no effort reaches the joint |
| `set_joint3_effort` | Publish one effort command for panda_joint3 on /robot1/panda_joint3_controller/command; the AIC node may overwrite it, and while the world is paused no effort reaches the joint |
| `set_joint4_effort` | Publish one effort command for panda_joint4 on /robot1/panda_joint4_controller/command; the AIC node may overwrite it, and while the world is paused no effort reaches the joint |
| `set_joint5_effort` | Publish one effort command for panda_joint5 on /robot1/panda_joint5_controller/command; the AIC node may overwrite it, and while the world is paused no effort reaches the joint |
| `set_joint6_effort` | Publish one effort command for panda_joint6 on /robot1/panda_joint6_controller/command; the AIC node may overwrite it, and while the world is paused no effort reaches the joint |
| `set_joint7_effort` | Publish one effort command for panda_joint7 on /robot1/panda_joint7_controller/command; the AIC node may overwrite it, and while the world is paused no effort reaches the joint |

## Source and status

- Upstream: [cpezzato/panda_simulation](https://github.com/cpezzato/panda_simulation) at `58e1675a372b` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/cpezzato__panda_simulation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/cpezzato__panda_simulation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/cpezzato__panda_simulation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/cpezzato__panda_simulation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/cpezzato__panda_simulation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
