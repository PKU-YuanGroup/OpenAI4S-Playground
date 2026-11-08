# Flamingo stage position controller (PositionController)

`labs/uw-loci__flamingo_control` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Flamingo stage position controller (PositionController), adapted from uw-loci/flamingo_control. It reads `position_x`, `position_y`, `position_z` and `rotation`; sets `home_x`, `home_y`, `home_z` and `home_rotation`; runs `move_stage` and `stop_motion`. `move_stage`: move all four stage axes to an absolute position with the controller's move_to_position; a target outside the configured stage limits is refused instead of clamped. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/uw-loci__flamingo_control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/uw-loci__flamingo_control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "flamingo_control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/uw-loci__flamingo_control",
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

- **Reads:** `position_x`, `position_y`, `position_z`, `rotation`
- **Sets:** `home_x`, `home_y`, `home_z`, `home_rotation`

| Action | What it does |
| --- | --- |
| `move_stage` | Move all four stage axes to an absolute position with the controller's move_to_position; a target outside the configured stage limits is refused instead of clamped |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [uw-loci/flamingo_control](https://github.com/uw-loci/flamingo_control) at `0eee5dac8e54` (MIT); fetch it with `python3 scripts/add_device.py labs/uw-loci__flamingo_control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/uw-loci__flamingo_control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/uw-loci__flamingo_control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/uw-loci__flamingo_control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/uw-loci__flamingo_control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
