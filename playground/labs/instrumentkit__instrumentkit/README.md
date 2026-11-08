# Tektronix DPO70000 oscilloscope (instrumentkit)

`labs/instrumentkit__instrumentkit` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence AGPL-3.0

Tektronix DPO70000 oscilloscope (instrumentkit), adapted from instrumentkit/instrumentkit. It reads `acquire_enhanced_enob`, `acquire_enhanced_state`, `acquire_interp_8bit`, `acquire_magnivu` and 8 more; runs `run_acquisition`, `stop_acquisition`, `force_trigger`, `software_trigger` and 1 more. `run_acquisition`: enable the trigger and start acquisition (the native run, :RUN). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/instrumentkit__instrumentkit
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/instrumentkit__instrumentkit --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "instrumentkit": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/instrumentkit__instrumentkit",
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

- **Reads:** `acquire_enhanced_enob`, `acquire_enhanced_state`, `acquire_interp_8bit`, `acquire_magnivu`, `acquire_mode`, `acquire_mode_actual`, `acquire_num_acquisitions`, `acquire_num_avgs`, `acquire_num_envelop`, `acquire_num_frames`, `acquire_state`, `trigger_state`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `run_acquisition` | Enable the trigger and start acquisition (the native run, :RUN) |
| `stop_acquisition` | Disable the trigger and stop acquisition (the native stop, :STOP); it takes no input |
| `force_trigger` | Force a trigger event (the native force_trigger, TRIG FORC) |
| `software_trigger` | Send a SCPI software trigger event (the inherited native trigger, *TRG) |
| `reset_instrument` | Reset the instrument (the inherited native reset, *RST); it may revert all settings |

## Source and status

- Upstream: [instrumentkit/instrumentkit](https://github.com/instrumentkit/instrumentkit) at `a13c15020b6d` (AGPL-3.0); fetch it with `python3 scripts/add_device.py labs/instrumentkit__instrumentkit` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/instrumentkit__instrumentkit`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/instrumentkit__instrumentkit) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/instrumentkit__instrumentkit/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/instrumentkit__instrumentkit/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
