# StageController (Phytron stepper over serial)

`labs/simonmeersschaut__stagecontroller` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

StageController (Phytron stepper over serial), adapted from simonmeersschaut/stagecontroller. It runs `start_rotation` and `stop_rotation`. `start_rotation`: start the stepper rotation by sending the upstream XL+ command. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/simonmeersschaut__stagecontroller
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/simonmeersschaut__stagecontroller --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "stagecontroller": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/simonmeersschaut__stagecontroller",
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
- **Sets:** —

| Action | What it does |
| --- | --- |
| `start_rotation` | Start the stepper rotation by sending the upstream XL+ command |
| `stop_rotation` | Stop the stepper by sending the upstream XS stop command |

## Source and status

- Upstream: [simonmeersschaut/stagecontroller](https://github.com/simonmeersschaut/stagecontroller) at `7edb1ac137a0` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/simonmeersschaut__stagecontroller` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/simonmeersschaut__stagecontroller`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/simonmeersschaut__stagecontroller) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/simonmeersschaut__stagecontroller/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/simonmeersschaut__stagecontroller/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
