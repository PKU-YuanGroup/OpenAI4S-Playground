# ECE Tool Suite oscilloscope (ece_suite.instruments.keysight.KeysightScope)

`labs/karimrayttu__ece-tool-suite` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

ECE Tool Suite oscilloscope (ece_suite.instruments.keysight.KeysightScope), adapted from karimrayttu/ece-tool-suite. It reads `identity` and `measurements`; runs `measure_item`, `measure_vpp`, `capture`, `run` and 3 more. `measure_item`: read one scalar automatic measurement from the scope's current measurement set. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/karimrayttu__ece-tool-suite
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/karimrayttu__ece-tool-suite --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ece-tool-suite": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/karimrayttu__ece-tool-suite",
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

- **Reads:** `identity`, `measurements`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `measure_item` | Read one scalar automatic measurement from the scope's current measurement set |
| `measure_vpp` | Measure peak-to-peak voltage on channel 1 (:MEAS:VPP?) |
| `capture` | Capture channel 1 and report a scalar summary of the record; the waveform array itself is not transferred |
| `run` | Start continuous acquisition (:RUN) |
| `single` | Arm one acquisition (:SINGle) |
| `reset_instrument` | Reset the scope to its default setup (*RST and *CLS) |
| `stop_acquisition` | Stop acquisition (:STOP, the safe state); it takes no input |

## Source and status

- Upstream: [karimrayttu/ece-tool-suite](https://github.com/karimrayttu/ece-tool-suite) at `13f7962a674e` (MIT); fetch it with `python3 scripts/add_device.py labs/karimrayttu__ece-tool-suite` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/karimrayttu__ece-tool-suite`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/karimrayttu__ece-tool-suite) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/karimrayttu__ece-tool-suite/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/karimrayttu__ece-tool-suite/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
