# TwinCAT NC axis telemetry (ophyd-ads, read only)

`labs/pcdshub__ophyd-ads` · Sensors and cameras · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence BSD-3-Clause

TwinCAT NC axis telemetry (ophyd-ads, read only), adapted from pcdshub/ophyd-ads. It reads `act_acc`, `act_pos`, `act_pos_modulo`, `act_torque` and 8 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pcdshub__ophyd-ads
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pcdshub__ophyd-ads --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ophyd-ads": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pcdshub__ophyd-ads",
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

- **Reads:** `act_acc`, `act_pos`, `act_pos_modulo`, `act_torque`, `act_velo`, `axis_state`, `cmd_no`, `control_d_word`, `couple_state`, `ctrl_output`, `drive_output`, `read_channels`
- **Sets:** —

## Source and status

- Upstream: [pcdshub/ophyd-ads](https://github.com/pcdshub/ophyd-ads) at `2029e0bebee6` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/pcdshub__ophyd-ads` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pcdshub__ophyd-ads`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pcdshub__ophyd-ads) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pcdshub__ophyd-ads/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pcdshub__ophyd-ads/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
