# MagScope focus motor (magscope.PythonMicroscopeFocusMotor)

`labs/7jameslondon__magscope` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

MagScope focus motor (magscope.PythonMicroscopeFocusMotor), adapted from 7jameslondon/magscope. It reads `current_z`, `is_moving`, `lower_limit` and `upper_limit`; sets `target_z`; runs `focus`. `focus`: move the focus axis to a target Z position or run an autofocus search over a declared range, returning the achieved Z position and focus score. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/7jameslondon__magscope
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/7jameslondon__magscope --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "magscope": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/7jameslondon__magscope",
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

- **Reads:** `current_z`, `is_moving`, `lower_limit`, `upper_limit`
- **Sets:** `target_z`

| Action | What it does |
| --- | --- |
| `focus` | Move the focus axis to a target Z position or run an autofocus search over a declared range, returning the achieved Z position and focus score. |

## Source and status

- Upstream: [7jameslondon/magscope](https://github.com/7jameslondon/magscope) at `d8f5f6036eb4` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/7jameslondon__magscope` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/7jameslondon__magscope`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/7jameslondon__magscope) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/7jameslondon__magscope/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/7jameslondon__magscope/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
