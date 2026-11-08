# Tektronix TDS 3052 oscilloscope

`labs/samdejong86__tektronix-serial-daq-python` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Tektronix TDS 3052 oscilloscope, adapted from samdejong86/tektronix-serial-daq-python. It sets `ch1_scale`, `ch2_scale`, `coupling_ch1`, `coupling_ch2` and 8 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/samdejong86__tektronix-serial-daq-python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/samdejong86__tektronix-serial-daq-python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tektronix-serial-daq-python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/samdejong86__tektronix-serial-daq-python",
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
- **Sets:** `ch1_scale`, `ch2_scale`, `coupling_ch1`, `coupling_ch2`, `horizontal_scale`, `impedance_ch1`, `impedance_ch2`, `record_length`, `trigger_level`, `trigger_position`, `trigger_source`, `trigger_slope`

## Source and status

- Upstream: [samdejong86/tektronix-serial-daq-python](https://github.com/samdejong86/tektronix-serial-daq-python) at `e7728bc44030` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/samdejong86__tektronix-serial-daq-python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/samdejong86__tektronix-serial-daq-python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/samdejong86__tektronix-serial-daq-python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/samdejong86__tektronix-serial-daq-python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/samdejong86__tektronix-serial-daq-python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
