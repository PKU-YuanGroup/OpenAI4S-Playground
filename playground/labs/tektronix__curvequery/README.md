# Tektronix 4/5/6 Series MSO waveform download (curvequery)

`labs/tektronix__curvequery` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence Apache-2.0

Tektronix 4/5/6 Series MSO waveform download (curvequery), adapted from tektronix/curvequery. It runs `download_curves`. `download_curves`: download every displayed waveform source through the curvequery feature and return the traces. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/tektronix__curvequery
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/tektronix__curvequery --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "curvequery": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/tektronix__curvequery",
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
| `download_curves` | Download every displayed waveform source through the curvequery feature and return the traces |

## Source and status

- Upstream: [tektronix/curvequery](https://github.com/tektronix/curvequery) at `57e59cc076eb` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/tektronix__curvequery` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/tektronix__curvequery`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/tektronix__curvequery) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/tektronix__curvequery/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/tektronix__curvequery/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
