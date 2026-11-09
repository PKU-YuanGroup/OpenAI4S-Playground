# Octoaxes 7-axis microscope stage

`labs/veerwang__octoaxes` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Octoaxes 7-axis microscope stage, adapted from veerwang/octoaxes. It reads `x_position_um`, `y_position_um`, `z_steps`, `moving` and 2 more; runs `move_xy`, `set_illumination` and `deenergise`. `move_xy`: move the X and Y stage axes to absolute positions in micrometres. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/veerwang__octoaxes
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/veerwang__octoaxes --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "octoaxes": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/veerwang__octoaxes",
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

- **Reads:** `x_position_um`, `y_position_um`, `z_steps`, `moving`, `illumination_port`, `illumination_percent`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_xy` | Move the X and Y stage axes to absolute positions in micrometres |
| `set_illumination` | Set the illumination channel and intensity used for subsequent imaging or observation, with an optional bounded on-duration after which the light is turned off. |
| `deenergise` | De-energise every stage axis and switch all illumination ports off |

## Source and status

- Upstream: [veerwang/octoaxes](https://github.com/veerwang/octoaxes) at `77cb47e0fdf8` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/veerwang__octoaxes` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/veerwang__octoaxes`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/veerwang__octoaxes) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/veerwang__octoaxes/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/veerwang__octoaxes/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
