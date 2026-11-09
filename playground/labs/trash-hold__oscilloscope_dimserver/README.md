# Tektronix TDS3054C oscilloscope (oscilloscope_dimserver)

`labs/trash-hold__oscilloscope_dimserver` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Tektronix TDS3054C oscilloscope (oscilloscope_dimserver), adapted from trash-hold/oscilloscope_dimserver. It reads `horizontal_increment`; sets `channel`, `channel_enabled`, `vertical_scale`, `vertical_position` and 5 more; runs `single_acquisition` and `stop_acquisition`. `single_acquisition`: run one single-sequence acquisition and wait for it to finish (the native sample). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/trash-hold__oscilloscope_dimserver
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/trash-hold__oscilloscope_dimserver --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "oscilloscope_dimserver": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/trash-hold__oscilloscope_dimserver",
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

- **Reads:** `horizontal_increment`
- **Sets:** `channel`, `channel_enabled`, `vertical_scale`, `vertical_position`, `horizontal_scale`, `horizontal_position`, `trigger_channel`, `trigger_level`, `trigger_slope`

| Action | What it does |
| --- | --- |
| `single_acquisition` | Run one single-sequence acquisition and wait for it to finish (the native sample) |
| `stop_acquisition` | Stop the acquisition (ACQ:STATE STOP); this is the safe state and takes no input |

## Source and status

- Upstream: [trash-hold/oscilloscope_dimserver](https://github.com/trash-hold/oscilloscope_dimserver) at `6a34db58756f` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/trash-hold__oscilloscope_dimserver` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/trash-hold__oscilloscope_dimserver`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/trash-hold__oscilloscope_dimserver) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/trash-hold__oscilloscope_dimserver/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/trash-hold__oscilloscope_dimserver/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
