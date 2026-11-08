# Scanning SQUID microscope: Attocube coarse positioning (scanning-squid)

`labs/moler-group__scanning-squid` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Scanning SQUID microscope: Attocube coarse positioning (scanning-squid), adapted from moler-group/scanning-squid. It reads `scanner_position` and `attocube_modes`; runs `step` and `ground`. `step`: step one Attocube axis with atto.step: mode stp, stepu or stepd with the count (the upstream writes it twice, atto.py:109-124, 169, so the steps made are not known from the source), stepw, a wait, mode gnd. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/moler-group__scanning-squid
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/moler-group__scanning-squid --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "scanning-squid": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/moler-group__scanning-squid",
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

- **Reads:** `scanner_position`, `attocube_modes`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `step` | Step one Attocube axis with atto.step: mode stp, stepu or stepd with the count (the upstream writes it twice, atto.py:109-124, 169, so the steps made are not known from the source), stepw, a wait, mode gnd |
| `ground` | Stop and ground every Attocube axis (atto.stop) and read each mode back |

## Source and status

- Upstream: [moler-group/scanning-squid](https://github.com/moler-group/scanning-squid) at `32a61e8f8f4f` (MIT); fetch it with `python3 scripts/add_device.py labs/moler-group__scanning-squid` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/moler-group__scanning-squid`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/moler-group__scanning-squid) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/moler-group__scanning-squid/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/moler-group__scanning-squid/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
