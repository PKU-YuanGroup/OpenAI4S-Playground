# ZEUS liquid-handling module (zeus.ZeusModule)

`labs/nicholasmorrow__zeus` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

ZEUS liquid-handling module (zeus.ZeusModule), adapted from nicholasmorrow/zeus. It reads `z_position`; runs `initialize`, `move_z`, `pick_tip`, `discard_tip` and 3 more. `initialize`: initialize the Z-drive and the dosing drive (native initZDrive and initDosingDrive). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/nicholasmorrow__zeus
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/nicholasmorrow__zeus --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "zeus": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/nicholasmorrow__zeus",
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

- **Reads:** `z_position`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `initialize` | Initialize the Z-drive and the dosing drive (native initZDrive and initDosingDrive) |
| `move_z` | Command the Z-drive to a position at slow or fast speed (native GZ command) |
| `pick_tip` | Pick up a tip from a tip type and deck geometry table entry (native GT command) |
| `discard_tip` | Discard the tip at a deck geometry table entry (native GU command) |
| `aspirate` | Aspirate a volume with the dosing drive (native GA command) |
| `dispense` | Dispense a volume with the dosing drive (native GD command) |
| `emergency_stop` | Engage the native emergency stop (AB); it takes no input |

## Source and status

- Upstream: [nicholasmorrow/zeus](https://github.com/nicholasmorrow/zeus) at `d2f5dbc1bc4f` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/nicholasmorrow__zeus` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/nicholasmorrow__zeus`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/nicholasmorrow__zeus) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/nicholasmorrow__zeus/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/nicholasmorrow__zeus/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
