# SRS SR830 lock-in amplifier

`labs/ludwigregalado__lock-in_sr830` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

SRS SR830 lock-in amplifier, adapted from ludwigregalado/lock-in_sr830. It reads `x`, `y`, `r`, `theta` and 2 more; sets `frequency`, `amplitude`, `input_config`, `ground` and 6 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ludwigregalado__lock-in_sr830
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ludwigregalado__lock-in_sr830 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "lock-in_sr830": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ludwigregalado__lock-in_sr830",
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

- **Reads:** `x`, `y`, `r`, `theta`, `phase`, `identity`
- **Sets:** `frequency`, `amplitude`, `input_config`, `ground`, `coupling`, `line_filter`, `reserve`, `time_constant_index`, `slope`, `sync`

## Source and status

- Upstream: [ludwigregalado/lock-in_sr830](https://github.com/ludwigregalado/lock-in_sr830) at `fbd78df88f25` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/ludwigregalado__lock-in_sr830` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ludwigregalado__lock-in_sr830`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ludwigregalado__lock-in_sr830) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ludwigregalado__lock-in_sr830/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ludwigregalado__lock-in_sr830/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
