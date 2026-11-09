# Leica LASAF CAM server (leicacam.CAM)

`labs/martinhjelmare__leicacam` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

Leica LASAF CAM server (leicacam.CAM), adapted from martinhjelmare/leicacam. It reads `stage_information`; runs `start_matrix_scan`, `stop_matrix_scan`, `pause_matrix_scan`, `autofocus_scan` and 4 more. `start_matrix_scan`: start the matrix scan (the CAM startscan command). A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/martinhjelmare__leicacam
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/martinhjelmare__leicacam --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "leicacam": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/martinhjelmare__leicacam",
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

- **Reads:** `stage_information`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `start_matrix_scan` | Start the matrix scan (the CAM startscan command) |
| `stop_matrix_scan` | Stop the matrix scan (the CAM stopscan command), the safe state of the scan |
| `pause_matrix_scan` | Toggle the pause of the matrix scan (the CAM pausescan command) |
| `autofocus_scan` | Start the matrix focus scan (the CAM autofocusscan command) |
| `enable_scan_field` | Enable one scan field of the experiment matrix (the CAM enable command with value true) |
| `disable_scan_field` | Disable one scan field of the experiment matrix (the CAM enable command with value false) |
| `enable_all_scan_fields` | Enable every scan field of the experiment matrix (the CAM enableall command with value true) |
| `disable_all_scan_fields` | Disable every scan field of the experiment matrix (the CAM enableall command with value false) |

## Source and status

- Upstream: [martinhjelmare/leicacam](https://github.com/martinhjelmare/leicacam) at `5c33a0d6daa1` (MIT); fetch it with `python3 scripts/add_device.py labs/martinhjelmare__leicacam` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/martinhjelmare__leicacam`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/martinhjelmare__leicacam) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/martinhjelmare__leicacam/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/martinhjelmare__leicacam/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
