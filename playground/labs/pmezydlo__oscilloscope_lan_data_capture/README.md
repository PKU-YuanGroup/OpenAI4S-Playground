# Rigol DS1000Z series oscilloscope (oscilloscope_functions.oscilloscope)

`labs/pmezydlo__oscilloscope_lan_data_capture` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence NOASSERTION

Rigol DS1000Z series oscilloscope (oscilloscope_functions.oscilloscope), adapted from pmezydlo/oscilloscope_lan_data_capture. It reads `manufacturer`, `instrument_model`, `serial_number`, `firmware_version` and 4 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pmezydlo__oscilloscope_lan_data_capture
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pmezydlo__oscilloscope_lan_data_capture --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "oscilloscope_lan_data_capture": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pmezydlo__oscilloscope_lan_data_capture",
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

- **Reads:** `manufacturer`, `instrument_model`, `serial_number`, `firmware_version`, `active_channels`, `timebase_scale_s_per_div`, `timebase_offset_s`, `settings`
- **Sets:** —

## Source and status

- Upstream: [pmezydlo/oscilloscope_lan_data_capture](https://github.com/pmezydlo/oscilloscope_lan_data_capture) at `f68c0b8d5acb` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/pmezydlo__oscilloscope_lan_data_capture` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pmezydlo__oscilloscope_lan_data_capture`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pmezydlo__oscilloscope_lan_data_capture) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pmezydlo__oscilloscope_lan_data_capture/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pmezydlo__oscilloscope_lan_data_capture/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
