# RIGOL MSO5000 series oscilloscope (pymso5000.Scope)

`labs/mabl__pymso5000` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

RIGOL MSO5000 series oscilloscope (pymso5000.Scope), adapted from mabl/pymso5000. It reads `identity`, `trigger_status`, `average_count`, `sample_rate` and 6 more; sets `acquisition_type`, `channel1_scale_per_div`, `channel1_offset`, `timebase_scale_s_per_div` and 2 more; runs `run`, `measure` and `configure_channel_input`. `run`: start continuous acquisition (the native RUN command). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/mabl__pymso5000
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/mabl__pymso5000 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymso5000": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/mabl__pymso5000",
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

- **Reads:** `identity`, `trigger_status`, `average_count`, `sample_rate`, `memory_depth_points`, `channel1_enabled`, `channel1_coupling`, `channel1_probe_ratio`, `channel1_bandwidth_limit`, `timebase_mode`
- **Sets:** `acquisition_type`, `channel1_scale_per_div`, `channel1_offset`, `timebase_scale_s_per_div`, `timebase_offset_s`, `memory_depth`

| Action | What it does |
| --- | --- |
| `run` | Start continuous acquisition (the native RUN command) |
| `measure` | Read one scalar automatic measurement item from one analog channel |
| `configure_channel_input` | Set the analog channel 1 display and input conditioning |

## Source and status

- Upstream: [mabl/pymso5000](https://github.com/mabl/pymso5000) at `48ebacc0317a` (MIT); fetch it with `python3 scripts/add_device.py labs/mabl__pymso5000` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/mabl__pymso5000`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/mabl__pymso5000) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/mabl__pymso5000/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/mabl__pymso5000/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
