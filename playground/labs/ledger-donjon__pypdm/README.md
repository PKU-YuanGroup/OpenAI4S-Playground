# AlphANOV PDM laser source (pypdm.pdm:PDM)

`labs/ledger-donjon__pypdm` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence LGPL-3.0

AlphANOV PDM laser source (pypdm.pdm:PDM), adapted from ledger-donjon/pypdm. It reads `address`, `protocol_version`, `activation`, `interlock_closed` and 13 more; runs `configure_pulse` and `disable_emission`. `configure_pulse`: write the pulse frequency and the diode current instructions and apply them to the device. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ledger-donjon__pypdm
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ledger-donjon__pypdm --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pypdm": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ledger-donjon__pypdm",
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

- **Reads:** `address`, `protocol_version`, `activation`, `interlock_closed`, `temperature`, `current`, `current_percentage`, `maximum_current`, `maximum_mean_current`, `offset_current`, `frequency`, `pulse_width`, `delay`, `operating_mode`, `current_source`, `sync_source`, `delay_line_type`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `configure_pulse` | Write the pulse frequency and the diode current instructions and apply them to the device |
| `disable_emission` | Clear the laser activation instruction and apply it (the native safe state); it takes no input |

## Source and status

- Upstream: [ledger-donjon/pypdm](https://github.com/ledger-donjon/pypdm) at `a059c30e5054` (LGPL-3.0); fetch it with `python3 scripts/add_device.py labs/ledger-donjon__pypdm` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ledger-donjon__pypdm`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ledger-donjon__pypdm) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ledger-donjon__pypdm/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ledger-donjon__pypdm/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
