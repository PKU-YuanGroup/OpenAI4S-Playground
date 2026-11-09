# Keithley 2450 source-measure unit

`labs/yongxb__keithley-smu-controls` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence NOASSERTION

Keithley 2450 source-measure unit, adapted from yongxb/keithley-smu-controls. It reads `voltage` and `current`; sets `source_current`, `compliance_voltage` and `output`; runs `safe_state`. `safe_state`: disable the source output and set the source current to zero. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/yongxb__keithley-smu-controls
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/yongxb__keithley-smu-controls --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "keithley-smu-controls": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/yongxb__keithley-smu-controls",
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
- **Sets:** `source_current`, `compliance_voltage`, `output`

| Action | What it does |
| --- | --- |
| `safe_state` | Disable the source output and set the source current to zero |

## Source and status

- Upstream: [yongxb/keithley-smu-controls](https://github.com/yongxb/keithley-smu-controls) at `6afb567c2912` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/yongxb__keithley-smu-controls` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/yongxb__keithley-smu-controls`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/yongxb__keithley-smu-controls) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/yongxb__keithley-smu-controls/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/yongxb__keithley-smu-controls/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
