# Tecan FluentControl liquid handler (fluent_control_automation.FluentControlClient)

`labs/aaronslaff__tecan_fluentcontrol` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Tecan FluentControl liquid handler (fluent_control_automation.FluentControlClient), adapted from aaronslaff/tecan_fluentcontrol. It reads `instrument_status`, `deck_layout` and `transfer_status`; runs `post_transfer_session`, `start_transfer_session`, `get_transfer_status`, `cancel_transfer_session` and 1 more. `post_transfer_session`: post one source-to-destination transfer and create a transfer session. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/aaronslaff__tecan_fluentcontrol
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/aaronslaff__tecan_fluentcontrol --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "tecan_fluentcontrol": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/aaronslaff__tecan_fluentcontrol",
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

- **Reads:** `instrument_status`, `deck_layout`, `transfer_status`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `post_transfer_session` | Post one source-to-destination transfer and create a transfer session |
| `start_transfer_session` | Start the transfer session with the given id |
| `get_transfer_status` | Read the status of the transfer session with the given id |
| `cancel_transfer_session` | Cancel the transfer session with the given id |
| `cancel_active_transfer` | Cancel the active transfer session (the safe state); it takes no input |

## Source and status

- Upstream: [aaronslaff/tecan_fluentcontrol](https://github.com/aaronslaff/tecan_fluentcontrol) at `5bbff1713f97` (MIT); fetch it with `python3 scripts/add_device.py labs/aaronslaff__tecan_fluentcontrol` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/aaronslaff__tecan_fluentcontrol`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/aaronslaff__tecan_fluentcontrol) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/aaronslaff__tecan_fluentcontrol/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/aaronslaff__tecan_fluentcontrol/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
