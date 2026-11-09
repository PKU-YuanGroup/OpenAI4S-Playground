# LCLS TPR trigger channel (pcdsdevices.TprTrigger)

`labs/pcdshub__pcdsdevices` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

LCLS TPR trigger channel (pcdsdevices.TprTrigger), adapted from pcdshub/pcdsdevices. It reads `channel_enabled`, `trigger_enabled`, `eventrate` and `label`; sets `delay_ns` and `width_ns`; runs `set_trigger_enabled`. `set_trigger_enabled`: enable or disable the configured TPR channel, its trigger output, or both. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pcdshub__pcdsdevices
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pcdshub__pcdsdevices --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pcdsdevices": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pcdshub__pcdsdevices",
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

- **Reads:** `channel_enabled`, `trigger_enabled`, `eventrate`, `label`
- **Sets:** `delay_ns`, `width_ns`

| Action | What it does |
| --- | --- |
| `set_trigger_enabled` | Enable or disable the configured TPR channel, its trigger output, or both |

## Source and status

- Upstream: [pcdshub/pcdsdevices](https://github.com/pcdshub/pcdsdevices) at `d13b06eb53e6` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/pcdshub__pcdsdevices` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pcdshub__pcdsdevices`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pcdshub__pcdsdevices) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pcdshub__pcdsdevices/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pcdshub__pcdsdevices/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
