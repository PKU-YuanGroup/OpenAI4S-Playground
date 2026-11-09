# Nion STEM instrument (nion.device_kit.InstrumentDevice:Instrument)

`labs/nion-software__nionswift-instrumentation-kit` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R3 · licence GPL-3.0

Nion STEM instrument (nion.device_kit.InstrumentDevice:Instrument), adapted from nion-software/nionswift-instrumentation-kit. It reads `beam_current_a`; sets `beam_voltage`, `defocus_m` and `energy_offset_ev`; runs `high_tension_off`. `high_tension_off`: remove the high tension: write the EHT control as 0 through the value manager; no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/nion-software__nionswift-instrumentation-kit
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/nion-software__nionswift-instrumentation-kit --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "nionswift-instrumentation-kit": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/nion-software__nionswift-instrumentation-kit",
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

- **Reads:** `beam_current_a`
- **Sets:** `beam_voltage`, `defocus_m`, `energy_offset_ev`

| Action | What it does |
| --- | --- |
| `high_tension_off` | Remove the high tension: write the EHT control as 0 through the value manager; no input |

## Source and status

- Upstream: [nion-software/nionswift-instrumentation-kit](https://github.com/nion-software/nionswift-instrumentation-kit) at `4db575faa502` (GPL-3.0); fetch it with `python3 scripts/add_device.py labs/nion-software__nionswift-instrumentation-kit` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/nion-software__nionswift-instrumentation-kit`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/nion-software__nionswift-instrumentation-kit) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/nion-software__nionswift-instrumentation-kit/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/nion-software__nionswift-instrumentation-kit/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
