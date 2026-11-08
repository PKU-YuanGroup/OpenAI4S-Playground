# TCD1304 linear CCD (TCD1304Rev2Controller)

`labs/drmcnelson__linear-ccd-with-ltspice-kicad-firmware-and-python-library` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence CC-BY-NC-SA-4.0

TCD1304 linear CCD (TCD1304Rev2Controller), adapted from drmcnelson/linear-ccd-with-ltspice-kicad-firmware-and-python-library. It reads `identifier`, `configuration`, `pixel_count`, `dark_pixel_count` and 1 more; runs `measure_intensity` and `set_holdoff`. `measure_intensity`: measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/drmcnelson__linear-ccd-with-ltspice-kicad-firmware-and-python-library
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/drmcnelson__linear-ccd-with-ltspice-kicad-firmware-and-python-library --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "linear-ccd-with-ltspice-kicad-firmware-and-python-library": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/drmcnelson__linear-ccd-with-ltspice-kicad-firmware-and-python-library",
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

- **Reads:** `identifier`, `configuration`, `pixel_count`, `dark_pixel_count`, `sensor`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `measure_intensity` | Measure optical or radiant intensity at a declared wavelength or channel and return the value with its unit and integration time. |
| `set_holdoff` | Set the firmware sync holdoff time, the delay the firmware's 'set holdoff usecs' command configures (help.txt:82) |

## Source and status

- Upstream: [drmcnelson/linear-ccd-with-ltspice-kicad-firmware-and-python-library](https://github.com/drmcnelson/linear-ccd-with-ltspice-kicad-firmware-and-python-library) at `fcda5364d1ec` (CC-BY-NC-SA-4.0); fetch it with `python3 scripts/add_device.py labs/drmcnelson__linear-ccd-with-ltspice-kicad-firmware-and-python-library` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/drmcnelson__linear-ccd-with-ltspice-kicad-firmware-and-python-library`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/drmcnelson__linear-ccd-with-ltspice-kicad-firmware-and-python-library) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/drmcnelson__linear-ccd-with-ltspice-kicad-firmware-and-python-library/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/drmcnelson__linear-ccd-with-ltspice-kicad-firmware-and-python-library/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
