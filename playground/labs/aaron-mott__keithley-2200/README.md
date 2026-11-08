# Keithley 2200 series programmable DC power supply (KEI2220S)

`labs/aaron-mott__keithley-2200` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence NOASSERTION

Keithley 2200 series programmable DC power supply (KEI2220S), adapted from aaron-mott/keithley-2200. It reads `measured_voltage`, `measured_current` and `measured_power`; sets `voltage`, `current`, `output`, `overvoltage_protection` and 1 more; runs `output_off`. `output_off`: disable the output with OUTP OFF (the declared safe state); no input, no output. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/aaron-mott__keithley-2200
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/aaron-mott__keithley-2200 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "keithley-2200": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/aaron-mott__keithley-2200",
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

- **Reads:** `measured_voltage`, `measured_current`, `measured_power`
- **Sets:** `voltage`, `current`, `output`, `overvoltage_protection`, `overvoltage_protection_enabled`

| Action | What it does |
| --- | --- |
| `output_off` | Disable the output with OUTP OFF (the declared safe state); no input, no output |

## Source and status

- Upstream: [aaron-mott/keithley-2200](https://github.com/aaron-mott/keithley-2200) at `348fb5df70d9` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/aaron-mott__keithley-2200` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/aaron-mott__keithley-2200`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/aaron-mott__keithley-2200) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/aaron-mott__keithley-2200/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/aaron-mott__keithley-2200/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
