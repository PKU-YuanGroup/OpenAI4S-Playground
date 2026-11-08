# Ando AQ-6315A optical spectrum analyzer

`labs/christofferkrook__laserphysics_devices` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence GPL-3.0

Ando AQ-6315A optical spectrum analyzer, adapted from christofferkrook/laserphysics_devices. It sets `start_wl`, `stop_wl`, `center_wl`, `span` and 7 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/christofferkrook__laserphysics_devices
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/christofferkrook__laserphysics_devices --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "laserphysics_devices": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/christofferkrook__laserphysics_devices",
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

- **Reads:** —
- **Sets:** `start_wl`, `stop_wl`, `center_wl`, `span`, `averages`, `resolution`, `scale`, `current_trace`, `display_on`, `write_enabled`, `sweep_status`

## Source and status

- Upstream: [christofferkrook/laserphysics_devices](https://github.com/christofferkrook/laserphysics_devices) at `7af657f90b19` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/christofferkrook__laserphysics_devices` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/christofferkrook__laserphysics_devices`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/christofferkrook__laserphysics_devices) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/christofferkrook__laserphysics_devices/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/christofferkrook__laserphysics_devices/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
