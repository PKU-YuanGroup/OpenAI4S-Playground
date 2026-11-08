# SQUAD Lab AD75019 crosspoint switch (qcdrivers Muxi)

`labs/squad-lab__qcdrivers` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence AGPL-3.0

SQUAD Lab AD75019 crosspoint switch (qcdrivers Muxi), adapted from squad-lab/qcdrivers. It reads `identity`; runs `connect`, `status` and `reset_matrix`. `connect`: close one crosspoint with SWITCH32 x,y and read it back with STAT? x,y. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/squad-lab__qcdrivers
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/squad-lab__qcdrivers --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "qcdrivers": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/squad-lab__qcdrivers",
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

- **Reads:** `identity`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `connect` | Close one crosspoint with SWITCH32 x,y and read it back with STAT? x,y |
| `status` | Read one crosspoint of the firmware's 32x32 route buffer with STAT? x,y |
| `reset_matrix` | Open every crosspoint with *RST and read this command's two reply lines |

## Source and status

- Upstream: [squad-lab/qcdrivers](https://github.com/squad-lab/qcdrivers) at `6704e1c1794e` (AGPL-3.0); fetch it with `python3 scripts/add_device.py labs/squad-lab__qcdrivers` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/squad-lab__qcdrivers`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/squad-lab__qcdrivers) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/squad-lab__qcdrivers/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/squad-lab__qcdrivers/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
