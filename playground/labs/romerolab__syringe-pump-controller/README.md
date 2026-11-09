# New Era NE-500/501 syringe pump

`labs/romerolab__syringe-pump-controller` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence LGPL-3.0

New Era NE-500/501 syringe pump, adapted from romerolab/syringe-pump-controller. It reads `direction`; sets `flow_rate` and `diameter`; runs `dispense`, `prime` and `stop_all`. `dispense`: run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/romerolab__syringe-pump-controller
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/romerolab__syringe-pump-controller --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "syringe-pump-controller": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/romerolab__syringe-pump-controller",
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

- **Reads:** `direction`
- **Sets:** `flow_rate`, `diameter`

| Action | What it does |
| --- | --- |
| `dispense` | Run a pump at a declared flow rate for a declared duration or volume in a declared direction, reporting the volume moved. |
| `prime` | Prime the pump: INF direction, 10.0 MH, run (the upstream prime sequence) |
| `stop_all` | Stop all pumps with the broadcast *STP command; takes no input |

## Source and status

- Upstream: [romerolab/syringe-pump-controller](https://github.com/romerolab/syringe-pump-controller) at `7c2af002a04a` (LGPL-3.0); fetch it with `python3 scripts/add_device.py labs/romerolab__syringe-pump-controller` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/romerolab__syringe-pump-controller`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/romerolab__syringe-pump-controller) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/romerolab__syringe-pump-controller/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/romerolab__syringe-pump-controller/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
