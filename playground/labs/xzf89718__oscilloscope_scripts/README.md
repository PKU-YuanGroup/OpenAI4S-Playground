# Tektronix TBS2000B oscilloscope

`labs/xzf89718__oscilloscope_scripts` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Tektronix TBS2000B oscilloscope, adapted from xzf89718/oscilloscope_scripts. It reads `frequency`, `amplitude` and `high`; sets `channel`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/xzf89718__oscilloscope_scripts
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/xzf89718__oscilloscope_scripts --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "oscilloscope_scripts": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/xzf89718__oscilloscope_scripts",
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

- **Reads:** `frequency`, `amplitude`, `high`
- **Sets:** `channel`

## Source and status

- Upstream: [xzf89718/oscilloscope_scripts](https://github.com/xzf89718/oscilloscope_scripts) at `105e6021650f` (MIT); fetch it with `python3 scripts/add_device.py labs/xzf89718__oscilloscope_scripts` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/xzf89718__oscilloscope_scripts`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/xzf89718__oscilloscope_scripts) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/xzf89718__oscilloscope_scripts/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/xzf89718__oscilloscope_scripts/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
