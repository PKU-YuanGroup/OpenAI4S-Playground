# INSTRUSTAR ISDS205B USB oscilloscope (instrustar.Scope)

`labs/gridinwork__ai-oscilloscope-isds205b` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

INSTRUSTAR ISDS205B USB oscilloscope (instrustar.Scope), adapted from gridinwork/ai-oscilloscope-isds205b. It reads `available`, `ch1_voltage_resolution_v`, `ch2_voltage_resolution_v`, `ch1_coupling_ac` and 8 more; sets `sample_rate_hz`, `generator_waveform`, `trigger_mode`, `trigger_style` and 3 more; runs `capture`, `set_input_range` and `generator_enable`. `capture`: capture one waveform on both channels and return per-channel scalar measurements. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/gridinwork__ai-oscilloscope-isds205b
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/gridinwork__ai-oscilloscope-isds205b --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ai-oscilloscope-isds205b": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/gridinwork__ai-oscilloscope-isds205b",
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

- **Reads:** `available`, `ch1_voltage_resolution_v`, `ch2_voltage_resolution_v`, `ch1_coupling_ac`, `ch2_coupling_ac`, `generator_enabled`, `has_hard_trigger`, `has_dds`, `has_io`, `has_pretrigger_percent`, `has_roll_mode`, `memory_length_kb`
- **Sets:** `sample_rate_hz`, `generator_waveform`, `trigger_mode`, `trigger_style`, `trigger_source`, `trigger_level_mv`, `trigger_pretrigger_percent`

| Action | What it does |
| --- | --- |
| `capture` | Capture one waveform on both channels and return per-channel scalar measurements |
| `set_input_range` | Request one channel's input range in mV and read back the voltage resolution the device reports |
| `generator_enable` | Enable or disable the DDS generator output |

## Source and status

- Upstream: [gridinwork/ai-oscilloscope-isds205b](https://github.com/gridinwork/ai-oscilloscope-isds205b) at `cb1bdda97869` (MIT); fetch it with `python3 scripts/add_device.py labs/gridinwork__ai-oscilloscope-isds205b` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/gridinwork__ai-oscilloscope-isds205b`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/gridinwork__ai-oscilloscope-isds205b) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/gridinwork__ai-oscilloscope-isds205b/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/gridinwork__ai-oscilloscope-isds205b/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
