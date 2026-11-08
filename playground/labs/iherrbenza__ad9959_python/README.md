# AD9959 four-channel DDS (DDS_ESP32_lab.DDS_ESP32)

`labs/iherrbenza__ad9959_python` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

AD9959 four-channel DDS (DDS_ESP32_lab.DDS_ESP32), adapted from iherrbenza/ad9959_python. It sets `frequency`, `amplitude` and `phase`; runs `mute`. `mute`: set every channel amplitude word to 0 (the safe state); it takes no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/iherrbenza__ad9959_python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/iherrbenza__ad9959_python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ad9959_python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/iherrbenza__ad9959_python",
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

- **Reads:** —
- **Sets:** `frequency`, `amplitude`, `phase`

| Action | What it does |
| --- | --- |
| `mute` | Set every channel amplitude word to 0 (the safe state); it takes no input |

## Source and status

- Upstream: [iherrbenza/ad9959_python](https://github.com/iherrbenza/ad9959_python) at `cd5298ec17fe` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/iherrbenza__ad9959_python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/iherrbenza__ad9959_python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/iherrbenza__ad9959_python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/iherrbenza__ad9959_python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/iherrbenza__ad9959_python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
