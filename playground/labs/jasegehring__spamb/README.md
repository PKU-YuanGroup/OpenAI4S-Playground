# SPAMB syringe pump (Chemyx Fusion 4000-X, PumpController)

`labs/jasegehring__spamb` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

SPAMB syringe pump (Chemyx Fusion 4000-X, PumpController), adapted from jasegehring/spamb. It reads `running`, `dispensed_volume` and `volume_remaining`; sets `direction`, `flow_rate`, `target_volume` and `syringe_diameter`; runs `run_pump` and `stop_pump`. `run_pump`: run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/jasegehring__spamb
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/jasegehring__spamb --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "spamb": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/jasegehring__spamb",
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

- **Reads:** `running`, `dispensed_volume`, `volume_remaining`
- **Sets:** `direction`, `flow_rate`, `target_volume`, `syringe_diameter`

| Action | What it does |
| --- | --- |
| `run_pump` | Run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. |
| `stop_pump` | Stop the pump; this is the safe state and takes no input |

## Source and status

- Upstream: [jasegehring/spamb](https://github.com/jasegehring/spamb) at `06a404c1879d` (MIT); fetch it with `python3 scripts/add_device.py labs/jasegehring__spamb` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/jasegehring__spamb`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/jasegehring__spamb) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/jasegehring__spamb/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/jasegehring__spamb/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
