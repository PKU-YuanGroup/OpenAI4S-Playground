# Science Jubilee motion platform (science_jubilee.Machine.Machine)

`labs/machineagency__science-jubilee` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Science Jubilee motion platform (science_jubilee.Machine.Machine), adapted from machineagency/science-jubilee. It reads `x_position`, `y_position` and `z_position`; runs `move_to`, `home` and `set_tool_offset`. `move_to`: move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/machineagency__science-jubilee
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/machineagency__science-jubilee --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "science-jubilee": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/machineagency__science-jubilee",
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

- **Reads:** `x_position`, `y_position`, `z_position`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_to` | Move the tool centre point to a Cartesian position and orientation in a named frame. The endpoint solves inverse kinematics; an unreachable target is rejected before motion. |
| `home` | Drive axes to their declared home position or reference switch, establishing the coordinate reference needed by other motion capabilities. |
| `set_tool_offset` | Set the X/Y/Z tool offset of a configured tool with the upstream G10 command |

## Source and status

- Upstream: [machineagency/science-jubilee](https://github.com/machineagency/science-jubilee) at `bb918fa78f30` (MIT); fetch it with `python3 scripts/add_device.py labs/machineagency__science-jubilee` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/machineagency__science-jubilee`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/machineagency__science-jubilee) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/machineagency__science-jubilee/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/machineagency__science-jubilee/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
