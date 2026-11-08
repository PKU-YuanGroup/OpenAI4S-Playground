# Thorlabs compact spectrometer (pyCCT SpectrometerWrapper)

`labs/hslarson__speck-lab-goniometer` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Thorlabs compact spectrometer (pyCCT SpectrometerWrapper), adapted from hslarson/speck-lab-goniometer. It reads `device_id`; sets `manual_exposure`, `hardware_average`, `input_hw_trigger_enabled`, `input_hw_trigger_average_no_wait` and 3 more; runs `acquire_spectrum`. `acquire_spectrum`: acquire an optical or mass spectrum over a declared wavelength or mass range and return the axis and intensity arrays, or an artifact reference for large spectra. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/hslarson__speck-lab-goniometer
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/hslarson__speck-lab-goniometer --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "speck-lab-goniometer": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/hslarson__speck-lab-goniometer",
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

- **Reads:** `device_id`
- **Sets:** `manual_exposure`, `hardware_average`, `input_hw_trigger_enabled`, `input_hw_trigger_average_no_wait`, `input_hw_trigger_falling_edge`, `output_hw_trigger_delay`, `use_amplitude_correction`

| Action | What it does |
| --- | --- |
| `acquire_spectrum` | Acquire an optical or mass spectrum over a declared wavelength or mass range and return the axis and intensity arrays, or an artifact reference for large spectra. |

## Source and status

- Upstream: [hslarson/speck-lab-goniometer](https://github.com/hslarson/speck-lab-goniometer) at `9ca84d8c8c6c` (MIT); fetch it with `python3 scripts/add_device.py labs/hslarson__speck-lab-goniometer` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/hslarson__speck-lab-goniometer`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/hslarson__speck-lab-goniometer) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/hslarson__speck-lab-goniometer/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/hslarson__speck-lab-goniometer/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
