# Boston Dynamics Spot (bosdyn.client.robot.Robot)

`robots/boston-dynamics__spot-sdk` · Mobile robots · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence LicenseRef-proprietary

Boston Dynamics Spot (bosdyn.client.robot.Robot), adapted from boston-dynamics/spot-sdk. It reads `serial_number`, `nickname`, `species`, `estopped` and 5 more; sets `motors_on`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/boston-dynamics__spot-sdk
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/boston-dynamics__spot-sdk --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "spot-sdk": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/boston-dynamics__spot-sdk",
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

- **Reads:** `serial_number`, `nickname`, `species`, `estopped`, `has_arm`, `usernames`, `frame_names`, `can_power_off_robot`, `redundant_safety_stop_enabled`
- **Sets:** `motors_on`

## Source and status

- Upstream: [boston-dynamics/spot-sdk](https://github.com/boston-dynamics/spot-sdk) at `04537ddafe06` (LicenseRef-proprietary); fetch it with `python3 scripts/add_device.py robots/boston-dynamics__spot-sdk` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/boston-dynamics__spot-sdk`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/boston-dynamics__spot-sdk) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/boston-dynamics__spot-sdk/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/boston-dynamics__spot-sdk/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
