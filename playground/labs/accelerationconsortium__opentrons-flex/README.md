# Opentrons Flex motion controller (FlexMotionController)

`labs/accelerationconsortium__opentrons-flex` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Opentrons Flex motion controller (FlexMotionController), adapted from accelerationconsortium/opentrons-flex. It reads `simulating` and `machine_status`; sets `lights_button` and `lights_rails`; runs `home`, `cartesian_pose` and `stop`. `home`: home every Flex axis with FlexMotionController.home(); the declared re-enable: after a halt or an e-stop the connector refuses every other actuation until this full home completes. The latch refuses it and a safety reset never runs it. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/accelerationconsortium__opentrons-flex
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/accelerationconsortium__opentrons-flex --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "opentrons-flex": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/accelerationconsortium__opentrons-flex",
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

- **Reads:** `simulating`, `machine_status`
- **Sets:** `lights_button`, `lights_rails`

| Action | What it does |
| --- | --- |
| `home` | Home every Flex axis with FlexMotionController.home(); the declared re-enable: after a halt or an e-stop the connector refuses every other actuation until this full home completes. The latch refuses it and a safety reset never runs it. |
| `cartesian_pose` | Move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. |
| `stop` | Halt all motion with FlexMotionController.stop() (the OT3API halt path); it takes no input, is the declared safe state, and leaves the robot needing a full home |

## Source and status

- Upstream: [accelerationconsortium/opentrons-flex](https://github.com/accelerationconsortium/opentrons-flex) at `2639016ee9f2` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/accelerationconsortium__opentrons-flex` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/accelerationconsortium__opentrons-flex`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/accelerationconsortium__opentrons-flex) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/accelerationconsortium__opentrons-flex/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/accelerationconsortium__opentrons-flex/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
