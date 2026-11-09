# SRS SR865 lock-in amplifier

`labs/naqslab__naqslab_devices` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

SRS SR865 lock-in amplifier, adapted from naqslab/naqslab_devices. It reads `tau_index` and `sens_index`; sets `time_constant`, `sensitivity` and `phase`. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/naqslab__naqslab_devices
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/naqslab__naqslab_devices --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "naqslab_devices": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/naqslab__naqslab_devices",
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

- **Reads:** `tau_index`, `sens_index`
- **Sets:** `time_constant`, `sensitivity`, `phase`

## Source and status

- Upstream: [naqslab/naqslab_devices](https://github.com/naqslab/naqslab_devices) at `2c0ac4fb715e` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/naqslab__naqslab_devices` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/naqslab__naqslab_devices`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/naqslab__naqslab_devices) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/naqslab__naqslab_devices/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/naqslab__naqslab_devices/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
