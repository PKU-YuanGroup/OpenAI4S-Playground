# APO 1m Ash Dome rotation (ASCOM Alpaca dome server)

`labs/holtzmanjon__apoalpyca` · Other devices · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

APO 1m Ash Dome rotation (ASCOM Alpaca dome server), adapted from holtzmanjon/apoalpyca. It reads `azimuth`, `shutterstatus`, `slewing`, `athome` and 1 more; runs `slew_azimuth`, `park`, `find_home`, `set_park` and 1 more. `slew_azimuth`: start a SlewToAzimuth and wait until the server reports slewing (relay on). Completion is a started rotation, not arrival; no start within 1.5 s is unknown. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/holtzmanjon__apoalpyca
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/holtzmanjon__apoalpyca --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "apoalpyca": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/holtzmanjon__apoalpyca",
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

- **Reads:** `azimuth`, `shutterstatus`, `slewing`, `athome`, `atpark`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `slew_azimuth` | Start a SlewToAzimuth and wait until the server reports slewing (relay on). Completion is a started rotation, not arrival; no start within 1.5 s is unknown |
| `park` | Start a Park slew to the stored park position and wait until the server reports slewing; already parked or no start within 1.5 s is unknown |
| `find_home` | Start a FindHome rotation and wait until the server reports slewing; already home or no start within 1.5 s is unknown |
| `set_park` | Store the current azimuth as the park position through SetPark; no motion is commanded |
| `abort_slew` | Switch the rotation relay off through AbortSlew and confirm the server's slewing flag is false; the dome coasts and the shutters are not affected |

## Source and status

- Upstream: [holtzmanjon/apoalpyca](https://github.com/holtzmanjon/apoalpyca) at `3d4c48ec092c` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/holtzmanjon__apoalpyca` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/holtzmanjon__apoalpyca`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/holtzmanjon__apoalpyca) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/holtzmanjon__apoalpyca/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/holtzmanjon__apoalpyca/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
