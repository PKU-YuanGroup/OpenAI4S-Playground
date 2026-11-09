# New Era syringe pump (nesp-lib Pump)

`labs/florian-lapp__nesp-lib-py` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

New Era syringe pump (nesp-lib Pump), adapted from florian-lapp/nesp-lib-py. It reads `model_number`, `firmware_version`, `status`, `running` and 2 more; sets `syringe_diameter_mm`, `pumping_direction`, `pumping_volume_ml`, `pumping_rate_ml_per_min` and 1 more; runs `run_pump`, `purge` and `stop_pump`. `run_pump`: start the pump with the configured direction, volume and rate (Pump.run without waiting); it returns after starting the pump, and the state reports whether it is running. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/florian-lapp__nesp-lib-py
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/florian-lapp__nesp-lib-py --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "nesp-lib-py": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/florian-lapp__nesp-lib-py",
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

- **Reads:** `model_number`, `firmware_version`, `status`, `running`, `volume_infused_ml`, `volume_withdrawn_ml`
- **Sets:** `syringe_diameter_mm`, `pumping_direction`, `pumping_volume_ml`, `pumping_rate_ml_per_min`, `safe_mode_timeout_s`

| Action | What it does |
| --- | --- |
| `run_pump` | Start the pump with the configured direction, volume and rate (Pump.run without waiting); it returns after starting the pump, and the state reports whether it is running |
| `purge` | Run the pump at its maximum rate in the configured direction until it is stopped (Pump.run_purge); it returns after starting the purge |
| `stop_pump` | Stop the pump without waiting for the run to end (Pump.stop without waiting); it takes no input |

## Source and status

- Upstream: [florian-lapp/nesp-lib-py](https://github.com/florian-lapp/nesp-lib-py) at `c16abc82c9fe` (MIT); fetch it with `python3 scripts/add_device.py labs/florian-lapp__nesp-lib-py` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/florian-lapp__nesp-lib-py`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/florian-lapp__nesp-lib-py) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/florian-lapp__nesp-lib-py/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/florian-lapp__nesp-lib-py/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
