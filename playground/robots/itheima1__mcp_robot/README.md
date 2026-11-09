# itheima1 mcp_robot six-servo arm (ServoControllerStandalone)

`robots/itheima1__mcp_robot` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

itheima1 mcp_robot six-servo arm (ServoControllerStandalone), adapted from itheima1/mcp_robot. It reads `joint_positions`; runs `move_joints`, `home`, `disable_all_torque` and `enable_all_torque`. `move_joints`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/itheima1__mcp_robot
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/itheima1__mcp_robot --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "mcp_robot": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/itheima1__mcp_robot",
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

- **Reads:** `joint_positions`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_joints` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |
| `home` | Drive axes to their declared home position or reference switch, establishing the coordinate reference needed by other motion capabilities. |
| `disable_all_torque` | Disable the torque of servos 1 to 6 (the safe state); it takes no input |
| `enable_all_torque` | Re-enable the torque of servos 1 to 6 after a safety reset (the declared re-enable); it takes no input, is refused while the e-stop is latched and is never run by the reset. The upstream arm_tighten documents that the arm then holds its current position; treat it as an actuation |

## Source and status

- Upstream: [itheima1/mcp_robot](https://github.com/itheima1/mcp_robot) at `18f9ea5ff42c` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/itheima1__mcp_robot` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/itheima1__mcp_robot`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/itheima1__mcp_robot) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/itheima1__mcp_robot/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/itheima1__mcp_robot/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
