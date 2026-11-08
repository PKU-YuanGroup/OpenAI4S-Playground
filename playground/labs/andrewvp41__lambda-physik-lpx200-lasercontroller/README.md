# Lambda Physik LPX 200 laser

`labs/andrewvp41__lambda-physik-lpx200-lasercontroller` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence NOASSERTION

Lambda Physik LPX 200 laser, adapted from andrewvp41/lambda-physik-lpx200-lasercontroller. It reads `operating_mode`, `pressure` and `gas_mix`; sets `trigger_mode`, `mode`, `repetition_rate`, `high_voltage` and 1 more; runs `emission_on` and `emission_off`. `emission_on`: start laser operation with OPMODE=ON (the RUN STOP start command). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/andrewvp41__lambda-physik-lpx200-lasercontroller
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/andrewvp41__lambda-physik-lpx200-lasercontroller --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "lambda-physik-lpx200-lasercontroller": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/andrewvp41__lambda-physik-lpx200-lasercontroller",
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

- **Reads:** `operating_mode`, `pressure`, `gas_mix`
- **Sets:** `trigger_mode`, `mode`, `repetition_rate`, `high_voltage`, `energy`

| Action | What it does |
| --- | --- |
| `emission_on` | Start laser operation with OPMODE=ON (the RUN STOP start command) |
| `emission_off` | Stop laser emission with OPMODE=OFF (the RUN STOP stop command); takes no input |

## Source and status

- Upstream: [andrewvp41/lambda-physik-lpx200-lasercontroller](https://github.com/andrewvp41/lambda-physik-lpx200-lasercontroller) at `abd240f534a9` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/andrewvp41__lambda-physik-lpx200-lasercontroller` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/andrewvp41__lambda-physik-lpx200-lasercontroller`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/andrewvp41__lambda-physik-lpx200-lasercontroller) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/andrewvp41__lambda-physik-lpx200-lasercontroller/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/andrewvp41__lambda-physik-lpx200-lasercontroller/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
