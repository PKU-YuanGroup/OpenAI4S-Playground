# Keithley DAQ6510 data acquisition system (identity only)

`labs/croesnick__keithley-daq6510` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence MIT

Keithley DAQ6510 data acquisition system (identity only), adapted from croesnick/keithley-daq6510. It reads `idn` and `identify`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/croesnick__keithley-daq6510
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/croesnick__keithley-daq6510 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "keithley-daq6510": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/croesnick__keithley-daq6510",
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

- **Reads:** `idn`, `identify`
- **Sets:** —

## Source and status

- Upstream: [croesnick/keithley-daq6510](https://github.com/croesnick/keithley-daq6510) at `4c800f325a14` (MIT); fetch it with `python3 scripts/add_device.py labs/croesnick__keithley-daq6510` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/croesnick__keithley-daq6510`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/croesnick__keithley-daq6510) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/croesnick__keithley-daq6510/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/croesnick__keithley-daq6510/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
