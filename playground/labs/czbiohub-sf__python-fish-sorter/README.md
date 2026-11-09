# Fish Sorter pneumatic valve controller (Wago, Modbus TCP)

`labs/czbiohub-sf__python-fish-sorter` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

Fish Sorter pneumatic valve controller (Wago, Modbus TCP), adapted from czbiohub-sf/python-fish-sorter. It reads `function_code` and `function_echo`; sets `draw_time_ms` and `expel_time_ms`; runs `set_pressure`, `set_vacuum`, `idle_atmospheric` and `safe_pneumatics`. `set_pressure`: pressure on or off: writes the upstream press_on or press_off code and waits until the controller has taken it. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/czbiohub-sf__python-fish-sorter
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/czbiohub-sf__python-fish-sorter --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "python-fish-sorter": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/czbiohub-sf__python-fish-sorter",
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

- **Reads:** `function_code`, `function_echo`
- **Sets:** `draw_time_ms`, `expel_time_ms`

| Action | What it does |
| --- | --- |
| `set_pressure` | Pressure on or off: writes the upstream press_on or press_off code and waits until the controller has taken it |
| `set_vacuum` | Vacuum on or off: writes the upstream vac_on or vac_off code (the controller program sets or clears its Vacuum output) and waits until the controller has taken it |
| `idle_atmospheric` | Atmospheric idle: writes the upstream func_idle code and waits until the controller has taken it |
| `safe_pneumatics` | Safe-state stop path: writes the func_idle code and waits until the controller has taken it; takes no input |

## Source and status

- Upstream: [czbiohub-sf/python-fish-sorter](https://github.com/czbiohub-sf/python-fish-sorter) at `a8f2409fa692` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/czbiohub-sf__python-fish-sorter` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/czbiohub-sf__python-fish-sorter`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/czbiohub-sf__python-fish-sorter) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/czbiohub-sf__python-fish-sorter/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/czbiohub-sf__python-fish-sorter/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
