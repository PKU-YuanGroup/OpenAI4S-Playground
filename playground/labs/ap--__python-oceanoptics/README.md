# Ocean Optics QE65000/QE65Pro TEC

`labs/ap--__python-oceanoptics` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Ocean Optics QE65000/QE65Pro TEC, adapted from ap--/python-oceanoptics. It reads `tec_temperature`, `pcb_temperature`, `heatsink_temperature`, `tec_enabled` and 1 more; sets `setpoint`; runs `set_temperature` and `tec_safe_off`. `set_temperature`: set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ap--__python-oceanoptics
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ap--__python-oceanoptics --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "python-oceanoptics": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ap--__python-oceanoptics",
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

- **Reads:** `tec_temperature`, `pcb_temperature`, `heatsink_temperature`, `tec_enabled`, `fan_enabled`
- **Sets:** `setpoint`

| Action | What it does |
| --- | --- |
| `set_temperature` | Set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. |
| `tec_safe_off` | Switch the TEC controller off and leave the cooling fan on (the safe state); no input |

## Source and status

- Upstream: [ap--/python-oceanoptics](https://github.com/ap--/python-oceanoptics) at `3df0c263e47c` (MIT); fetch it with `python3 scripts/add_device.py labs/ap--__python-oceanoptics` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ap--__python-oceanoptics`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ap--__python-oceanoptics) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ap--__python-oceanoptics/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ap--__python-oceanoptics/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
