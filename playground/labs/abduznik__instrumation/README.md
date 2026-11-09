# RIGOL DS1054Z oscilloscope

`labs/abduznik__instrumation` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence AGPL-3.0

RIGOL DS1054Z oscilloscope, adapted from abduznik/instrumation. It reads `identity`, `sample_rate`, `timebase_mode`, `timebase_offset` and 5 more; sets `acquire_type`, `timebase_scale`, `trigger_sweep`, `edge_trigger_source` and 6 more; runs `run`, `force_trigger` and `stop_acquisition`. `run`: start the acquisition (:RUN) and report the trigger status. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/abduznik__instrumation
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/abduznik__instrumation --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "instrumation": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/abduznik__instrumation",
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

- **Reads:** `identity`, `sample_rate`, `timebase_mode`, `timebase_offset`, `trigger_mode`, `trigger_status`, `ch1_offset`, `ch1_probe`, `ch1_invert`
- **Sets:** `acquire_type`, `timebase_scale`, `trigger_sweep`, `edge_trigger_source`, `edge_trigger_slope`, `edge_trigger_level`, `ch1_display`, `ch1_coupling`, `ch1_scale`, `ch1_bw_limit`

| Action | What it does |
| --- | --- |
| `run` | Start the acquisition (:RUN) and report the trigger status |
| `force_trigger` | Force a trigger event (:TFORce) and report the trigger status |
| `stop_acquisition` | Stop the acquisition (:STOP), the safe state, and report the trigger status |

## Source and status

- Upstream: [abduznik/instrumation](https://github.com/abduznik/instrumation) at `483d6d5d0b69` (AGPL-3.0); fetch it with `python3 scripts/add_device.py labs/abduznik__instrumation` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/abduznik__instrumation`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/abduznik__instrumation) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/abduznik__instrumation/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/abduznik__instrumation/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
