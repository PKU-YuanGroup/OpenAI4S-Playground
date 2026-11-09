# Niryo pick-and-place planner (Unity Robotics Hub)

`robots/unity-technologies__unity-robotics-hub` · Other devices · simulation · risk R0 · licence Apache-2.0

Niryo pick-and-place planner (Unity Robotics Hub), adapted from unity-technologies/unity-robotics-hub. It runs `plan_pick_and_place`. `plan_pick_and_place`: plan four trajectories. executed is always false. Exclusive. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/unity-technologies__unity-robotics-hub
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/unity-technologies__unity-robotics-hub --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "unity-robotics-hub": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/unity-technologies__unity-robotics-hub",
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
| `plan_pick_and_place` | Plan four trajectories. executed is always false. Exclusive. |

## Source and status

- Upstream: [unity-technologies/unity-robotics-hub](https://github.com/unity-technologies/unity-robotics-hub) at `b8d1e1d4c76c` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/unity-technologies__unity-robotics-hub` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/unity-technologies__unity-robotics-hub`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/unity-technologies__unity-robotics-hub) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/unity-technologies__unity-robotics-hub/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/unity-technologies__unity-robotics-hub/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
