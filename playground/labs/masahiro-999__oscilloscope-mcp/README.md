# RIGOL DS1000Z-series oscilloscope (RigolDs1000z)

`labs/masahiro-999__oscilloscope-mcp` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

RIGOL DS1000Z-series oscilloscope (RigolDs1000z), adapted from masahiro-999/oscilloscope-mcp. It reads `identity`, `active_channel_count`, `acquire_memory_depth`, `acquire_sample_rate` and 3 more; sets `channel_1_scale`, `channel_1_offset`, `channel_1_probe`, `channel_1_coupling` and 8 more; runs `measure` and `run_control`. `measure`: read the scope-side automatic measurements for one or more items on a channel. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/masahiro-999__oscilloscope-mcp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/masahiro-999__oscilloscope-mcp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "oscilloscope-mcp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/masahiro-999__oscilloscope-mcp",
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

- **Reads:** `identity`, `active_channel_count`, `acquire_memory_depth`, `acquire_sample_rate`, `trigger_mode`, `trigger_status`, `trigger_holdoff`
- **Sets:** `channel_1_scale`, `channel_1_offset`, `channel_1_probe`, `channel_1_coupling`, `channel_1_display`, `timebase_scale`, `timebase_offset`, `timebase_mode`, `acquire_type`, `acquire_averages`, `trigger_sweep`, `trigger_coupling`

| Action | What it does |
| --- | --- |
| `measure` | Read the scope-side automatic measurements for one or more items on a channel |
| `run_control` | Start, stop, arm a single acquisition, or force a trigger |

## Source and status

- Upstream: [masahiro-999/oscilloscope-mcp](https://github.com/masahiro-999/oscilloscope-mcp) at `e45773551e2b` (MIT); fetch it with `python3 scripts/add_device.py labs/masahiro-999__oscilloscope-mcp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/masahiro-999__oscilloscope-mcp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/masahiro-999__oscilloscope-mcp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/masahiro-999__oscilloscope-mcp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/masahiro-999__oscilloscope-mcp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
