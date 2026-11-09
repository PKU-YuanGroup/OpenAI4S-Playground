# Agilent E8257D PSG signal generator

`labs/smithsonian__rxlab-instruments` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Agilent E8257D PSG signal generator, adapted from smithsonian/rxlab-instruments. It reads `identity`; sets `frequency`, `power` and `output_enabled`; runs `scpi_rst`. `scpi_rst`: call GenericInstrument.reset, which writes '*RST' (labinstruments/generic.py:65-68). The docstring says only 'Reset instrument' and does not state the effect on the RF output, the frequency or the power. An ordinary command: the safety reset does not call it, and it is not a re-enable or a safe-state action. A later read returns the instrument's reply and does not state what '*RST' set. The operator confirms the instrument, including whether the RF output is enabled. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/smithsonian__rxlab-instruments
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/smithsonian__rxlab-instruments --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "rxlab-instruments": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/smithsonian__rxlab-instruments",
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

- **Reads:** `identity`
- **Sets:** `frequency`, `power`, `output_enabled`

| Action | What it does |
| --- | --- |
| `scpi_rst` | Call GenericInstrument.reset, which writes '*RST' (labinstruments/generic.py:65-68). The docstring says only 'Reset instrument' and does not state the effect on the RF output, the frequency or the power. An ordinary command: the safety reset does not call it, and it is not a re-enable or a safe-state action. A later read returns the instrument's reply and does not state what '*RST' set. The operator confirms the instrument, including whether the RF output is enabled. |

## Source and status

- Upstream: [smithsonian/rxlab-instruments](https://github.com/smithsonian/rxlab-instruments) at `2fbf8e6913e9` (MIT); fetch it with `python3 scripts/add_device.py labs/smithsonian__rxlab-instruments` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/smithsonian__rxlab-instruments`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/smithsonian__rxlab-instruments) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/smithsonian__rxlab-instruments/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/smithsonian__rxlab-instruments/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
