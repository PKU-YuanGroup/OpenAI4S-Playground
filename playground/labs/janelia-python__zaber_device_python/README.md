# Zaber stage (zaber_device.ZaberStage)

`labs/janelia-python__zaber_device_python` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

Zaber stage (zaber_device.ZaberStage), adapted from janelia-python/zaber_device_python. It reads `x_position`, `y_position`, `z_position`, `x_actuator_id` and 3 more; sets `x_microstep_size`, `y_microstep_size`, `z_microstep_size`, `x_travel` and 2 more; runs `home`, `stop_motion`, `move_absolute`, `move_relative` and 2 more. `home`: home every device in the chain and report the home status of the configured axes. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/janelia-python__zaber_device_python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/janelia-python__zaber_device_python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "zaber_device_python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/janelia-python__zaber_device_python",
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

- **Reads:** `x_position`, `y_position`, `z_position`, `x_actuator_id`, `y_actuator_id`, `z_actuator_id`, `homed`
- **Sets:** `x_microstep_size`, `y_microstep_size`, `z_microstep_size`, `x_travel`, `y_travel`, `z_travel`

| Action | What it does |
| --- | --- |
| `home` | Home every device in the chain and report the home status of the configured axes |
| `stop_motion` | Stop every device in the chain immediately (the native stop, the safe state) |
| `move_absolute` | Move the x, y and z axes to absolute positions in the stage unit |
| `move_relative` | Move the x, y and z axes by relative distances in the stage unit |
| `move_to_stored_position` | Move the x, y and z axes to the positions stored at an address |
| `store_position` | Store the current x, y and z positions at an address and return the stored positions |

## Source and status

- Upstream: [janelia-python/zaber_device_python](https://github.com/janelia-python/zaber_device_python) at `2fec6746359b` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/janelia-python__zaber_device_python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/janelia-python__zaber_device_python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/janelia-python__zaber_device_python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/janelia-python__zaber_device_python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/janelia-python__zaber_device_python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
