# Hantek 1008C eight-channel USB instrument (pyhantek1008C.Hantek1008)

`labs/vadter__hantek1008c` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Hantek 1008C eight-channel USB instrument (pyhantek1008C.Hantek1008), adapted from vadter/hantek1008c. It reads `active_channels`, `time`, `vscales`, `generator_waveform_max_length` and 1 more; sets `generator_on` and `generator_speed`; runs `set_generator_waveform`, `pause`, `resume` and `generator_off`. `set_generator_waveform`: send a generator waveform: one byte per part of the wave, each bit an output. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/vadter__hantek1008c
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/vadter__hantek1008c --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "hantek1008c": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/vadter__hantek1008c",
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

- **Reads:** `active_channels`, `time`, `vscales`, `generator_waveform_max_length`, `paused`
- **Sets:** `generator_on`, `generator_speed`

| Action | What it does |
| --- | --- |
| `set_generator_waveform` | Send a generator waveform: one byte per part of the wave, each bit an output |
| `pause` | Start the upstream keep-alive pause thread that pings the instrument every 0.01 s |
| `resume` | Stop the upstream keep-alive pause thread |
| `generator_off` | Switch the generator off and stop the keep-alive pause thread (the safe state) |

## Source and status

- Upstream: [vadter/hantek1008c](https://github.com/vadter/hantek1008c) at `178773a7a716` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/vadter__hantek1008c` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/vadter__hantek1008c`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/vadter__hantek1008c) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/vadter__hantek1008c/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/vadter__hantek1008c/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
