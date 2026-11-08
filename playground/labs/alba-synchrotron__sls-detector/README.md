# SLS Mythen II detector (sls.client.Detector)

`labs/alba-synchrotron__sls-detector` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

SLS Mythen II detector (sls.client.Detector), adapted from alba-synchrotron/sls-detector. It reads `detector_type`, `run_status`, `settings`, `nb_modules` and 2 more; sets `energy_threshold`, `exposure_time`, `nb_frames`, `nb_cycles` and 2 more; runs `acquire`, `start_acquisition` and `stop_acquisition`. `acquire`: run one configured acquisition through Detector.acquire() and return the last frame. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/alba-synchrotron__sls-detector
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/alba-synchrotron__sls-detector --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sls-detector": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/alba-synchrotron__sls-detector",
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

- **Reads:** `detector_type`, `run_status`, `settings`, `nb_modules`, `module_serial_number`, `exposure_time_left`
- **Sets:** `energy_threshold`, `exposure_time`, `nb_frames`, `nb_cycles`, `frame_period`, `delay_after_trigger`

| Action | What it does |
| --- | --- |
| `acquire` | Run one configured acquisition through Detector.acquire() and return the last frame |
| `start_acquisition` | Start acquisition with the configured timers (the native start_acquisition command) |
| `stop_acquisition` | Stop acquisition with the native stop_acquisition command (the safe state); it takes no input |

## Source and status

- Upstream: [alba-synchrotron/sls-detector](https://github.com/alba-synchrotron/sls-detector) at `961d33152af2` (MIT); fetch it with `python3 scripts/add_device.py labs/alba-synchrotron__sls-detector` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/alba-synchrotron__sls-detector`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/alba-synchrotron__sls-detector) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/alba-synchrotron__sls-detector/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/alba-synchrotron__sls-detector/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
