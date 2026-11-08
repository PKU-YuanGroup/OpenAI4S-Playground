# HelixCycler OT thermocycler (tc_send_code.HardwareController)

`labs/helixworks-technologies__helixcycler` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

HelixCycler OT thermocycler (tc_send_code.HardwareController), adapted from helixworks-technologies/helixcycler. It reads `lid_temperature`, `plate_temperature` and `plate_hold_remaining`; sets `lid_setpoint`, `plate_setpoint` and `shake_speed`; runs `set_plate_target`, `open_lid`, `close_lid` and `deactivate_all`. `set_plate_target`: set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/helixworks-technologies__helixcycler
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/helixworks-technologies__helixcycler --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "helixcycler": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/helixworks-technologies__helixcycler",
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

- **Reads:** `lid_temperature`, `plate_temperature`, `plate_hold_remaining`
- **Sets:** `lid_setpoint`, `plate_setpoint`, `shake_speed`

| Action | What it does |
| --- | --- |
| `set_plate_target` | Set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. |
| `open_lid` | Open the lid (the native M126 command) |
| `close_lid` | Close the lid (the native M127 command) |
| `deactivate_all` | Stop the shaker and turn off heating and cooling for the plate and the lid (the native deactivate_shaker, G28 and M106, then deactivate_all, M18); it takes no input |

## Source and status

- Upstream: [helixworks-technologies/helixcycler](https://github.com/helixworks-technologies/helixcycler) at `29bcd934a8d5` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/helixworks-technologies__helixcycler` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/helixworks-technologies__helixcycler`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/helixworks-technologies__helixcycler) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/helixworks-technologies__helixcycler/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/helixworks-technologies__helixcycler/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
