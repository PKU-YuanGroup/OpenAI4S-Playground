# Keithley 2230G multi-channel power supply

`labs/aaron-mott__keithley-2230g` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence NOASSERTION

Keithley 2230G multi-channel power supply, adapted from aaron-mott/keithley-2230g. It reads `measured_voltage_ch1`, `measured_voltage_ch2`, `measured_voltage_ch3`, `measured_current_ch1` and 2 more; sets `voltage_setpoint_ch1`, `voltage_setpoint_ch2`, `voltage_setpoint_ch3`, `current_limit_ch1` and 5 more; runs `output_off`. `output_off`: disable all three channel outputs (safe state). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/aaron-mott__keithley-2230g
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/aaron-mott__keithley-2230g --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "keithley-2230g": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/aaron-mott__keithley-2230g",
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

- **Reads:** `measured_voltage_ch1`, `measured_voltage_ch2`, `measured_voltage_ch3`, `measured_current_ch1`, `measured_current_ch2`, `measured_current_ch3`
- **Sets:** `voltage_setpoint_ch1`, `voltage_setpoint_ch2`, `voltage_setpoint_ch3`, `current_limit_ch1`, `current_limit_ch2`, `current_limit_ch3`, `output_ch1`, `output_ch2`, `output_ch3`

| Action | What it does |
| --- | --- |
| `output_off` | Disable all three channel outputs (safe state) |

## Source and status

- Upstream: [aaron-mott/keithley-2230g](https://github.com/aaron-mott/keithley-2230g) at `4c4d9024808f` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/aaron-mott__keithley-2230g` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/aaron-mott__keithley-2230g`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/aaron-mott__keithley-2230g) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/aaron-mott__keithley-2230g/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/aaron-mott__keithley-2230g/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
