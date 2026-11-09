# Tektronix AFG1000/AFG3000 arbitrary function generator

`labs/asvela__tektronix-func-gen` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Tektronix AFG1000/AFG3000 arbitrary function generator, adapted from asvela/tektronix-func-gen. It reads `error_queue` and `waveform_catalogue`; sets `output_ch1`, `output_ch2`, `function_ch1`, `function_ch2` and 7 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/asvela__tektronix-func-gen
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/asvela__tektronix-func-gen --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tektronix-func-gen": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/asvela__tektronix-func-gen",
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

- **Reads:** `error_queue`, `waveform_catalogue`
- **Sets:** `output_ch1`, `output_ch2`, `function_ch1`, `function_ch2`, `amplitude_ch1`, `amplitude_ch2`, `offset_ch1`, `offset_ch2`, `frequency_ch1`, `frequency_ch2`, `frequency_lock`

## Source and status

- Upstream: [asvela/tektronix-func-gen](https://github.com/asvela/tektronix-func-gen) at `30f7406e89bd` (MIT); fetch it with `python3 scripts/add_device.py labs/asvela__tektronix-func-gen` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/asvela__tektronix-func-gen`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/asvela__tektronix-func-gen) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/asvela__tektronix-func-gen/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/asvela__tektronix-func-gen/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
