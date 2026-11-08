# IKA RCT digital 5 hotplate and magnetic stirrer (Minerva RCTDigital5)

`labs/bamresearch__mapz_at_bam` · Thermal and process control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

IKA RCT digital 5 hotplate and magnetic stirrer (Minerva RCTDigital5), adapted from bamresearch/mapz_at_bam. It reads `device_name`, `external_temperature`, `hotplate_temperature`, `stirring_speed` and 2 more; sets `temperature_setpoint` and `stirring_speed_setpoint`; runs `heat_to`, `start_stirring` and `stop_hotplate`. `heat_to`: set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/bamresearch__mapz_at_bam
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/bamresearch__mapz_at_bam --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "mapz_at_bam": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/bamresearch__mapz_at_bam",
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

- **Reads:** `device_name`, `external_temperature`, `hotplate_temperature`, `stirring_speed`, `viscosity_trend`, `safety_temperature`
- **Sets:** `temperature_setpoint`, `stirring_speed_setpoint`

| Action | What it does |
| --- | --- |
| `heat_to` | Set the target temperature of a thermal zone and optionally wait for the zone to reach the setpoint within a declared tolerance. |
| `start_stirring` | Start stirring at a speed; the speed is the setpoint used by the start command |
| `stop_hotplate` | Stop heating and stirring and reset both setpoints to zero (the safe state); takes no input |

## Source and status

- Upstream: [bamresearch/mapz_at_bam](https://github.com/bamresearch/mapz_at_bam) at `ad4cd71528aa` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/bamresearch__mapz_at_bam` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/bamresearch__mapz_at_bam`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/bamresearch__mapz_at_bam) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/bamresearch__mapz_at_bam/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/bamresearch__mapz_at_bam/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
