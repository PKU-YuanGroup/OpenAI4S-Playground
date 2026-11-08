# Rigol DHO oscilloscope through rigol-dho-mcp (controlled MCP contract)

`labs/mattjax16__rigol-dho-mcp` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence MIT

Rigol DHO oscilloscope through rigol-dho-mcp (controlled MCP contract), adapted from mattjax16/rigol-dho-mcp. It reads `trigger_status`; runs `identify`, `get_status`, `run_control`, `configure_channel` and 12 more. `identify`: query the *IDN? identity string through the identify tool. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/mattjax16__rigol-dho-mcp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/mattjax16__rigol-dho-mcp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "rigol-dho-mcp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/mattjax16__rigol-dho-mcp",
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

- **Reads:** `trigger_status`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `identify` | Query the *IDN? identity string through the identify tool. |
| `get_status` | Read trigger status, sample rate, memory depth, acquisition type, timebase and enabled-channel settings, as the strings the scope returns. |
| `run_control` | Send one acquisition control (run, stop, single, autoset, clear, force_trigger); the reply carries the queried trigger status. |
| `configure_channel` | Change only the supplied analog-channel settings; returns the queried channel settings (no inversion readback). |
| `configure_timebase` | Set the main timebase scale and/or offset; returns the queried values. |
| `configure_trigger_edge` | Set EDGE trigger mode, then the supplied source, slope, level and sweep; returns the queried trigger settings and status. |
| `configure_acquisition` | Set memory depth, acquisition type and average count; returns the queried values and sample rate. |
| `configure_cursors` | Set the cursor mode (OFF, MANual, TRACk) with type and source or track sources; returns the queried mode. Coordinates use the typed cursor bindings. |
| `get_cursor_values` | Read cursor positions and deltas of the active mode; the complete result is a JSON artifact. |
| `get_measurement` | Select and read one automatic measurement item on one channel (SI units); selecting is a scope write. |
| `measure_between` | Select and read a delay (s) or phase (degrees) item between two channels; selecting is a scope write. |
| `get_waveform` | Capture the screen or deep-memory waveform: statistics plus every returned decimated time/voltage sample, as a JSON artifact. Memory mode needs a fresh STOP status first. |
| `get_screenshot` | Capture the scope display as a PNG image artifact. |
| `configure_cursors_time` | Manual TIME cursors: sets type TIME and cursor A/B coordinates in seconds. |
| `configure_cursors_amplitude` | Manual AMPLitude cursors: sets type AMPLitude and cursor A/B coordinates in volts. |
| `configure_cursors_current` | Manual cursors on the retained type: enters MANual, reads the type, applies only that axis's candidates and omits cursor_type. An unreadable type leaves the mode change unresolved. |

## Source and status

- Upstream: [mattjax16/rigol-dho-mcp](https://github.com/mattjax16/rigol-dho-mcp) at `f9ac71918698` (MIT); fetch it with `python3 scripts/add_device.py labs/mattjax16__rigol-dho-mcp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/mattjax16__rigol-dho-mcp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/mattjax16__rigol-dho-mcp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/mattjax16__rigol-dho-mcp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/mattjax16__rigol-dho-mcp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
