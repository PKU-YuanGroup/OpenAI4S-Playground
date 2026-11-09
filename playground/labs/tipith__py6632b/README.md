# HP 6632B DC source (py6632B.HP6632B)

`labs/tipith__py6632b` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

HP 6632B DC source (py6632B.HP6632B), adapted from tipith/py6632b. It reads `voltage`, `current`, `output_enabled` and `identity`; runs `set_source`, `set_output` and `stop_output`. `set_source`: set the output voltage and current limit together with one native SOUR:VOLT/CURR command. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/tipith__py6632b
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/tipith__py6632b --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "py6632b": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/tipith__py6632b",
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

- **Reads:** `voltage`, `current`, `output_enabled`, `identity`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `set_source` | Set the output voltage and current limit together with one native SOUR:VOLT/CURR command |
| `set_output` | Enable or disable the source output |
| `stop_output` | Disable the source output (the safe state); it takes no input |

## Source and status

- Upstream: [tipith/py6632b](https://github.com/tipith/py6632b) at `a91f78a004f5` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/tipith__py6632b` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/tipith__py6632b`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/tipith__py6632b) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/tipith__py6632b/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/tipith__py6632b/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
