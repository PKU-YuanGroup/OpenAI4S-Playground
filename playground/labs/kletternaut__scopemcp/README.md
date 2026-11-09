# Owon/Abestop DS1102 oscilloscope (ds1102_mcp.ScopeController)

`labs/kletternaut__scopemcp` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Owon/Abestop DS1102 oscilloscope (ds1102_mcp.ScopeController), adapted from kletternaut/scopemcp. It reads `instrument_model`, `run_status`, `channel1_frequency_hz`, `channel1_offset_raw` and 4 more; sets `channel1_scale`, `channel1_coupling`, `channel1_offset_v`, `horizontal_scale` and 4 more; runs `autoset`, `run` and `stop_acquisition`. `autoset`: run the scope's automatic setup (:AUToset on). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/kletternaut__scopemcp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/kletternaut__scopemcp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "scopemcp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/kletternaut__scopemcp",
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

- **Reads:** `instrument_model`, `run_status`, `channel1_frequency_hz`, `channel1_offset_raw`, `channel2_frequency_hz`, `channel2_scale`, `channel2_coupling`, `channel2_offset_raw`
- **Sets:** `channel1_scale`, `channel1_coupling`, `channel1_offset_v`, `horizontal_scale`, `trigger_mode`, `trigger_slope`, `trigger_source`, `trigger_level_mv`

| Action | What it does |
| --- | --- |
| `autoset` | Run the scope's automatic setup (:AUToset on) |
| `run` | Start continuous acquisition (:run) |
| `stop_acquisition` | Stop the acquisition (:stop, the safe state); it takes no input |

## Source and status

- Upstream: [kletternaut/scopemcp](https://github.com/kletternaut/scopemcp) at `a932b777694d` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/kletternaut__scopemcp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/kletternaut__scopemcp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/kletternaut__scopemcp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/kletternaut__scopemcp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/kletternaut__scopemcp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
