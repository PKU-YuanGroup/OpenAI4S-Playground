# Siglent SPD3303 series power supply (instro.psu.drivers.siglent_spd3303.SiglentSPD3303)

`labs/nominal-io__instro` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence Apache-2.0

Siglent SPD3303 series power supply (instro.psu.drivers.siglent_spd3303.SiglentSPD3303), adapted from nominal-io/instro. It reads `voltage_ch1`, `current_ch1`, `regulation_mode_ch1`, `voltage_ch2` and 3 more; sets `voltage_setpoint_ch1`, `current_setpoint_ch1`, `output_enabled_ch1`, `voltage_setpoint_ch2` and 2 more; runs `output_off`. `output_off`: disable both channel outputs (OUTP CH1,OFF and OUTP CH2,OFF); it takes no input and is the declared safe state. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/nominal-io__instro
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/nominal-io__instro --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "instro": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/nominal-io__instro",
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

- **Reads:** `voltage_ch1`, `current_ch1`, `regulation_mode_ch1`, `voltage_ch2`, `current_ch2`, `regulation_mode_ch2`, `psu_mode`
- **Sets:** `voltage_setpoint_ch1`, `current_setpoint_ch1`, `output_enabled_ch1`, `voltage_setpoint_ch2`, `current_setpoint_ch2`, `output_enabled_ch2`

| Action | What it does |
| --- | --- |
| `output_off` | Disable both channel outputs (OUTP CH1,OFF and OUTP CH2,OFF); it takes no input and is the declared safe state |

## Source and status

- Upstream: [nominal-io/instro](https://github.com/nominal-io/instro) at `311aee4ae227` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/nominal-io__instro` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/nominal-io__instro`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/nominal-io__instro) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/nominal-io__instro/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/nominal-io__instro/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
