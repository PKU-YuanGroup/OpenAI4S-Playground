# Harvard Apparatus OEM syringe pump

`labs/drkirkm__syringepump` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence CC0-1.0

Harvard Apparatus OEM syringe pump, adapted from drkirkm/syringepump. It reads `pumping`; sets `flow_rate` and `diameter`; runs `run_pump` and `stop_all`. `run_pump`: start the configured pump address at the flow rate it was configured with. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/drkirkm__syringepump
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/drkirkm__syringepump --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "syringepump": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/drkirkm__syringepump",
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

- **Reads:** `pumping`
- **Sets:** `flow_rate`, `diameter`

| Action | What it does |
| --- | --- |
| `run_pump` | Start the configured pump address at the flow rate it was configured with |
| `stop_all` | Stop all three pump addresses with the STP, 01STP and 02STP commands |

## Source and status

- Upstream: [drkirkm/syringepump](https://github.com/drkirkm/syringepump) at `6a39723535c3` (CC0-1.0); fetch it with `python3 scripts/add_device.py labs/drkirkm__syringepump` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/drkirkm__syringepump`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/drkirkm__syringepump) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/drkirkm__syringepump/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/drkirkm__syringepump/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
