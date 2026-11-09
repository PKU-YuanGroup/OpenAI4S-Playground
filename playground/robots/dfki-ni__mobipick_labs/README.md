# Mobipick tables-demo experiment camera

`robots/dfki-ni__mobipick_labs` · Sensors and cameras · simulation · risk R1 · licence BSD-3-Clause

Mobipick tables-demo experiment camera, adapted from dfki-ni/mobipick_labs. It runs `capture`. `capture`: capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/dfki-ni__mobipick_labs
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/dfki-ni__mobipick_labs --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "mobipick_labs": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/dfki-ni__mobipick_labs",
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
| `capture` | Capture a single image from a named camera with a declared resolution and exposure and return an image artifact reference. |

## Source and status

- Upstream: [dfki-ni/mobipick_labs](https://github.com/dfki-ni/mobipick_labs) at `adbfa53af2f6` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py robots/dfki-ni__mobipick_labs` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/dfki-ni__mobipick_labs`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/dfki-ni__mobipick_labs) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/dfki-ni__mobipick_labs/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/dfki-ni__mobipick_labs/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
