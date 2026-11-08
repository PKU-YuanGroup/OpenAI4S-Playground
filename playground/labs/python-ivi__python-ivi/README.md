# LeCroy WaveRunner 104MXi-A oscilloscope

`labs/python-ivi__python-ivi` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

LeCroy WaveRunner 104MXi-A oscilloscope, adapted from python-ivi/python-ivi. It reads `measurement_frequency`, `measurement_period` and `measurement_vpp`; sets `trigger_mode`, `acquisition_type`, `sample_mode`, `acquisition_averages` and 2 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/python-ivi__python-ivi
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/python-ivi__python-ivi --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "python-ivi": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/python-ivi__python-ivi",
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

- **Reads:** `measurement_frequency`, `measurement_period`, `measurement_vpp`
- **Sets:** `trigger_mode`, `acquisition_type`, `sample_mode`, `acquisition_averages`, `timebase_mode`, `timebase_reference`

## Source and status

- Upstream: [python-ivi/python-ivi](https://github.com/python-ivi/python-ivi) at `cfa45ceade07` (MIT); fetch it with `python3 scripts/add_device.py labs/python-ivi__python-ivi` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/python-ivi__python-ivi`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/python-ivi__python-ivi) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/python-ivi__python-ivi/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/python-ivi__python-ivi/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
