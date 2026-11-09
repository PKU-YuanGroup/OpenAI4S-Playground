# BMG microplate reader incubator and status (sidecar.bmg_interface.BmgCom)

`labs/ad-sdl__bmg_module` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

BMG microplate reader incubator and status (sidecar.bmg_interface.BmgCom), adapted from ad-sdl/bmg_module. It reads `version`, `status`, `error`, `temperature_1` and 2 more; sets `setpoint`; runs `heater_off`. `heater_off`: switch the incubator off (native set_temp(0.0), Temp 0.0); takes no input and runs during an e-stop. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ad-sdl__bmg_module
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ad-sdl__bmg_module --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "bmg_module": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ad-sdl__bmg_module",
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

- **Reads:** `version`, `status`, `error`, `temperature_1`, `temperature_2`, `temperature_3`
- **Sets:** `setpoint`

| Action | What it does |
| --- | --- |
| `heater_off` | Switch the incubator off (native set_temp(0.0), Temp 0.0); takes no input and runs during an e-stop |

## Source and status

- Upstream: [ad-sdl/bmg_module](https://github.com/ad-sdl/bmg_module) at `22d55c6036e9` (MIT); fetch it with `python3 scripts/add_device.py labs/ad-sdl__bmg_module` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ad-sdl__bmg_module`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ad-sdl__bmg_module) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ad-sdl__bmg_module/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ad-sdl__bmg_module/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
