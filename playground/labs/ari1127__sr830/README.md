# SRS SR830 lock-in amplifier

`labs/ari1127__sr830` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

SRS SR830 lock-in amplifier, adapted from ari1127/sr830. It reads `x`, `y`, `r`, `theta` and 14 more; sets `frequency`, `amplitude`, `phase`, `reference_source` and 4 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ari1127__sr830
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ari1127__sr830 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sr830": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ari1127__sr830",
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

- **Reads:** `x`, `y`, `r`, `theta`, `snapshot`, `harmonic`, `trigger_shape`, `aux_output_1`, `aux_output_2`, `grounding`, `line_filter`, `reserve`, `filter_slope`, `sync_filter`, `display_1`, `display_2`, `expand_1`, `expand_2`
- **Sets:** `frequency`, `amplitude`, `phase`, `reference_source`, `input_source`, `coupling`, `time_constant_index`, `sensitivity_index`

## Source and status

- Upstream: [ari1127/sr830](https://github.com/ari1127/sr830) at `930c9c5dcd80` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/ari1127__sr830` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ari1127__sr830`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ari1127__sr830) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ari1127__sr830/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ari1127__sr830/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
