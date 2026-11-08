# Keysight InfiniiVision oscilloscope

`labs/asvela__keyoscacquire` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Keysight InfiniiVision oscilloscope, adapted from asvela/keyoscacquire. It reads `operation_condition`; sets `acq_type`, `num_averages`, `p_mode`, `num_points` and 1 more; runs `read_error`. `read_error`: read and remove the oldest entry of the instrument error queue (:SYSTem:ERRor?). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/asvela__keyoscacquire
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/asvela__keyoscacquire --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "keyoscacquire": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/asvela__keyoscacquire",
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

- **Reads:** `operation_condition`
- **Sets:** `acq_type`, `num_averages`, `p_mode`, `num_points`, `wav_format`

| Action | What it does |
| --- | --- |
| `read_error` | Read and remove the oldest entry of the instrument error queue (:SYSTem:ERRor?) |

## Source and status

- Upstream: [asvela/keyoscacquire](https://github.com/asvela/keyoscacquire) at `1d093470ab99` (MIT); fetch it with `python3 scripts/add_device.py labs/asvela__keyoscacquire` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/asvela__keyoscacquire`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/asvela__keyoscacquire) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/asvela__keyoscacquire/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/asvela__keyoscacquire/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
