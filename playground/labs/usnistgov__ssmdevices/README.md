# Mini-Circuits RCDAT USB switch attenuator

`labs/usnistgov__ssmdevices` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NIST-PD

Mini-Circuits RCDAT USB switch attenuator, adapted from usnistgov/ssmdevices. It reads `part_number` and `serial_number`; sets `attenuation_setting`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/usnistgov__ssmdevices
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/usnistgov__ssmdevices --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ssmdevices": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/usnistgov__ssmdevices",
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

- **Reads:** `part_number`, `serial_number`
- **Sets:** `attenuation_setting`

## Source and status

- Upstream: [usnistgov/ssmdevices](https://github.com/usnistgov/ssmdevices) at `4680dde88566` (NIST-PD); fetch it with `python3 scripts/add_device.py labs/usnistgov__ssmdevices` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/usnistgov__ssmdevices`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/usnistgov__ssmdevices) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/usnistgov__ssmdevices/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/usnistgov__ssmdevices/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
