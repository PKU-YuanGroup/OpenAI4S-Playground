# New Era SyringeONE NE-1000 syringe pump (syrpp.SyrPump)

`labs/yuanxun-yx__syrpp` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

New Era SyringeONE NE-1000 syringe pump (syrpp.SyrPump), adapted from yuanxun-yx/syrpp. It reads `status`, `firmware_version`, `volume` and `volume_dispensed`; sets `diameter`, `phase`, `phase_function`, `pumping_rate` and 5 more; runs `start_program` and `stop_program`. `start_program`: start the configured pumping program (RUN) and report the pump prompt afterwards. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/yuanxun-yx__syrpp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/yuanxun-yx__syrpp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "syrpp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/yuanxun-yx__syrpp",
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

- **Reads:** `status`, `firmware_version`, `volume`, `volume_dispensed`
- **Sets:** `diameter`, `phase`, `phase_function`, `pumping_rate`, `direction`, `alarm`, `power_fail`, `key_beep`, `buzzer`

| Action | What it does |
| --- | --- |
| `start_program` | Start the configured pumping program (RUN) and report the pump prompt afterwards |
| `stop_program` | Stop the pumping program (STP); the native stop and the safe-state action |

## Source and status

- Upstream: [yuanxun-yx/syrpp](https://github.com/yuanxun-yx/syrpp) at `ae784882903c` (MIT); fetch it with `python3 scripts/add_device.py labs/yuanxun-yx__syrpp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/yuanxun-yx__syrpp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/yuanxun-yx__syrpp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/yuanxun-yx__syrpp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/yuanxun-yx__syrpp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
