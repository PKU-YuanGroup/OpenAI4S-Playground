# Keithley 2400 series source measure unit

`labs/natlabrockies__keithley_gpt` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Keithley 2400 series source measure unit, adapted from natlabrockies/keithley_gpt. It reads `identity`; sets `current_compliance`, `measure_current_range`, `measure_voltage_range`, `four_wire` and 4 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/natlabrockies__keithley_gpt
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/natlabrockies__keithley_gpt --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "keithley_gpt": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/natlabrockies__keithley_gpt",
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

- **Reads:** `identity`
- **Sets:** `current_compliance`, `measure_current_range`, `measure_voltage_range`, `four_wire`, `nplc_current`, `nplc_voltage`, `source_current_range`, `source_voltage_range`

## Source and status

- Upstream: [natlabrockies/keithley_gpt](https://github.com/natlabrockies/keithley_gpt) at `4cad464fd26e` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/natlabrockies__keithley_gpt` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/natlabrockies__keithley_gpt`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/natlabrockies__keithley_gpt) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/natlabrockies__keithley_gpt/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/natlabrockies__keithley_gpt/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
