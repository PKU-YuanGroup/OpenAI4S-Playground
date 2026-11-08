# NI PXIe oscilloscope (niscope DirectBackend)

`labs/ymzds__niscope-mcp` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

NI PXIe oscilloscope (niscope DirectBackend), adapted from ymzds/niscope-mcp. It reads `device_model`; sets `channel_enabled`, `vertical_range`, `vertical_offset`, `vertical_coupling` and 7 more; runs `measure_waveform` and `auto_setup`. `measure_waveform`: acquire one channel and return its scalar waveform measurements. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ymzds__niscope-mcp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ymzds__niscope-mcp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "niscope-mcp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ymzds__niscope-mcp",
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

- **Reads:** `device_model`
- **Sets:** `channel_enabled`, `vertical_range`, `vertical_offset`, `vertical_coupling`, `probe_attenuation`, `input_impedance`, `sample_rate`, `record_length`, `trigger_source`, `trigger_level`, `trigger_slope`

| Action | What it does |
| --- | --- |
| `measure_waveform` | Acquire one channel and return its scalar waveform measurements |
| `auto_setup` | Run the native oscilloscope auto setup (Autoset) |

## Source and status

- Upstream: [ymzds/niscope-mcp](https://github.com/ymzds/niscope-mcp) at `75a3a09bb6ea` (MIT); fetch it with `python3 scripts/add_device.py labs/ymzds__niscope-mcp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ymzds__niscope-mcp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ymzds__niscope-mcp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ymzds__niscope-mcp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ymzds__niscope-mcp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
