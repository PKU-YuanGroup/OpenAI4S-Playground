# Tektronix DPO70000 oscilloscope

`labs/gregmoille__instrumentcontrol` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Tektronix DPO70000 oscilloscope, adapted from gregmoille/instrumentcontrol. It reads `acquisition_mode_actual`, `acquisition_num_acquisitions`, `acquisition_num_averages`, `acquisition_num_envelopes` and 2 more; sets `acquisition_mode`, `acquisition_num_samples`, `acquisition_sampling_mode`, `acquisition_state` and 5 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/gregmoille__instrumentcontrol
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/gregmoille__instrumentcontrol --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "instrumentcontrol": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/gregmoille__instrumentcontrol",
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

- **Reads:** `acquisition_mode_actual`, `acquisition_num_acquisitions`, `acquisition_num_averages`, `acquisition_num_envelopes`, `acquisition_num_frames`, `trigger_state`
- **Sets:** `acquisition_mode`, `acquisition_num_samples`, `acquisition_sampling_mode`, `acquisition_state`, `acquisition_stop_after`, `acquisition_enhanced_enob`, `acquisition_enhanced_state`, `acquisition_interp_8bit`, `acquisition_magnivu`

## Source and status

- Upstream: [gregmoille/instrumentcontrol](https://github.com/gregmoille/instrumentcontrol) at `2cf8c78dea00` (MIT); fetch it with `python3 scripts/add_device.py labs/gregmoille__instrumentcontrol` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/gregmoille__instrumentcontrol`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/gregmoille__instrumentcontrol) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/gregmoille__instrumentcontrol/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/gregmoille__instrumentcontrol/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
