# Benning MM12 digital multimeter

`labs/urmel79__jupyter_pyvisa_lab` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence GPL-3.0

Benning MM12 digital multimeter, adapted from urmel79/jupyter_pyvisa_lab. It reads `device_model`, `device_serial`, `model_id`, `firmware_version` and 6 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/urmel79__jupyter_pyvisa_lab
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/urmel79__jupyter_pyvisa_lab --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "jupyter_pyvisa_lab": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/urmel79__jupyter_pyvisa_lab",
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

- **Reads:** `device_model`, `device_serial`, `model_id`, `firmware_version`, `function`, `value_base`, `base_unit`, `value_display`, `display_unit`, `read_display`
- **Sets:** —

## Source and status

- Upstream: [urmel79/jupyter_pyvisa_lab](https://github.com/urmel79/jupyter_pyvisa_lab) at `418a7f6bbef1` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/urmel79__jupyter_pyvisa_lab` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/urmel79__jupyter_pyvisa_lab`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/urmel79__jupyter_pyvisa_lab) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/urmel79__jupyter_pyvisa_lab/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/urmel79__jupyter_pyvisa_lab/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
