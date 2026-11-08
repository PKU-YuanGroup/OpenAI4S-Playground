# nebPod NPX rig controller (nebPod.Controller)

`labs/nbush257__pyexpcontrol` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence NOASSERTION

nebPod NPX rig controller (nebPod.Controller), adapted from nbush257/pyexpcontrol. It reads `valves`, `gpio` and `camera_triggering`; sets `laser_amplitude`; runs `set_valve`, `set_all_valves`, `set_gpio`, `start_camera_trigger` and 2 more. `set_valve`: open or close one olfactometer valve. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/nbush257__pyexpcontrol
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/nbush257__pyexpcontrol --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pyexpcontrol": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/nbush257__pyexpcontrol",
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

- **Reads:** `valves`, `gpio`, `camera_triggering`
- **Sets:** `laser_amplitude`

| Action | What it does |
| --- | --- |
| `set_valve` | Open or close one olfactometer valve |
| `set_all_valves` | Set all eight olfactometer valves from an eight-character binary pattern (leftmost character is Valve 1, '1' is open) |
| `set_gpio` | Drive one GPIO pin high or low |
| `start_camera_trigger` | Start the camera trigger with the upstream default frame rate |
| `stop_camera_trigger` | Stop the camera trigger |
| `all_off` | Safe state: laser off at 0 V, all olfactometer valves closed, camera trigger stopped |

## Source and status

- Upstream: [nbush257/pyexpcontrol](https://github.com/nbush257/pyexpcontrol) at `06e94c4d22ac` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/nbush257__pyexpcontrol` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/nbush257__pyexpcontrol`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/nbush257__pyexpcontrol) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/nbush257__pyexpcontrol/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/nbush257__pyexpcontrol/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
