# Thorlabs PM100D optical power meter (QCoDeS contrib driver)

`labs/qcodes__qcodes_contrib_drivers` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Thorlabs PM100D optical power meter (QCoDeS contrib driver), adapted from qcodes/qcodes_contrib_drivers. It reads `power`, `attenuation`, `averaging`, `zero_value` and 1 more; sets `power_range` and `auto_range`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/qcodes__qcodes_contrib_drivers
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/qcodes__qcodes_contrib_drivers --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "qcodes_contrib_drivers": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/qcodes__qcodes_contrib_drivers",
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

- **Reads:** `power`, `attenuation`, `averaging`, `zero_value`, `current_range`
- **Sets:** `power_range`, `auto_range`

## Source and status

- Upstream: [qcodes/qcodes_contrib_drivers](https://github.com/qcodes/qcodes_contrib_drivers) at `187164d608ed` (MIT); fetch it with `python3 scripts/add_device.py labs/qcodes__qcodes_contrib_drivers` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/qcodes__qcodes_contrib_drivers`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/qcodes__qcodes_contrib_drivers) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/qcodes__qcodes_contrib_drivers/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/qcodes__qcodes_contrib_drivers/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
