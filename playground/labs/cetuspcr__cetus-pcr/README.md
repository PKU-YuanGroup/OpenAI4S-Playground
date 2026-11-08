# Cetus PCR low-cost thermocycler (functions.ArduinoPCR)

`labs/cetuspcr__cetus-pcr` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Cetus PCR low-cost thermocycler (functions.ArduinoPCR), adapted from cetuspcr/cetus-pcr. It reads `sample_temperature`, `lid_temperature`, `is_running`, `current_step` and 1 more; runs `run_protocol` and `stop_peltier`. `run_protocol`: run one temperature hold step for a number of cycles through the upstream PID experiment loop; the Peltier is driven by that loop, not by a temperature setpoint of the firmware. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/cetuspcr__cetus-pcr
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/cetuspcr__cetus-pcr --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "cetus-pcr": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/cetuspcr__cetus-pcr",
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

- **Reads:** `sample_temperature`, `lid_temperature`, `is_running`, `current_step`, `current_cycle`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `run_protocol` | Run one temperature hold step for a number of cycles through the upstream PID experiment loop; the Peltier is driven by that loop, not by a temperature setpoint of the firmware |
| `stop_peltier` | Clear the experiment flag and write <peltier 0 0>, setting both Peltier PWMs to zero; it takes no input |

## Source and status

- Upstream: [cetuspcr/cetus-pcr](https://github.com/cetuspcr/cetus-pcr) at `bbed1fd40257` (MIT); fetch it with `python3 scripts/add_device.py labs/cetuspcr__cetus-pcr` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/cetuspcr__cetus-pcr`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/cetuspcr__cetus-pcr) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/cetuspcr__cetus-pcr/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/cetuspcr__cetus-pcr/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
