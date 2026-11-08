# uSMU source-measure unit (usmu_py.USMU)

`labs/undalogic__usmu_py` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

uSMU source-measure unit (usmu_py.USMU), adapted from undalogic/usmu_py. It reads `identification` and `adc_0_1`; runs `configure`, `iv_point` and `output`. `configure`: set the oversample rate and lock the current range; the native class has no query for either setting, so the applied values are returned. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/undalogic__usmu_py
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/undalogic__usmu_py --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "usmu_py": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/undalogic__usmu_py",
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

- **Reads:** `identification`, `adc_0_1`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `configure` | Set the oversample rate and lock the current range; the native class has no query for either setting, so the applied values are returned |
| `iv_point` | Set the current limit, source the voltage and return the voltage and current the device measures for that point |
| `output` | Enable or disable the output: CH1:ENA enables it, CH1:DIS disables it into the high-impedance state |

## Source and status

- Upstream: [undalogic/usmu_py](https://github.com/undalogic/usmu_py) at `345dc809f971` (MIT); fetch it with `python3 scripts/add_device.py labs/undalogic__usmu_py` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/undalogic__usmu_py`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/undalogic__usmu_py) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/undalogic__usmu_py/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/undalogic__usmu_py/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
