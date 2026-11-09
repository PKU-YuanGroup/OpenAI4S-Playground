# Olin ModCon USB source-measure unit

`labs/itdaniher__olin-smus` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Olin ModCon USB source-measure unit, adapted from itdaniher/olin-smus. It reads `measured_voltage`, `measured_current`, `mod_voltage` and `source_mode`; sets `source_voltage` and `source_current`; runs `source_off`. `source_off`: set the source current target to zero with the upstream set(amps=0) safety call; it takes no input and is the declared safe state. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/itdaniher__olin-smus
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/itdaniher__olin-smus --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "olin-smus": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/itdaniher__olin-smus",
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

- **Reads:** `measured_voltage`, `measured_current`, `mod_voltage`, `source_mode`
- **Sets:** `source_voltage`, `source_current`

| Action | What it does |
| --- | --- |
| `source_off` | Set the source current target to zero with the upstream set(amps=0) safety call; it takes no input and is the declared safe state |

## Source and status

- Upstream: [itdaniher/olin-smus](https://github.com/itdaniher/olin-smus) at `3bddec37c09a` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/itdaniher__olin-smus` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/itdaniher__olin-smus`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/itdaniher__olin-smus) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/itdaniher__olin-smus/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/itdaniher__olin-smus/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
