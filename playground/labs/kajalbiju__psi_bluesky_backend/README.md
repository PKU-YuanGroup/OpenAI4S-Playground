# Oxford Instruments Mercury iTC temperature controller (PSI Bluesky4)

`labs/kajalbiju__psi_bluesky_backend` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Oxford Instruments Mercury iTC temperature controller (PSI Bluesky4), adapted from kajalbiju/psi_bluesky_backend. It reads `temperature`; sets `temperature_setpoint`, `heater_setpoint`, `p_value`, `i_value` and 1 more; runs `heater_off`. `heater_off`: drive the temperature-loop setpoint to 0 K and the heater-loop setpoint to 0 (the safe state); it takes no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/kajalbiju__psi_bluesky_backend
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/kajalbiju__psi_bluesky_backend --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "psi_bluesky_backend": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/kajalbiju__psi_bluesky_backend",
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

- **Reads:** `temperature`
- **Sets:** `temperature_setpoint`, `heater_setpoint`, `p_value`, `i_value`, `d_value`

| Action | What it does |
| --- | --- |
| `heater_off` | Drive the temperature-loop setpoint to 0 K and the heater-loop setpoint to 0 (the safe state); it takes no input |

## Source and status

- Upstream: [kajalbiju/psi_bluesky_backend](https://github.com/kajalbiju/psi_bluesky_backend) at `59252b014ef3` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/kajalbiju__psi_bluesky_backend` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/kajalbiju__psi_bluesky_backend`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/kajalbiju__psi_bluesky_backend) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/kajalbiju__psi_bluesky_backend/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/kajalbiju__psi_bluesky_backend/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
