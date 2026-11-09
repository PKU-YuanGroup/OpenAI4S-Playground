# NI-DAQmx analog output (PyMoDAQ DAQ_NIDAQmx_Actuator)

`labs/pymodaq__pymodaq_plugins_daqmx` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

NI-DAQmx analog output (PyMoDAQ DAQ_NIDAQmx_Actuator), adapted from pymodaq/pymodaq_plugins_daqmx. It reads `device`, `analog_output_max_rate`, `analog_input_max_rate`, `analog_triggering_supported` and 2 more; sets `analog_output`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pymodaq__pymodaq_plugins_daqmx
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pymodaq__pymodaq_plugins_daqmx --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pymodaq_plugins_daqmx": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pymodaq__pymodaq_plugins_daqmx",
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

- **Reads:** `device`, `analog_output_max_rate`, `analog_input_max_rate`, `analog_triggering_supported`, `trigger_source_count`, `last_write_index`
- **Sets:** `analog_output`

## Source and status

- Upstream: [pymodaq/pymodaq_plugins_daqmx](https://github.com/pymodaq/pymodaq_plugins_daqmx) at `f2129a920a64` (MIT); fetch it with `python3 scripts/add_device.py labs/pymodaq__pymodaq_plugins_daqmx` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pymodaq__pymodaq_plugins_daqmx`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_daqmx) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pymodaq__pymodaq_plugins_daqmx/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pymodaq__pymodaq_plugins_daqmx/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
