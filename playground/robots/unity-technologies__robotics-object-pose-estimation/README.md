# UR3 pick-and-place planner (Unity object pose estimation demo)

`robots/unity-technologies__robotics-object-pose-estimation` · Other devices · simulation · risk R1 · licence Apache-2.0

UR3 pick-and-place planner (Unity object pose estimation demo), adapted from unity-technologies/robotics-object-pose-estimation. It runs `plan_pick_and_place`. `plan_pick_and_place`: plan (never execute) the five UR3 pick-and-place trajectories; executed is false. A command: it changes the node's shared planner, so never call while Unity plans; a zero quaternion is refused. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/unity-technologies__robotics-object-pose-estimation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/unity-technologies__robotics-object-pose-estimation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "robotics-object-pose-estimation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/unity-technologies__robotics-object-pose-estimation",
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
| `plan_pick_and_place` | Plan (never execute) the five UR3 pick-and-place trajectories; executed is false. A command: it changes the node's shared planner, so never call while Unity plans; a zero quaternion is refused. |

## Source and status

- Upstream: [unity-technologies/robotics-object-pose-estimation](https://github.com/unity-technologies/robotics-object-pose-estimation) at `45156479bee5` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/unity-technologies__robotics-object-pose-estimation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/unity-technologies__robotics-object-pose-estimation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/unity-technologies__robotics-object-pose-estimation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/unity-technologies__robotics-object-pose-estimation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/unity-technologies__robotics-object-pose-estimation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
