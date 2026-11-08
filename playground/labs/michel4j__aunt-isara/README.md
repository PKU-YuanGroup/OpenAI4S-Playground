# ISARA sample automounter (AuntISARAApp)

`labs/michel4j__aunt-isara` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

ISARA sample automounter (AuntISARAApp), adapted from michel4j/aunt-isara. It reads `status`, `action`, `position`, `tool` and 7 more; runs `select_mount_port`, `home` and `stop_all_motion`. `select_mount_port`: convert a dewar port into the native tool, puck and sample mount parameters and store it as the next port; this prepares a mount and does not move the robot. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/michel4j__aunt-isara
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/michel4j__aunt-isara --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "aunt-isara": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/michel4j__aunt-isara",
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

- **Reads:** `status`, `action`, `position`, `tool`, `emergency_ok`, `collision_ok`, `lid_open`, `mounted_sample`, `next_port`, `dewar_temperature_1`, `dewar_temperature_2`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `select_mount_port` | Convert a dewar port into the native tool, puck and sample mount parameters and store it as the next port; this prepares a mount and does not move the robot |
| `home` | Home the automounter with the current tool and report whether the controller reached HOME and is idle |
| `stop_all_motion` | Stop all sample-operation motion by queueing the native panic command; it takes no input |

## Source and status

- Upstream: [michel4j/aunt-isara](https://github.com/michel4j/aunt-isara) at `f95cff5e6cec` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/michel4j__aunt-isara` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/michel4j__aunt-isara`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/michel4j__aunt-isara) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/michel4j__aunt-isara/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/michel4j__aunt-isara/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
