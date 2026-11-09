# Jackson Labs Low Noise Rubidium GNSDO

`labs/pangea567__gnsdo-scpi-simulator` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence MIT

Jackson Labs Low Noise Rubidium GNSDO, adapted from pangea567/gnsdo-scpi-simulator. It reads `identity`, `sync_locked`, `tint`, `health` and 14 more; runs `start_holdover`, `recover_from_holdover`, `set_sync_source` and `set_ptime_output`. `start_holdover`: put the oscillator into holdover (the device keeps the last known frequency without GPS). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pangea567__gnsdo-scpi-simulator
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pangea567__gnsdo-scpi-simulator --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "gnsdo-scpi-simulator": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pangea567__gnsdo-scpi-simulator",
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

- **Reads:** `identity`, `sync_locked`, `tint`, `health`, `satellites_tracked`, `satellites_visible`, `pcb_temperature`, `tcxo_voltage`, `power_supply_voltage`, `csac_temperature`, `csac_status`, `lifetime`, `csac_lifetime`, `leap_seconds`, `ptime_output`, `ptime_date`, `ptime_time`, `holdover_duration`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `start_holdover` | Put the oscillator into holdover (the device keeps the last known frequency without GPS) |
| `recover_from_holdover` | End holdover and return the oscillator to its reference |
| `set_sync_source` | Set the synchronization source mode; the clone's documentation names GPS, EXTERNAL and INTERNAL as examples, and the upstream setter stores any non-empty value |
| `set_ptime_output` | Enable or disable the PTIME time-sharing output |

## Source and status

- Upstream: [pangea567/gnsdo-scpi-simulator](https://github.com/pangea567/gnsdo-scpi-simulator) at `a2d57a9759ab` (MIT); fetch it with `python3 scripts/add_device.py labs/pangea567__gnsdo-scpi-simulator` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pangea567__gnsdo-scpi-simulator`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pangea567__gnsdo-scpi-simulator) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pangea567__gnsdo-scpi-simulator/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pangea567__gnsdo-scpi-simulator/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
