# Hantek 1008C USB oscilloscope (hantek1008.Hantek1008)

`labs/mfg92__hantek1008py` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence Apache-2.0

Hantek 1008C USB oscilloscope (hantek1008.Hantek1008), adapted from mfg92/hantek1008py. It reads `active_channels`, `vertical_scales`, `zero_offsets`, `paused` and 1 more; runs `set_generator_on`, `set_generator_speed`, `set_generator_waveform`, `set_paused` and 1 more. `set_generator_on`: enable or disable the eight digital waveform-generator outputs. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/mfg92__hantek1008py
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/mfg92__hantek1008py --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "hantek1008py": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/mfg92__hantek1008py",
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

- **Reads:** `active_channels`, `vertical_scales`, `zero_offsets`, `paused`, `generator_waveform_max_length`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_generator_on` | Enable or disable the eight digital waveform-generator outputs |
| `set_generator_speed` | Set the generator speed in revolutions per minute |
| `set_generator_waveform` | Upload a waveform as bytes; bit i of each byte is digital output i |
| `set_paused` | Start or stop the USB keep-alive pause thread |
| `generator_off` | Disable the waveform generator outputs (the safe state); it takes no input |

## Source and status

- Upstream: [mfg92/hantek1008py](https://github.com/mfg92/hantek1008py) at `302e45ad9d47` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/mfg92__hantek1008py` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/mfg92__hantek1008py`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/mfg92__hantek1008py) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/mfg92__hantek1008py/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/mfg92__hantek1008py/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
