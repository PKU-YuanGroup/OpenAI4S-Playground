# Siglent SDS2000X Plus through lxkang00/oscilloscope-mcp (SCPI transport)

`labs/lxkang00__oscilloscope-mcp` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence NOASSERTION

Siglent SDS2000X Plus through lxkang00/oscilloscope-mcp (SCPI transport), adapted from lxkang00/oscilloscope-mcp. It reads `identity`, `trigger_status` and `acquisition_state`; runs `acquisition_control`, `configure_channel`, `get_channel`, `configure_timebase` and 18 more. `acquisition_control`: send one acquisition control: run, stop, autoset, force trigger, clear measurement statistics or factory reset. The driver sends the same SCPI word the pinned handler sends. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/lxkang00__oscilloscope-mcp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/lxkang00__oscilloscope-mcp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "oscilloscope-mcp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/lxkang00__oscilloscope-mcp",
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

- **Reads:** `identity`, `trigger_status`, `acquisition_state`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `acquisition_control` | Send one acquisition control: run, stop, autoset, force trigger, clear measurement statistics or factory reset. The driver sends the same SCPI word the pinned handler sends. |
| `configure_channel` | Set analog channel settings with the pinned :CHANnelN: commands; reply is the handler summary. |
| `get_channel` | Read the eight settings the pinned get_channel handler reads. A native failure is reported as a failed call instead of being hidden behind the handler's N/A fallback. |
| `configure_timebase` | Set main timebase scale, delay and mode under :TIMebase:. |
| `get_timebase` | Read timebase scale, delay and mode. |
| `configure_trigger` | Set trigger sweep, type, source, level, slope, coupling and holdoff in the pinned order. |
| `get_trigger` | Read the current trigger type, sweep, source, level and slope. |
| `configure_acquisition` | Set acquisition mode, memory depth, interpolation and average count under :ACQuire:. |
| `get_acquisition` | Read acquisition mode, memory depth, sample rate and interpolation. |
| `measure` | Select and read one automatic measurement item. The reply is the pinned handler's text; the numeric value is parsed from the same reply and is null when it is not a number. |
| `get_measure_stats` | Read count, mean, minimum, maximum and standard deviation of the measurement statistics. |
| `get_waveform_preamble` | Read and parse the ten-field waveform preamble. The waveform sample array is not carried by this binding. |
| `configure_display` | Set display grid, persistence, intensity, grid style and axis mode. |
| `configure_cursors` | Set cursor mode, sources and manual cursor type. |
| `get_cursor_values` | Read cursor mode and, when cursors are on, delta X and delta Y. |
| `configure_math` | Set math display, function, sources, scale, offset and FFT options. |
| `configure_digital` | Set digital-bus display, position, height, label and threshold on MSO models. |
| `save_setup` | Save the current setup to internal memory or USB with the pinned filename validation. |
| `recall_setup` | Recall a saved setup from internal memory or USB with the pinned filename validation. |
| `get_frequency_counter` | Read the hardware frequency counter mode, source and current frequency. |
| `get_status` | Read acquisition state, trigger state, operation complete and event status register. |
| `get_next_error` | Read and clear the next device error-queue entry. |

## Source and status

- Upstream: [lxkang00/oscilloscope-mcp](https://github.com/lxkang00/oscilloscope-mcp) at `3eebcdfb3c33` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/lxkang00__oscilloscope-mcp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/lxkang00__oscilloscope-mcp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/lxkang00__oscilloscope-mcp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/lxkang00__oscilloscope-mcp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/lxkang00__oscilloscope-mcp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
