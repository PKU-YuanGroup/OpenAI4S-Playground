# Harvard PHD 2000 syringe pump (Model 44)

`labs/matteobroketa__harvard_pump_diy_control` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Harvard PHD 2000 syringe pump (Model 44), adapted from matteobroketa/harvard_pump_diy_control. It reads `running`, `status` and `address`; sets `flow_rate`, `direction` and `syringe_diameter_mm`; runs `run_pump`, `pause_pump`, `resume_pump` and `stop_pump`. `run_pump`: start the pump in the configured direction (RUN). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/matteobroketa__harvard_pump_diy_control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/matteobroketa__harvard_pump_diy_control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "harvard_pump_diy_control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/matteobroketa__harvard_pump_diy_control",
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

- **Reads:** `running`, `status`, `address`
- **Sets:** `flow_rate`, `direction`, `syringe_diameter_mm`

| Action | What it does |
| --- | --- |
| `run_pump` | Start the pump in the configured direction (RUN) |
| `pause_pump` | Stop the pump and keep the configured rate for a later resume (the upstream pause is the native stop) |
| `resume_pump` | Resume pumping in the configured direction after a pause (the upstream resume is the native start) |
| `stop_pump` | Stop the pump with the addressed STP command (the native stop, the safe state); it takes no input |

## Source and status

- Upstream: [matteobroketa/harvard_pump_diy_control](https://github.com/matteobroketa/harvard_pump_diy_control) at `d4a888432a81` (MIT); fetch it with `python3 scripts/add_device.py labs/matteobroketa__harvard_pump_diy_control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/matteobroketa__harvard_pump_diy_control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/matteobroketa__harvard_pump_diy_control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/matteobroketa__harvard_pump_diy_control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/matteobroketa__harvard_pump_diy_control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
