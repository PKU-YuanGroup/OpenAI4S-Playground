# Tektronix MDO3000 series oscilloscope (tekinstr.Oscilloscope)

`labs/l-johnston__tekinstr` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Tektronix MDO3000 series oscilloscope (tekinstr.Oscilloscope), adapted from l-johnston/tekinstr. It reads `sample_rate`, `acquisition_count` and `trigger_state`; sets `record_length`, `horizontal_scale`, `horizontal_delay_mode`, `acquisition_mode` and 3 more; runs `force_trigger`. `force_trigger`: force a trigger event and report the trigger state afterwards. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/l-johnston__tekinstr
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/l-johnston__tekinstr --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tekinstr": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/l-johnston__tekinstr",
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

- **Reads:** `sample_rate`, `acquisition_count`, `trigger_state`
- **Sets:** `record_length`, `horizontal_scale`, `horizontal_delay_mode`, `acquisition_mode`, `num_averages`, `acquisition_state`, `single_acquisition`

| Action | What it does |
| --- | --- |
| `force_trigger` | Force a trigger event and report the trigger state afterwards |

## Source and status

- Upstream: [l-johnston/tekinstr](https://github.com/l-johnston/tekinstr) at `7949430c1a68` (MIT); fetch it with `python3 scripts/add_device.py labs/l-johnston__tekinstr` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/l-johnston__tekinstr`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/l-johnston__tekinstr) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/l-johnston__tekinstr/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/l-johnston__tekinstr/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
