# Franka TMR spine and battery ROS 2 interfaces

`robots/frankarobotics__franka_ros2` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence Apache-2.0

Franka TMR spine and battery ROS 2 interfaces, adapted from frankarobotics/franka_ros2. It reads `position`, `position_valid`, `state`, `state_valid` and 3 more; runs `move_absolute`, `halt_motion`, `switch_off_spine`, `switch_on_spine` and 2 more. `move_absolute`: move the spine to an absolute position through the ROS 2 MoveAbsolute action; the action returns the spine's reached flag and stop reason, and cancellation requests the upstream quick-stop and re-arm path. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/frankarobotics__franka_ros2
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/frankarobotics__franka_ros2 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "franka_ros2": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/frankarobotics__franka_ros2",
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

- **Reads:** `position`, `position_valid`, `state`, `state_valid`, `state_error_code`, `state_error_description`, `read_battery_state`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `move_absolute` | Move the spine to an absolute position through the ROS 2 MoveAbsolute action; the action returns the spine's reached flag and stop reason, and cancellation requests the upstream quick-stop and re-arm path |
| `halt_motion` | Halt an ongoing spine motion through the acknowledged Halt service; the upstream quick-stop then waits for SwitchedOff and re-arms the drive to SwitchedOn, so this is not the safe state |
| `switch_off_spine` | Switch the spine drive off through the acknowledged SwitchOff service; the callback returns after the REST transition to SwitchedOff, which disables motion |
| `switch_on_spine` | Switch the spine drive on through the acknowledged SwitchOn service (SwitchedOn, enabling motion); the declared re-enable after a safety reset: the reset never calls it and it is refused while the e-stop is latched |
| `stop_wireless_charging` | Stop wireless charging through the acknowledged std_srvs/Trigger service; the output is the service's application result, not a measured charging state |
| `try_start_wireless_charging` | Attempt to start wireless charging through the acknowledged std_srvs/Trigger service; the output is the service's application result, not a measured charging state |

## Source and status

- Upstream: [frankarobotics/franka_ros2](https://github.com/frankarobotics/franka_ros2) at `4acc05c01ebf` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/frankarobotics__franka_ros2` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/frankarobotics__franka_ros2`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/frankarobotics__franka_ros2) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/frankarobotics__franka_ros2/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/frankarobotics__franka_ros2/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
