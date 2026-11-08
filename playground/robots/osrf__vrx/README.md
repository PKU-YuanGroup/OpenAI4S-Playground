# Virtual RobotX (VRX) simulation environment

`robots/osrf__vrx` · Simulation · marine robotics · simulation · risk R2 · licence Apache-2.0

Virtual RobotX (VRX) simulation environment, adapted from osrf/vrx. It reads `read_sim_clock` and `read_task_info`; runs `publish_left_thrust`, `publish_right_thrust`, `publish_left_thrust_position` and `publish_right_thrust_position`. `publish_left_thrust`: publish one Float64 command on /wamv/thrusters/left/thrust; the receipt is transmission evidence only, not motion, thrust attainment or stopping. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/osrf__vrx
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/osrf__vrx --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "vrx": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/osrf__vrx",
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

- **Reads:** `read_sim_clock`, `read_task_info`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `publish_left_thrust` | Publish one Float64 command on /wamv/thrusters/left/thrust; the receipt is transmission evidence only, not motion, thrust attainment or stopping. |
| `publish_right_thrust` | Publish one Float64 command on /wamv/thrusters/right/thrust; the receipt is transmission evidence only, not motion, thrust attainment or stopping. |
| `publish_left_thrust_position` | Publish one Float64 command on /wamv/thrusters/left/pos; the receipt is transmission evidence only, not joint motion or stopping. |
| `publish_right_thrust_position` | Publish one Float64 command on /wamv/thrusters/right/pos; the receipt is transmission evidence only, not joint motion or stopping. |

## Source and status

- Upstream: [osrf/vrx](https://github.com/osrf/vrx) at `7609d1bd90ce` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/osrf__vrx` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/osrf__vrx`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/osrf__vrx) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/osrf__vrx/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/osrf__vrx/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
