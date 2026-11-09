# Agilent 33220A arbitrary waveform generator

`labs/alexshkarin__pylablib-v0` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Agilent 33220A arbitrary waveform generator, adapted from alexshkarin/pylablib-v0. It sets `amplitude`, `frequency`, `offset`, `phase` and 5 more; runs `output_off`. `output_off`: disable the generator output (the safe state); it takes no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/alexshkarin__pylablib-v0
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/alexshkarin__pylablib-v0 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pylablib-v0": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/alexshkarin__pylablib-v0",
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

- **Reads:** —
- **Sets:** `amplitude`, `frequency`, `offset`, `phase`, `function`, `duty_cycle`, `burst_enabled`, `burst_mode`, `output`

| Action | What it does |
| --- | --- |
| `output_off` | Disable the generator output (the safe state); it takes no input |

## Source and status

- Upstream: [alexshkarin/pylablib-v0](https://github.com/alexshkarin/pylablib-v0) at `1c3c59d4bcbe` (MIT); fetch it with `python3 scripts/add_device.py labs/alexshkarin__pylablib-v0` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/alexshkarin__pylablib-v0`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/alexshkarin__pylablib-v0) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/alexshkarin__pylablib-v0/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/alexshkarin__pylablib-v0/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
