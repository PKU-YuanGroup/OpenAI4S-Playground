# LabJack U12 USB DAQ (Lantz U12)

`labs/labpy__lantz` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

LabJack U12 USB DAQ (Lantz U12), adapted from labpy/lantz. It reads `driver_version`, `firmware_version`, `analog_input_0`, `counter` and 2 more; sets `local_id`; runs `sample_voltages`, `set_analog_outputs`, `pulse_out` and `reset_device`. `sample_voltages`: acquire a block of analog input scans from channel 0 with aiBurst. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/labpy__lantz
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/labpy__lantz --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "lantz": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/labpy__lantz",
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

- **Reads:** `driver_version`, `firmware_version`, `analog_input_0`, `counter`, `streaming`, `measure_voltage`
- **Sets:** `local_id`

| Action | What it does |
| --- | --- |
| `sample_voltages` | Acquire a block of analog input scans from channel 0 with aiBurst |
| `set_analog_outputs` | Set both analog output voltages (U12.eAnalogOut) |
| `pulse_out` | Start a pulse train on the selected D0-D7 bits (U12.pulseOutStart) |
| `reset_device` | Reset the U12 (U12.reset), the safe state; it takes no input |

## Source and status

- Upstream: [labpy/lantz](https://github.com/labpy/lantz) at `3e878e3f765a` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/labpy__lantz` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/labpy__lantz`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/labpy__lantz) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/labpy__lantz/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/labpy__lantz/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
