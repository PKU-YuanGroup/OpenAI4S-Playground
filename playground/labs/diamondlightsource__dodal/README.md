# DECTRIS Eiger area detector (dodal)

`labs/diamondlightsource__dodal` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence Apache-2.0

DECTRIS Eiger area detector (dodal), adapted from diamondlightsource/dodal. It reads `armed`, `bit_depth`, `stale_params` and `acquisition_id`; runs `stage`, `unstage`, `disarm` and `files`. `stage`: arm the Eiger for one externally triggered collection with the operator's DetectorParams: stage() runs the upstream arming chain unless the detector is armed. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/diamondlightsource__dodal
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/diamondlightsource__dodal --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "dodal": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/diamondlightsource__dodal",
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

- **Reads:** `armed`, `bit_depth`, `stale_params`, `acquisition_id`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `stage` | Arm the Eiger for one externally triggered collection with the operator's DetectorParams: stage() runs the upstream arming chain unless the detector is armed |
| `unstage` | End the collection this connection staged: unstage() waits for the Odin writers, disarms the camera, checks Odin and disables ROI mode; without a staged collection only disarm_detector runs (staged false) |
| `disarm` | Clear the Eiger camera acquire (disarm_detector) and report the resulting armed state |
| `files` | Publish, as one bounded ZIP artifact, the .h5 files Odin wrote for the acquisition id it reports: the regular files directly in DetectorParams.directory whose names start with the id and an underscore, once the detector is neither arming nor armed (is_armed) and every Odin writer reports Writing_RBV 0 |

## Source and status

- Upstream: [diamondlightsource/dodal](https://github.com/diamondlightsource/dodal) at `f96fef4e72a7` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/diamondlightsource__dodal` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/diamondlightsource__dodal`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/diamondlightsource__dodal) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/diamondlightsource__dodal/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/diamondlightsource__dodal/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
