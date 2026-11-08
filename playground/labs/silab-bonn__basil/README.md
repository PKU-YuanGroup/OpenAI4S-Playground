# ISEG SHQ/NQH series high-voltage supply

`labs/silab-bonn__basil` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence BSD-3-Clause

ISEG SHQ/NQH series high-voltage supply, adapted from silab-bonn/basil. It reads `voltage` and `current`; sets `voltage_target`, `ramp_speed`, `answer_delay`, `autostart` and 1 more; runs `output_off`. `output_off`: set the channel's target voltage to 0 V (the upstream off()), the safe state of the supply. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/silab-bonn__basil
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/silab-bonn__basil --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "basil": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/silab-bonn__basil",
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

- **Reads:** `voltage`, `current`
- **Sets:** `voltage_target`, `ramp_speed`, `answer_delay`, `autostart`, `channel`

| Action | What it does |
| --- | --- |
| `output_off` | Set the channel's target voltage to 0 V (the upstream off()), the safe state of the supply |

## Source and status

- Upstream: [silab-bonn/basil](https://github.com/silab-bonn/basil) at `0630d8fd717f` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/silab-bonn__basil` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/silab-bonn__basil`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/silab-bonn__basil) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/silab-bonn__basil/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/silab-bonn__basil/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
