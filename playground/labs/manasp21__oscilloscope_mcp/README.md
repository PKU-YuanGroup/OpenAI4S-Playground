# Oscilloscope MCP Ethernet backend (oscilloscope_mcp.EthernetOscilloscope)

`labs/manasp21__oscilloscope_mcp` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Oscilloscope MCP Ethernet backend (oscilloscope_mcp.EthernetOscilloscope), adapted from manasp21/oscilloscope_mcp. It reads `initialized`, `acquisition_active`, `channel_count`, `trigger_source` and 4 more; sets `sample_rate_hz`, `record_length`, `voltage_range_v`, `coupling` and 1 more; runs `configure_channel`, `setup_trigger`, `acquire_waveform` and `stop_acquisition`. `configure_channel`: configure one channel's voltage range, coupling and impedance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/manasp21__oscilloscope_mcp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/manasp21__oscilloscope_mcp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "oscilloscope_mcp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/manasp21__oscilloscope_mcp",
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

- **Reads:** `initialized`, `acquisition_active`, `channel_count`, `trigger_source`, `trigger_type`, `trigger_level_v`, `trigger_edge`, `trigger_holdoff_s`
- **Sets:** `sample_rate_hz`, `record_length`, `voltage_range_v`, `coupling`, `impedance`

| Action | What it does |
| --- | --- |
| `configure_channel` | Configure one channel's voltage range, coupling and impedance |
| `setup_trigger` | Configure the trigger source, type, level, edge and holdoff |
| `acquire_waveform` | Acquire one channel and report the scalar measurements of the captured trace |
| `stop_acquisition` | Stop the acquisition (the native safe state); it takes no input |

## Source and status

- Upstream: [manasp21/oscilloscope_mcp](https://github.com/manasp21/oscilloscope_mcp) at `49b9c4a7b06b` (MIT); fetch it with `python3 scripts/add_device.py labs/manasp21__oscilloscope_mcp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/manasp21__oscilloscope_mcp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/manasp21__oscilloscope_mcp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/manasp21__oscilloscope_mcp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/manasp21__oscilloscope_mcp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
