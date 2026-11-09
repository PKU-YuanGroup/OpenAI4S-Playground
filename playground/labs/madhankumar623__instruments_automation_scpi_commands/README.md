# Programmable DC power supply (PowerSupply_Automation.py, DCsupply_1)

`labs/madhankumar623__instruments_automation_scpi_commands` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Programmable DC power supply (PowerSupply_Automation.py, DCsupply_1), adapted from madhankumar623/instruments_automation_scpi_commands. It reads `voltage_ch2`, `current_ch2`, `voltage_ch3` and `current_ch3`; sets `voltage_setpoint_ch2`, `current_setpoint_ch2`, `output_enabled_ch2`, `voltage_setpoint_ch3` and 2 more; runs `output_off`. `output_off`: switch both controlled channel outputs of DCsupply_1 off (INST:NSEL 2;OUTP OFF and INST:NSEL 3;OUTP OFF); it takes no input and is the declared safe state. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/madhankumar623__instruments_automation_scpi_commands
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/madhankumar623__instruments_automation_scpi_commands --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "instruments_automation_scpi_commands": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/madhankumar623__instruments_automation_scpi_commands",
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

- **Reads:** `voltage_ch2`, `current_ch2`, `voltage_ch3`, `current_ch3`
- **Sets:** `voltage_setpoint_ch2`, `current_setpoint_ch2`, `output_enabled_ch2`, `voltage_setpoint_ch3`, `current_setpoint_ch3`, `output_enabled_ch3`

| Action | What it does |
| --- | --- |
| `output_off` | Switch both controlled channel outputs of DCsupply_1 off (INST:NSEL 2;OUTP OFF and INST:NSEL 3;OUTP OFF); it takes no input and is the declared safe state |

## Source and status

- Upstream: [madhankumar623/instruments_automation_scpi_commands](https://github.com/madhankumar623/instruments_automation_scpi_commands) at `2080effa969d` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/madhankumar623__instruments_automation_scpi_commands` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/madhankumar623__instruments_automation_scpi_commands`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/madhankumar623__instruments_automation_scpi_commands) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/madhankumar623__instruments_automation_scpi_commands/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/madhankumar623__instruments_automation_scpi_commands/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
