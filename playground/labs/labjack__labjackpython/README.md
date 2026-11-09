# LabJack U3 USB DAQ (LabJackPython U3)

`labs/labjack__labjackpython` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

LabJack U3 USB DAQ (LabJackPython U3), adapted from labjack/labjackpython. It reads `analog_input_0`, `internal_temperature`, `dio_states` and `measure_voltage`; sets `fio_analog` and `eio_analog`; runs `set_digital_output` and `reset_device`. `set_digital_output`: drive one U3 digital I/O line high or low; the line is also set to output. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/labjack__labjackpython
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/labjack__labjackpython --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "labjackpython": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/labjack__labjackpython",
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

- **Reads:** `analog_input_0`, `internal_temperature`, `dio_states`, `measure_voltage`
- **Sets:** `fio_analog`, `eio_analog`

| Action | What it does |
| --- | --- |
| `set_digital_output` | Drive one U3 digital I/O line high or low; the line is also set to output |
| `reset_device` | Soft-reset the U3 to its power-up state (the native reset); it takes no input |

## Source and status

- Upstream: [labjack/labjackpython](https://github.com/labjack/labjackpython) at `a2f13eb548cc` (MIT); fetch it with `python3 scripts/add_device.py labs/labjack__labjackpython` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/labjack__labjackpython`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/labjack__labjackpython) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/labjack__labjackpython/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/labjack__labjackpython/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
