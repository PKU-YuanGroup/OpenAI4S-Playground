# Harvard Apparatus OEM syringe pump (Model 44)

`labs/bgamari__harvard-syringe-pump` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence GPL-3.0

Harvard Apparatus OEM syringe pump (Model 44), adapted from bgamari/harvard-syringe-pump. It reads `accumulated_volume` and `version`; sets `diameter`, `flow_rate`, `target_volume` and `mode`; runs `start_pump`, `stop_pump` and `set_direction`. `start_pump`: start the pump with its configured flow rate, target volume and mode (RUN); the reply prompt reports the resulting status. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/bgamari__harvard-syringe-pump
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/bgamari__harvard-syringe-pump --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "harvard-syringe-pump": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/bgamari__harvard-syringe-pump",
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

- **Reads:** `accumulated_volume`, `version`
- **Sets:** `diameter`, `flow_rate`, `target_volume`, `mode`

| Action | What it does |
| --- | --- |
| `start_pump` | Start the pump with its configured flow rate, target volume and mode (RUN); the reply prompt reports the resulting status |
| `stop_pump` | Stop the pump (STP), the safe state; the reply prompt reports the resulting status |
| `set_direction` | Select the pumping direction (DIR INF or DIR REF); the reply prompt reports the resulting status |

## Source and status

- Upstream: [bgamari/harvard-syringe-pump](https://github.com/bgamari/harvard-syringe-pump) at `d28b04fae069` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/bgamari__harvard-syringe-pump` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/bgamari__harvard-syringe-pump`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/bgamari__harvard-syringe-pump) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/bgamari__harvard-syringe-pump/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/bgamari__harvard-syringe-pump/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
