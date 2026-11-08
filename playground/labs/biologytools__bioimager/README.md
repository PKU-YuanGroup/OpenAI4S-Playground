# Cobolt laser (PythonMicroscope)

`labs/biologytools__bioimager` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence GPL-3.0

Cobolt laser (PythonMicroscope), adapted from biologytools/bioimager. It reads `power` and `status`; sets `emission` and `power_setpoint`; runs `disable_laser`. `disable_laser`: disable laser emission through the native disable(); it takes no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/biologytools__bioimager
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/biologytools__bioimager --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "bioimager": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/biologytools__bioimager",
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

- **Reads:** `power`, `status`
- **Sets:** `emission`, `power_setpoint`

| Action | What it does |
| --- | --- |
| `disable_laser` | Disable laser emission through the native disable(); it takes no input |

## Source and status

- Upstream: [biologytools/bioimager](https://github.com/biologytools/bioimager) at `149b45255d62` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/biologytools__bioimager` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/biologytools__bioimager`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/biologytools__bioimager) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/biologytools__bioimager/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/biologytools__bioimager/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
