# PAMILA read-only middle-layer variable list

`labs/nsls2__pamila` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence BSD-3-Clause

PAMILA read-only middle-layer variable list, adapted from nsls2/pamila. It reads `mlv_count`, `mlv_names`, `enabled_mlv_names`, `enabled_status` and 3 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/nsls2__pamila
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/nsls2__pamila --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pamila": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/nsls2__pamila",
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

- **Reads:** `mlv_count`, `mlv_names`, `enabled_mlv_names`, `enabled_status`, `values`, `value_units`, `read_channels`
- **Sets:** —

## Source and status

- Upstream: [nsls2/pamila](https://github.com/nsls2/pamila) at `62a439b6be7c` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/nsls2__pamila` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/nsls2__pamila`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/nsls2__pamila) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/nsls2__pamila/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/nsls2__pamila/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
