# DAVE underwater simulation ocean current

`robots/field-robotics-lab__dave` · Simulation · underwater robotics · simulation · risk R0 · licence Apache-2.0

DAVE underwater simulation ocean current, adapted from field-robotics-lab/dave. It reads `current_velocity_model`, `horizontal_angle_model` and `read_current`; runs `set_current` and `zero_current`. `set_current`: set the ocean-current velocity and direction means. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/field-robotics-lab__dave
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/field-robotics-lab__dave --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "dave": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/field-robotics-lab__dave",
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

- **Reads:** `current_velocity_model`, `horizontal_angle_model`, `read_current`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_current` | Set the ocean-current velocity and direction means |
| `zero_current` | Set the global constant-current model means to zero with the acknowledged service; stratified, tidal and per-vehicle transient currents are unchanged |

## Source and status

- Upstream: [field-robotics-lab/dave](https://github.com/field-robotics-lab/dave) at `e54ea16bdaf7` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/field-robotics-lab__dave` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/field-robotics-lab__dave`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/field-robotics-lab__dave) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/field-robotics-lab__dave/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/field-robotics-lab__dave/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
