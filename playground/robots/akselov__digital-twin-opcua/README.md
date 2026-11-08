# KUKA KR 16-2 via KUKAVARPROXY (KUKAVARPROXY_communication.KUKA)

`robots/akselov__digital-twin-opcua` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

KUKA KR 16-2 via KUKAVARPROXY (KUKAVARPROXY_communication.KUKA), adapted from akselov/digital-twin-opcua. It reads `joint_positions`, `motor_velocities`, `motor_torques` and `motor_currents`; runs `move_joints`. `move_joints`: write the six axis values to TARGET_AXIS as an E6AXIS string; the KRL program moves to it. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/akselov__digital-twin-opcua
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/akselov__digital-twin-opcua --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "digital-twin-opcua": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/akselov__digital-twin-opcua",
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

- **Reads:** `joint_positions`, `motor_velocities`, `motor_torques`, `motor_currents`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_joints` | Write the six axis values to TARGET_AXIS as an E6AXIS string; the KRL program moves to it |

## Source and status

- Upstream: [akselov/digital-twin-opcua](https://github.com/akselov/digital-twin-opcua) at `adc30f464665` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/akselov__digital-twin-opcua` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/akselov__digital-twin-opcua`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/akselov__digital-twin-opcua) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/akselov__digital-twin-opcua/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/akselov__digital-twin-opcua/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
