# Thorlabs APT piezo channel (interface.module.Module)

`labs/solgaardlab__apt_piezo` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Thorlabs APT piezo channel (interface.module.Module), adapted from solgaardlab/apt_piezo. It reads `max_travel`; sets `position` and `closed_loop`; runs `move_piezo` and `zero_piezo`. `move_piezo`: command the piezo module to a travel in micrometres (native move()). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/solgaardlab__apt_piezo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/solgaardlab__apt_piezo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "apt_piezo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/solgaardlab__apt_piezo",
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

- **Reads:** `max_travel`
- **Sets:** `position`, `closed_loop`

| Action | What it does |
| --- | --- |
| `move_piezo` | Command the piezo module to a travel in micrometres (native move()) |
| `zero_piezo` | Command the piezo to its zero position (native zero()); it takes no input and is the safe state |

## Source and status

- Upstream: [solgaardlab/apt_piezo](https://github.com/solgaardlab/apt_piezo) at `677eb8f632b6` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/solgaardlab__apt_piezo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/solgaardlab__apt_piezo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/solgaardlab__apt_piezo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/solgaardlab__apt_piezo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/solgaardlab__apt_piezo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
