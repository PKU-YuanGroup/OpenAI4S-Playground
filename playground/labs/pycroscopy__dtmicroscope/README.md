# DTMicroscope TEM client (DTMicroscope.base.twisted_client.TEMClient)

`labs/pycroscopy__dtmicroscope` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

DTMicroscope TEM client (DTMicroscope.base.twisted_client.TEMClient), adapted from pycroscopy/dtmicroscope. It reads `detectors`, `microscope_status` and `vacuum`; sets `stage` and `beam_position`; runs `acquire_image` and `acquire_spectrum`. `acquire_image`: acquire a microscope image of the current field of view for a declared channel, exposure, binning and region of interest, returning an image artifact. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/pycroscopy__dtmicroscope
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/pycroscopy__dtmicroscope --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "dtmicroscope": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/pycroscopy__dtmicroscope",
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

- **Reads:** `detectors`, `microscope_status`, `vacuum`
- **Sets:** `stage`, `beam_position`

| Action | What it does |
| --- | --- |
| `acquire_image` | Acquire a microscope image of the current field of view for a declared channel, exposure, binning and region of interest, returning an image artifact. |
| `acquire_spectrum` | Acquire one spectrum from a detector and return its samples |

## Source and status

- Upstream: [pycroscopy/dtmicroscope](https://github.com/pycroscopy/dtmicroscope) at `17245ba6df42` (MIT); fetch it with `python3 scripts/add_device.py labs/pycroscopy__dtmicroscope` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/pycroscopy__dtmicroscope`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/pycroscopy__dtmicroscope) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/pycroscopy__dtmicroscope/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/pycroscopy__dtmicroscope/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
