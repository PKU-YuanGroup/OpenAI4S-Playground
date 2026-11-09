# cambel ur_gripper_gz Hand-E gz-sim bringup

`robots/cambel__ur3` · Robot arms and grippers · simulation · risk R2 · licence MIT

cambel ur_gripper_gz Hand-E gz-sim bringup, adapted from cambel/ur3. It reads `read_joint_states`. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/cambel__ur3
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/cambel__ur3 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ur3": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/cambel__ur3",
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

- **Reads:** `read_joint_states`
- **Sets:** —

## Source and status

- Upstream: [cambel/ur3](https://github.com/cambel/ur3) at `10f96dc362a7` (MIT); fetch it with `python3 scripts/add_device.py robots/cambel__ur3` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/cambel__ur3`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/cambel__ur3) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/cambel__ur3/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/cambel__ur3/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
