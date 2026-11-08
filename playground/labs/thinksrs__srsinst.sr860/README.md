# SRS SR860 lock-in amplifier

`labs/thinksrs__srsinst.sr860` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

SRS SR860 lock-in amplifier, adapted from thinksrs/srsinst.sr860. It reads `x`, `y`, `r` and `theta`; sets `frequency`, `amplitude` and `time_constant`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/thinksrs__srsinst.sr860
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/thinksrs__srsinst.sr860 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "srsinst.sr860": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/thinksrs__srsinst.sr860",
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

- **Reads:** `x`, `y`, `r`, `theta`
- **Sets:** `frequency`, `amplitude`, `time_constant`

## Source and status

- Upstream: [thinksrs/srsinst.sr860](https://github.com/thinksrs/srsinst.sr860) at `c234ec204329` (MIT); fetch it with `python3 scripts/add_device.py labs/thinksrs__srsinst.sr860` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/thinksrs__srsinst.sr860`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/thinksrs__srsinst.sr860) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/thinksrs__srsinst.sr860/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/thinksrs__srsinst.sr860/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
