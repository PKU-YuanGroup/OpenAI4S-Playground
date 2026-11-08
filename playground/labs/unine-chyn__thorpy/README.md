# Thorlabs APT stage (Thorpy)

`labs/unine-chyn__thorpy` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Thorlabs APT stage (Thorpy), adapted from unine-chyn/thorpy. It reads `homed`; sets `position`, `max_velocity` and `acceleration`; runs `home` and `stop_motion`. `home`: start a home move and wait until the controller reports homed. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/unine-chyn__thorpy
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/unine-chyn__thorpy --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "thorpy": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/unine-chyn__thorpy",
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

- **Reads:** `homed`
- **Sets:** `position`, `max_velocity`, `acceleration`

| Action | What it does |
| --- | --- |
| `home` | Start a home move and wait until the controller reports homed |
| `stop_motion` | Stop every kind of motor move on the channel immediately |

## Source and status

- Upstream: [unine-chyn/thorpy](https://github.com/unine-chyn/thorpy) at `e8f000bd8a5b` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/unine-chyn__thorpy` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/unine-chyn__thorpy`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/unine-chyn__thorpy) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/unine-chyn__thorpy/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/unine-chyn__thorpy/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
