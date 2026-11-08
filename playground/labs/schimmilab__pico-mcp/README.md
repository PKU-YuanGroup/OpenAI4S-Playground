# PicoScope 5000A/B series oscilloscope (pico_mcp.scope.Scope)

`labs/schimmilab__pico-mcp` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

PicoScope 5000A/B series oscilloscope (pico_mcp.scope.Scope), adapted from schimmilab/pico-mcp. It reads `connected`, `variant`, `serial`, `resolution_bits` and 1 more; sets `channel_a_enabled`, `channel_a_coupling`, `channel_a_range_v`, `channel_b_enabled` and 8 more; runs `set_signal_generator`, `stop_signal_generator` and `capture_block`. `set_signal_generator`: configure the built-in signal generator (AWG) through ps5000aSetSigGenBuiltInV2. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/schimmilab__pico-mcp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/schimmilab__pico-mcp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "pico-mcp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/schimmilab__pico-mcp",
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

- **Reads:** `connected`, `variant`, `serial`, `resolution_bits`, `max_adc`
- **Sets:** `channel_a_enabled`, `channel_a_coupling`, `channel_a_range_v`, `channel_b_enabled`, `channel_b_coupling`, `channel_b_range_v`, `channel_c_enabled`, `channel_c_coupling`, `channel_c_range_v`, `channel_d_enabled`, `channel_d_coupling`, `channel_d_range_v`

| Action | What it does |
| --- | --- |
| `set_signal_generator` | Configure the built-in signal generator (AWG) through ps5000aSetSigGenBuiltInV2 |
| `stop_signal_generator` | Turn the built-in signal generator off (DC at 0 V); the safe state, no input |
| `capture_block` | Capture one block on all enabled channels and return the scalar measurements |

## Source and status

- Upstream: [schimmilab/pico-mcp](https://github.com/schimmilab/pico-mcp) at `08fd81ee1c1e` (MIT); fetch it with `python3 scripts/add_device.py labs/schimmilab__pico-mcp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/schimmilab__pico-mcp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/schimmilab__pico-mcp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/schimmilab__pico-mcp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/schimmilab__pico-mcp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
