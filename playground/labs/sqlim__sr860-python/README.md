# Stanford Research Systems SR860 DSP lock-in amplifier

`labs/sqlim__sr860-python` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Stanford Research Systems SR860 DSP lock-in amplifier, adapted from sqlim/sr860-python. It reads `time_constant_index`, `x`, `y`, `r` and 1 more; sets `frequency`, `amplitude`, `phase`, `dc_offset` and 10 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/sqlim__sr860-python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/sqlim__sr860-python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sr860-python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/sqlim__sr860-python",
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

- **Reads:** `time_constant_index`, `x`, `y`, `r`, `theta`
- **Sets:** `frequency`, `amplitude`, `phase`, `dc_offset`, `harmonic`, `time_constant`, `sync_filter_enable`, `adv_filter_enable`, `x_offset`, `y_offset`, `r_offset`, `x_offset_enable`, `y_offset_enable`, `r_offset_enable`

## Source and status

- Upstream: [sqlim/sr860-python](https://github.com/sqlim/sr860-python) at `00fa06645075` (MIT); fetch it with `python3 scripts/add_device.py labs/sqlim__sr860-python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/sqlim__sr860-python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/sqlim__sr860-python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/sqlim__sr860-python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/sqlim__sr860-python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
