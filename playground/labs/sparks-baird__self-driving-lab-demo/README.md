# CLSLab:Light NeoPixel + AS7341 (nonwireless serial)

`labs/sparks-baird__self-driving-lab-demo` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

CLSLab:Light NeoPixel + AS7341 (nonwireless serial), adapted from sparks-baird/self-driving-lab-demo. It sets `color`; runs `measure_spectrum`. `measure_spectrum`: measure the eight fixed AS7341 bands through the current NeoPixel color, with the ATIME, ASTEP and gain settings the command carries; the reply is one list of eight intensities. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/sparks-baird__self-driving-lab-demo
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/sparks-baird__self-driving-lab-demo --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "self-driving-lab-demo": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/sparks-baird__self-driving-lab-demo",
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
- **Sets:** `color`

| Action | What it does |
| --- | --- |
| `measure_spectrum` | Measure the eight fixed AS7341 bands through the current NeoPixel color, with the ATIME, ASTEP and gain settings the command carries; the reply is one list of eight intensities |

## Source and status

- Upstream: [sparks-baird/self-driving-lab-demo](https://github.com/sparks-baird/self-driving-lab-demo) at `051e91e34b63` (MIT); fetch it with `python3 scripts/add_device.py labs/sparks-baird__self-driving-lab-demo` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/sparks-baird__self-driving-lab-demo`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/sparks-baird__self-driving-lab-demo) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/sparks-baird__self-driving-lab-demo/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/sparks-baird__self-driving-lab-demo/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
