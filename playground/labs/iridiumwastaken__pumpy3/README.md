# Harvard PHD 2000 syringe pump (pumpy3.Pump2000)

`labs/iridiumwastaken__pumpy3` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Harvard PHD 2000 syringe pump (pumpy3.Pump2000), adapted from iridiumwastaken/pumpy3. It reads `infused_volume` and `running`; sets `diameter`, `rate` and `target_volume`; runs `start_pump` and `stop_pump`. `start_pump`: start infusing or withdrawing with the rate and target volume already configured. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/iridiumwastaken__pumpy3
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/iridiumwastaken__pumpy3 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pumpy3": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/iridiumwastaken__pumpy3",
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

- **Reads:** `infused_volume`, `running`
- **Sets:** `diameter`, `rate`, `target_volume`

| Action | What it does |
| --- | --- |
| `start_pump` | Start infusing or withdrawing with the rate and target volume already configured |
| `stop_pump` | Stop the pump with STP (the native stop, the safe state); it takes no input |

## Source and status

- Upstream: [iridiumwastaken/pumpy3](https://github.com/iridiumwastaken/pumpy3) at `0819cd6f9c40` (MIT); fetch it with `python3 scripts/add_device.py labs/iridiumwastaken__pumpy3` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/iridiumwastaken__pumpy3`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/iridiumwastaken__pumpy3) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/iridiumwastaken__pumpy3/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/iridiumwastaken__pumpy3/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
