# Thorlabs MCM3000 series 3-axis controller

`labs/amsikking__thorlabs_mcm3000` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Thorlabs MCM3000 series 3-axis controller, adapted from amsikking/thorlabs_mcm3000. It reads `position_ch0`, `position_ch1` and `position_ch2`; runs `move_channel` and `stop_motion`. `move_channel`: move one configured controller channel to a position in micrometres and report the position the controller reads back. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/amsikking__thorlabs_mcm3000
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/amsikking__thorlabs_mcm3000 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "thorlabs_mcm3000": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/amsikking__thorlabs_mcm3000",
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

- **Reads:** `position_ch0`, `position_ch1`, `position_ch2`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_channel` | Move one configured controller channel to a position in micrometres and report the position the controller reads back |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [amsikking/thorlabs_mcm3000](https://github.com/amsikking/thorlabs_mcm3000) at `390cd97e44ab` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/amsikking__thorlabs_mcm3000` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/amsikking__thorlabs_mcm3000`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/amsikking__thorlabs_mcm3000) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/amsikking__thorlabs_mcm3000/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/amsikking__thorlabs_mcm3000/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
