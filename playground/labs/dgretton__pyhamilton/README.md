# Hamilton liquid handler (pyhamilton.HamiltonInterface)

`labs/dgretton__pyhamilton` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Hamilton liquid handler (pyhamilton.HamiltonInterface), adapted from dgretton/pyhamilton. It reads `is_open` and `server_exited`; runs `initialize`, `aspirate`, `dispense`, `move_plate` and 3 more. `initialize`: initialize the Hamilton robot (the upstream INITIALIZE command) and wait for its response. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/dgretton__pyhamilton
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/dgretton__pyhamilton --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pyhamilton": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/dgretton__pyhamilton",
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

- **Reads:** `is_open`, `server_exited`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `initialize` | Initialize the Hamilton robot (the upstream INITIALIZE command) and wait for its response |
| `aspirate` | Aspirate a volume from one well with one pipetting channel and the named Hamilton liquid class; it does not attach or eject a tip |
| `dispense` | Dispense a volume into one well with one pipetting channel and the named Hamilton liquid class; it does not attach or eject a tip |
| `move_plate` | Move a plate from one Hamilton sequence to another with the iSWAP (ISWAP_GET then ISWAP_PLACE) |
| `set_labware_property` | Set one property of one labware item in the Hamilton run (the upstream SET_LABWARE_PROPERTY command) |
| `shutdown_interface` | Stop the Hamilton interface (the native stop): signal the server thread and terminate the OEM process; it takes no input |
| `start_interface` | Start the Hamilton interface again after a safety reset (the declared re-enable): HamiltonInterface.start() relaunches the OEM process (or the server or simulation process) that the stop terminated; the clone does not say whether that start moves the instrument. It takes no input, is refused while the e-stop is latched and is never run by the reset |

## Source and status

- Upstream: [dgretton/pyhamilton](https://github.com/dgretton/pyhamilton) at `65938d05cc8f` (MIT); fetch it with `python3 scripts/add_device.py labs/dgretton__pyhamilton` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/dgretton__pyhamilton`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/dgretton__pyhamilton) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/dgretton__pyhamilton/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/dgretton__pyhamilton/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
