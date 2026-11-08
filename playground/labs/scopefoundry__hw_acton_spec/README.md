# Acton spectrometer (acton_spec_interface:ActonSpectrometer)

`labs/scopefoundry__hw_acton_spec` · Spectroscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence BSD-3-Clause

Acton spectrometer (acton_spec_interface:ActonSpectrometer), adapted from scopefoundry/hw_acton_spec. It reads `done_status`, `grating_name` and `turret`; sets `center_wl`, `grating_id`, `exit_mirror`, `entrance_slit` and 1 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/scopefoundry__hw_acton_spec
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/scopefoundry__hw_acton_spec --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "hw_acton_spec": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/scopefoundry__hw_acton_spec",
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

- **Reads:** `done_status`, `grating_name`, `turret`
- **Sets:** `center_wl`, `grating_id`, `exit_mirror`, `entrance_slit`, `exit_slit`

## Source and status

- Upstream: [scopefoundry/hw_acton_spec](https://github.com/scopefoundry/hw_acton_spec) at `a4e112406b7f` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/scopefoundry__hw_acton_spec` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/scopefoundry__hw_acton_spec`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/scopefoundry__hw_acton_spec) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/scopefoundry__hw_acton_spec/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/scopefoundry__hw_acton_spec/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
