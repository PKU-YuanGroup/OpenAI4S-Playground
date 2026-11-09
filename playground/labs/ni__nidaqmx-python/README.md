# NI-DAQmx analog input task (voltage measurement)

`labs/ni__nidaqmx-python` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

NI-DAQmx analog input task (voltage measurement), adapted from ni/nidaqmx-python. It reads `task_done`, `channel_name` and `measure_voltage`; runs `sample_voltages`, `start_task` and `stop_task`. `sample_voltages`: acquire a block of voltage samples from the analog input task. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ni__nidaqmx-python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ni__nidaqmx-python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "nidaqmx-python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ni__nidaqmx-python",
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

- **Reads:** `task_done`, `channel_name`, `measure_voltage`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `sample_voltages` | Acquire a block of voltage samples from the analog input task |
| `start_task` | Start the task (the native start) so it begins the measurement |
| `stop_task` | Stop the task (the native stop, the safe state); it takes no input |

## Source and status

- Upstream: [ni/nidaqmx-python](https://github.com/ni/nidaqmx-python) at `04211cd36322` (MIT); fetch it with `python3 scripts/add_device.py labs/ni__nidaqmx-python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ni__nidaqmx-python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ni__nidaqmx-python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ni__nidaqmx-python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ni__nidaqmx-python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
