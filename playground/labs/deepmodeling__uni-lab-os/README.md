# Runze syringe pump

`labs/deepmodeling__uni-lab-os` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

Runze syringe pump, adapted from deepmodeling/uni-lab-os. It reads `plunger_position`, `velocity_grade`, `velocity_init`, `velocity_end` and 7 more; sets `position` and `max_velocity`; runs `pump` and `stop_pump`. `pump`: run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/deepmodeling__uni-lab-os
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/deepmodeling__uni-lab-os --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "uni-lab-os": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/deepmodeling__uni-lab-os",
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

- **Reads:** `plunger_position`, `velocity_grade`, `velocity_init`, `velocity_end`, `valve_position`, `status`, `command_buffer_status`, `backlash_position`, `aux_input_status_1`, `aux_input_status_2`, `software_version`
- **Sets:** `position`, `max_velocity`

| Action | What it does |
| --- | --- |
| `pump` | Run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. |
| `stop_pump` | Send the protocol T stop and confirm Idle; takes no input |

## Source and status

- Upstream: [deepmodeling/uni-lab-os](https://github.com/deepmodeling/uni-lab-os) at `43923ec9473e` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/deepmodeling__uni-lab-os` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/deepmodeling__uni-lab-os`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/deepmodeling__uni-lab-os) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/deepmodeling__uni-lab-os/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/deepmodeling__uni-lab-os/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
