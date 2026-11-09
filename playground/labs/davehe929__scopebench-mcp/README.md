# RIGOL DHO800/DHO900 oscilloscope

`labs/davehe929__scopebench-mcp` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence Apache-2.0

RIGOL DHO800/DHO900 oscilloscope, adapted from davehe929/scopebench-mcp. It reads `trigger_status`, `frequency`, `period`, `vpp` and 2 more; sets `channel_coupling`, `channel_scale`, `channel_offset`, `trigger_level` and 2 more; runs `measure`. `measure`: read one instrument-side scalar measurement of one analog channel. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/davehe929__scopebench-mcp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/davehe929__scopebench-mcp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "scopebench-mcp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/davehe929__scopebench-mcp",
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

- **Reads:** `trigger_status`, `frequency`, `period`, `vpp`, `vrms`, `mean`
- **Sets:** `channel_coupling`, `channel_scale`, `channel_offset`, `trigger_level`, `timebase_scale`, `timebase_offset`

| Action | What it does |
| --- | --- |
| `measure` | Read one instrument-side scalar measurement of one analog channel |

## Source and status

- Upstream: [davehe929/scopebench-mcp](https://github.com/davehe929/scopebench-mcp) at `3f0abc87a283` (Apache-2.0); fetch it with `python3 scripts/add_device.py labs/davehe929__scopebench-mcp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/davehe929__scopebench-mcp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/davehe929__scopebench-mcp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/davehe929__scopebench-mcp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/davehe929__scopebench-mcp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
