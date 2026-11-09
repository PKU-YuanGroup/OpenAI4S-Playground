# RIGOL DG4202 signal source (WaveBench dg4202 driver)

`labs/scaxlibur__wavebench` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

RIGOL DG4202 signal source (WaveBench dg4202 driver), adapted from scaxlibur/wavebench. It reads `identity` and `amplitude_unit`; sets `output`, `function`, `frequency`, `amplitude` and 1 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/scaxlibur__wavebench
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/scaxlibur__wavebench --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "wavebench": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/scaxlibur__wavebench",
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

- **Reads:** `identity`, `amplitude_unit`
- **Sets:** `output`, `function`, `frequency`, `amplitude`, `duty_cycle`

## Source and status

- Upstream: [scaxlibur/wavebench](https://github.com/scaxlibur/wavebench) at `44506c4975d8` (MIT); fetch it with `python3 scripts/add_device.py labs/scaxlibur__wavebench` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/scaxlibur__wavebench`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/scaxlibur__wavebench) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/scaxlibur__wavebench/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/scaxlibur__wavebench/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
