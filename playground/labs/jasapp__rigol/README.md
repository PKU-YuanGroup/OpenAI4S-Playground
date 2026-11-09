# RIGOL DP832A triple-channel DC power supply

`labs/jasapp__rigol` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

RIGOL DP832A triple-channel DC power supply, adapted from jasapp/rigol. It reads `voltage_ch1`, `current_ch1`, `power_ch1`, `voltage_ch2` and 5 more; sets `output_ch1`, `voltage_setpoint_ch1`, `current_setpoint_ch1`, `output_ch2` and 5 more; runs `set_ovp` and `set_ocp`. `set_ovp`: set the over-voltage protection threshold of one channel and enable it (:OUTP:OVP). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/jasapp__rigol
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/jasapp__rigol --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "rigol": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/jasapp__rigol",
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

- **Reads:** `voltage_ch1`, `current_ch1`, `power_ch1`, `voltage_ch2`, `current_ch2`, `power_ch2`, `voltage_ch3`, `current_ch3`, `power_ch3`
- **Sets:** `output_ch1`, `voltage_setpoint_ch1`, `current_setpoint_ch1`, `output_ch2`, `voltage_setpoint_ch2`, `current_setpoint_ch2`, `output_ch3`, `voltage_setpoint_ch3`, `current_setpoint_ch3`

| Action | What it does |
| --- | --- |
| `set_ovp` | Set the over-voltage protection threshold of one channel and enable it (:OUTP:OVP) |
| `set_ocp` | Set the over-current protection threshold of one channel and enable it (:OUTP:OCP) |

## Source and status

- Upstream: [jasapp/rigol](https://github.com/jasapp/rigol) at `602b8623f820` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/jasapp__rigol` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/jasapp__rigol`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/jasapp__rigol) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/jasapp__rigol/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/jasapp__rigol/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
