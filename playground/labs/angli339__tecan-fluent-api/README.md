# Tecan Fluent liquid handler through FluentControl (tecan_fluent.tecan_ctrl.Tecan)

`labs/angli339__tecan-fluent-api` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Tecan Fluent liquid handler through FluentControl (tecan_fluent.tecan_ctrl.Tecan), adapted from angli339/tecan-fluent-api. It reads `fluent_status` and `channel_open`; runs `liha_aspirate`, `liha_dispense`, `liha_mix`, `mca_aspirate` and 2 more. `liha_aspirate`: aspirate a volume through one LiHa tip from a 96-well labware well. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/angli339__tecan-fluent-api
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/angli339__tecan-fluent-api --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tecan-fluent-api": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/angli339__tecan-fluent-api",
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

- **Reads:** `fluent_status`, `channel_open`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `liha_aspirate` | Aspirate a volume through one LiHa tip from a 96-well labware well |
| `liha_dispense` | Dispense a volume through one LiHa tip into a 96-well labware well |
| `liha_mix` | Mix a volume in a 96-well labware well with one LiHa tip |
| `mca_aspirate` | Aspirate a volume from a whole plate with the MCA head |
| `mca_dispense` | Dispense a volume into a whole plate with the MCA head |
| `stop_fluent` | Stop the FluentControl method and detach the API channel (the safe state); it takes no input |

## Source and status

- Upstream: [angli339/tecan-fluent-api](https://github.com/angli339/tecan-fluent-api) at `d087edd9a4cd` (MIT); fetch it with `python3 scripts/add_device.py labs/angli339__tecan-fluent-api` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/angli339__tecan-fluent-api`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/angli339__tecan-fluent-api) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/angli339__tecan-fluent-api/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/angli339__tecan-fluent-api/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
