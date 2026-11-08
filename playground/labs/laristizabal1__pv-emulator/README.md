# EA-PS 10060-170 programmable DC source (PV emulator)

`labs/laristizabal1__pv-emulator` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

EA-PS 10060-170 programmable DC source (PV emulator), adapted from laristizabal1/pv-emulator. It reads `voltage`, `current`, `power` and `error_code`; sets `voltage_setpoint`, `current_setpoint` and `output`; runs `output_off`. `output_off`: switch the DC output off (OUTP OFF); this action is the safe state and takes no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/laristizabal1__pv-emulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/laristizabal1__pv-emulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pv-emulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/laristizabal1__pv-emulator",
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

- **Reads:** `voltage`, `current`, `power`, `error_code`
- **Sets:** `voltage_setpoint`, `current_setpoint`, `output`

| Action | What it does |
| --- | --- |
| `output_off` | Switch the DC output off (OUTP OFF); this action is the safe state and takes no input |

## Source and status

- Upstream: [laristizabal1/pv-emulator](https://github.com/laristizabal1/pv-emulator) at `a2339189e88c` (MIT); fetch it with `python3 scripts/add_device.py labs/laristizabal1__pv-emulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/laristizabal1__pv-emulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/laristizabal1__pv-emulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/laristizabal1__pv-emulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/laristizabal1__pv-emulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
