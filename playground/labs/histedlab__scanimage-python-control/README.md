# ScanImage remote control (py_json_client.ScanimageTcpipClient)

`labs/histedlab__scanimage-python-control` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

ScanImage remote control (py_json_client.ScanimageTcpipClient), adapted from histedlab/scanimage-python-control. It sets `scan_zoom_factor`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/histedlab__scanimage-python-control
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/histedlab__scanimage-python-control --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "scanimage-python-control": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/histedlab__scanimage-python-control",
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

- **Reads:** —
- **Sets:** `scan_zoom_factor`

## Source and status

- Upstream: [histedlab/scanimage-python-control](https://github.com/histedlab/scanimage-python-control) at `9de4309aef95` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/histedlab__scanimage-python-control` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/histedlab__scanimage-python-control`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/histedlab__scanimage-python-control) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/histedlab__scanimage-python-control/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/histedlab__scanimage-python-control/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
