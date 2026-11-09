# Syringe pump over serial (ctrl-syringe-pumps)

`labs/giansimone__ctrl-syringe-pumps` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence MIT

Syringe pump over serial (ctrl-syringe-pumps), adapted from giansimone/ctrl-syringe-pumps. It sets `diameter`, `direction` and `pumping_rate`; runs `run_pump`, `stop_pump`, `test_pump` and `reverse_direction`. `run_pump`: start the pump (RUN). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/giansimone__ctrl-syringe-pumps
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/giansimone__ctrl-syringe-pumps --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ctrl-syringe-pumps": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/giansimone__ctrl-syringe-pumps",
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
- **Sets:** `diameter`, `direction`, `pumping_rate`

| Action | What it does |
| --- | --- |
| `run_pump` | Start the pump (RUN) |
| `stop_pump` | Stop the pump (STP); the safe-state action |
| `test_pump` | Send the version/test command (VER) |
| `reverse_direction` | Reverse the flow for the selected pump (DIR REV) |

## Source and status

- Upstream: [giansimone/ctrl-syringe-pumps](https://github.com/giansimone/ctrl-syringe-pumps) at `3b0d31540034` (MIT); fetch it with `python3 scripts/add_device.py labs/giansimone__ctrl-syringe-pumps` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/giansimone__ctrl-syringe-pumps`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/giansimone__ctrl-syringe-pumps) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/giansimone__ctrl-syringe-pumps/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/giansimone__ctrl-syringe-pumps/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
