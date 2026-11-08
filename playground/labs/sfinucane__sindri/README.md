# Tektronix BERTScope bit error rate analyzer (sindri.tektronix.bertscope:BERTScope_TCP)

`labs/sfinucane__sindri` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Tektronix BERTScope bit error rate analyzer (sindri.tektronix.bertscope:BERTScope_TCP), adapted from sfinucane/sindri. It reads `identity`, `internal_temperature`, `running`, `detector_bit_count` and 6 more; sets `run_duration`; runs `start_run`, `halt_run`, `factory_reset` and `reset_detector_results`. `start_run`: start all systems within the BERTScope mainframe (RST 1). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/sfinucane__sindri
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/sfinucane__sindri --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sindri": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/sfinucane__sindri",
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

- **Reads:** `identity`, `internal_temperature`, `running`, `detector_bit_count`, `detector_error_count`, `detector_bit_error_rate`, `detector_elapsed_time`, `detector_resyncs`, `detector_error_free_bits_count`, `detector_error_free_time`
- **Sets:** `run_duration`

| Action | What it does |
| --- | --- |
| `start_run` | Start all systems within the BERTScope mainframe (RST 1) |
| `halt_run` | Stop all systems within the BERTScope mainframe (RST 0, the safe state); it takes no input |
| `factory_reset` | Set the instrument functions to the factory default power up state (*RST) |
| `reset_detector_results` | Reset the error detector results (DET:RRES) |

## Source and status

- Upstream: [sfinucane/sindri](https://github.com/sfinucane/sindri) at `d560635a28a5` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/sfinucane__sindri` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/sfinucane__sindri`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/sfinucane__sindri) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/sfinucane__sindri/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/sfinucane__sindri/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
