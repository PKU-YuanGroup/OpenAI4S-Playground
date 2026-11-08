# Universal Robots arm (ur_interface.ur:UR)

`labs/ad-sdl__ur_module` · Robot arms and grippers · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Universal Robots arm (ur_interface.ur:UR), adapted from ad-sdl/ur_module. It reads `movement_state`, `joint_positions`, `robot_mode`, `safety_status` and 5 more; runs `home`, `pause_program`, `stop_program`, `power_off_arm` and 1 more. `home`: command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/ad-sdl__ur_module
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/ad-sdl__ur_module --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ur_module": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/ad-sdl__ur_module",
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

- **Reads:** `movement_state`, `joint_positions`, `robot_mode`, `safety_status`, `operational_mode`, `program_state`, `loaded_program`, `program_run_status`, `remote_control`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `home` | Command one or more actuated joints to target positions in joint space, optionally over a declared duration, and report whether the target was reached within tolerance. |
| `pause_program` | Pause the loaded URP program with the dashboard 'pause'; completed only when the dashboard answers 'Pausing program' |
| `stop_program` | Stop the loaded URP program with the dashboard 'stop' (the upstream node's safety_stop); completed only when the dashboard answers 'Stopped'; not the e-stop |
| `power_off_arm` | Power the arm off with the dashboard 'power off' (the upstream node's e_stop) and confirm POWER_OFF by fresh 'robotmode' reads; it takes no input |
| `power_on` | Re-enable after a reset (refused while latched, never run by the reset, a permit for each call): with safety status NORMAL, send the dashboard 'brake release' to an arm in POWER_OFF, BOOTING, POWER_ON or IDLE and confirm RUNNING; it never unlocks a protective stop, restarts safety or changes the operational mode |

## Source and status

- Upstream: [ad-sdl/ur_module](https://github.com/ad-sdl/ur_module) at `75f1c5fe53c7` (MIT); fetch it with `python3 scripts/add_device.py labs/ad-sdl__ur_module` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/ad-sdl__ur_module`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/ad-sdl__ur_module) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/ad-sdl__ur_module/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/ad-sdl__ur_module/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
