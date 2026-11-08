# HP 89400 series vector signal analyzer (HP894xx.HP89400Device)

`labs/snhobbs__hp894xx` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence MIT

HP 89400 series vector signal analyzer (HP894xx.HP89400Device), adapted from snhobbs/hp894xx. It reads `center_frequency`, `span`, `x_units`, `y_units` and 5 more; runs `acquire_spectrum`, `abort_measurement` and `enable_autorange`. `acquire_spectrum`: read one trace: start a data read, return the Y values and the X/Y metadata the analyzer reports. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/snhobbs__hp894xx
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/snhobbs__hp894xx --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "hp894xx": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/snhobbs__hp894xx",
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

- **Reads:** `center_frequency`, `span`, `x_units`, `y_units`, `data_points`, `average_count`, `operating_condition`, `error_code`, `errors`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `acquire_spectrum` | Read one trace: start a data read, return the Y values and the X/Y metadata the analyzer reports |
| `abort_measurement` | Abort the measurement with the native abor write |
| `enable_autorange` | Enable or disable the input autorange with SENS:VOLT:RANGE:AUTO |

## Source and status

- Upstream: [snhobbs/hp894xx](https://github.com/snhobbs/hp894xx) at `6745a53c20fb` (MIT); fetch it with `python3 scripts/add_device.py labs/snhobbs__hp894xx` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/snhobbs__hp894xx`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/snhobbs__hp894xx) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/snhobbs__hp894xx/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/snhobbs__hp894xx/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
