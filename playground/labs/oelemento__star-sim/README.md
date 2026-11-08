# Hamilton STARlet digital twin (star_sim.RobotEnv, PyLabRobot ChatterBox)

`labs/oelemento__star-sim` · Liquid handling and fluidics · simulation · risk R2 · licence MIT

Hamilton STARlet digital twin (star_sim.RobotEnv, PyLabRobot ChatterBox), adapted from oelemento/star-sim. It reads `tips_remaining_columns`; runs `transfer`, `mix` and `tracked_volumes`. `transfer`: pick up fresh tips, aspirate the source wells, dispense the target wells, discard the tips; no cleanup after a failure. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/oelemento__star-sim
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/oelemento__star-sim --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "star-sim": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/oelemento__star-sim",
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

- **Reads:** `tips_remaining_columns`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `transfer` | Pick up fresh tips, aspirate the source wells, dispense the target wells, discard the tips; no cleanup after a failure |
| `mix` | Pick up fresh tips, aspirate and dispense the same wells per cycle, discard the tips; no cleanup after a failure |
| `tracked_volumes` | Tracked liquid volume of declared wells (PyLabRobot volume tracker bookkeeping, not a measurement) |

## Source and status

- Upstream: [oelemento/star-sim](https://github.com/oelemento/star-sim) at `5b5211a4c541` (MIT); fetch it with `python3 scripts/add_device.py labs/oelemento__star-sim` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/oelemento__star-sim`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/oelemento__star-sim) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/oelemento__star-sim/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/oelemento__star-sim/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
