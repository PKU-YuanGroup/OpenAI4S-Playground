# ArduPilot SITL Gazebo plugin (ROS 1 surface)

`robots/aurelienroy__ardupilot_sitl_gazebo_plugin` · Simulation · UAVs · simulation · risk R0 · licence Apache-2.0

ArduPilot SITL Gazebo plugin (ROS 1 surface), adapted from aurelienroy/ardupilot_sitl_gazebo_plugin. It reads `observe_motor_speed`; runs `take_lapse_lock` and `release_lapse_lock`. `take_lapse_lock`: take the plugin's bounded wall-time lapse lock with the upstream method default horizon of 1 s; this pauses the plugin loop that steps the paused Gazebo world and exchanges packets with ArduPilot SITL, not ArduPilot itself, and the plugin clears the lock automatically when the timer expires. A simulator: the market serves it with a stand-in that needs no simulator install.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add robots/aurelienroy__ardupilot_sitl_gazebo_plugin
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/robots/aurelienroy__ardupilot_sitl_gazebo_plugin --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ardupilot_sitl_gazebo_plugin": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "robots/aurelienroy__ardupilot_sitl_gazebo_plugin",
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

- **Reads:** `observe_motor_speed`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `take_lapse_lock` | Take the plugin's bounded wall-time lapse lock with the upstream method default horizon of 1 s; this pauses the plugin loop that steps the paused Gazebo world and exchanges packets with ArduPilot SITL, not ArduPilot itself, and the plugin clears the lock automatically when the timer expires |
| `release_lapse_lock` | Release this driver's lapse lock; succeeds only when the returned holder count is zero, because a positive count means another holder still pauses the loop |

## Source and status

- Upstream: [aurelienroy/ardupilot_sitl_gazebo_plugin](https://github.com/aurelienroy/ardupilot_sitl_gazebo_plugin) at `75430fbc7796` (Apache-2.0); fetch it with `python3 scripts/add_device.py robots/aurelienroy__ardupilot_sitl_gazebo_plugin` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/robots/aurelienroy__ardupilot_sitl_gazebo_plugin`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/robots/aurelienroy__ardupilot_sitl_gazebo_plugin) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/robots/aurelienroy__ardupilot_sitl_gazebo_plugin/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/robots/aurelienroy__ardupilot_sitl_gazebo_plugin/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
