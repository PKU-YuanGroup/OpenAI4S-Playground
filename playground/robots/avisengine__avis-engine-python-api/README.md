# AVIS Engine car (avisengine.Car)

`robots/avisengine__avis-engine-python-api` · Mobile robots · simulation · risk R1 · licence NOASSERTION

AVIS Engine car (avisengine.Car), adapted from avisengine/avis-engine-python-api. It reads `speed` and `sensors`; sets `throttle`, `steering` and `sensor_angle`; runs `stop_motion`. `stop_motion`: stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/avisengine__avis-engine-python-api
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/avisengine__avis-engine-python-api --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "avis-engine-python-api": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/avisengine__avis-engine-python-api",
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

- **Reads:** `speed`, `sensors`
- **Sets:** `throttle`, `steering`, `sensor_angle`

| Action | What it does |
| --- | --- |
| `stop_motion` | Stop all motion on the resource with a declared deceleration profile and report the stopping position. This capability is always cancellable=false and is exempt from rate limiting. |

## Source and status

- Upstream: [avisengine/avis-engine-python-api](https://github.com/avisengine/avis-engine-python-api) at `32b9a9e063a5` (NOASSERTION); fetch it with `python3 scripts/add_device.py robots/avisengine__avis-engine-python-api` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/avisengine__avis-engine-python-api`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/avisengine__avis-engine-python-api) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/avisengine__avis-engine-python-api/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/avisengine__avis-engine-python-api/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
