# Newport SMC100 motor controller (smc100_base.smc100)

`labs/jieunboy0516__newport-smc100-motor-controller-library---python` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Newport SMC100 motor controller (smc100_base.smc100), adapted from jieunboy0516/newport-smc100-motor-controller-library---python. It reads `position`, `state` and `errors`; sets `velocity`; runs `move_absolute`, `move_relative`, `start_home` and `stop_motion`. `move_absolute`: move the axis to an absolute position in mm (the native PA command). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/jieunboy0516__newport-smc100-motor-controller-library---python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/jieunboy0516__newport-smc100-motor-controller-library---python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "newport-smc100-motor-controller-library---python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/jieunboy0516__newport-smc100-motor-controller-library---python",
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

- **Reads:** `position`, `state`, `errors`
- **Sets:** `velocity`

| Action | What it does |
| --- | --- |
| `move_absolute` | Move the axis to an absolute position in mm (the native PA command) |
| `move_relative` | Move the axis by a relative offset in mm (the native PR command) |
| `start_home` | Start the native home command (OR); it reports command acceptance, not homing completion |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [jieunboy0516/newport-smc100-motor-controller-library---python](https://github.com/jieunboy0516/newport-smc100-motor-controller-library---python) at `b828102ddcc3` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/jieunboy0516__newport-smc100-motor-controller-library---python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/jieunboy0516__newport-smc100-motor-controller-library---python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/jieunboy0516__newport-smc100-motor-controller-library---python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/jieunboy0516__newport-smc100-motor-controller-library---python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/jieunboy0516__newport-smc100-motor-controller-library---python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
