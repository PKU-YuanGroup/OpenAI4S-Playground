# New Era NE-500 syringe pump

`labs/clarklabucb__newerapumps_python3` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

New Era NE-500 syringe pump, adapted from clarklabucb/newerapumps_python3. It sets `flow_rate` and `diameter`; runs `start_pump` and `stop_pump`. `start_pump`: start the pump at the flow rate stored on the device (<n>RUN). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/clarklabucb__newerapumps_python3
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/clarklabucb__newerapumps_python3 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "newerapumps_python3": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/clarklabucb__newerapumps_python3",
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

- **Reads:** —
- **Sets:** `flow_rate`, `diameter`

| Action | What it does |
| --- | --- |
| `start_pump` | Start the pump at the flow rate stored on the device (<n>RUN) |
| `stop_pump` | Stop this pump and zero its rate (<n>STP, then <n>RAT0UH); it takes no input |

## Source and status

- Upstream: [clarklabucb/newerapumps_python3](https://github.com/clarklabucb/newerapumps_python3) at `b8e3d0214ded` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/clarklabucb__newerapumps_python3` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/clarklabucb__newerapumps_python3`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/clarklabucb__newerapumps_python3) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/clarklabucb__newerapumps_python3/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/clarklabucb__newerapumps_python3/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
