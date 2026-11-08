# OpenArm PickCube-v1 (ManiSkill/SAPIEN)

`robots/enactic__openarm_maniskill_simulation` · Simulation · robot arm manipulation · simulation · risk R0 · licence NOASSERTION

OpenArm PickCube-v1 (ManiSkill/SAPIEN), adapted from enactic/openarm_maniskill_simulation. It reads `observation`, `reward`, `terminated`, `truncated` and 3 more; runs `reset`, `step` and `seed`. `reset`: reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/enactic__openarm_maniskill_simulation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/enactic__openarm_maniskill_simulation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "openarm_maniskill_simulation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/enactic__openarm_maniskill_simulation",
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

- **Reads:** `observation`, `reward`, `terminated`, `truncated`, `tick`, `episode`, `seed`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `reset` | Reset the simulated world to a scenario start state and return the initial observation. When a seed is supplied the endpoint records it in the receipt; otherwise the endpoint's declared default seed applies. |
| `step` | Advance the simulated world by a bounded number of fixed timesteps, optionally applying an action for each step, and return the resulting observation and terminal flags. |
| `seed` | Set the seed used by the simulated world's random number generators for subsequent steps, without resetting the world. The accepted seed is echoed in the receipt. |

## Source and status

- Upstream: [enactic/openarm_maniskill_simulation](https://github.com/enactic/openarm_maniskill_simulation) at `3d3615aadabf` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/enactic__openarm_maniskill_simulation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/enactic__openarm_maniskill_simulation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/enactic__openarm_maniskill_simulation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/enactic__openarm_maniskill_simulation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/enactic__openarm_maniskill_simulation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
