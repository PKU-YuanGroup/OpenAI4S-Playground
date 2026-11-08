# Agilent 33600A arbitrary waveform generator

`labs/samdejong86__agilent33600` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Agilent 33600A arbitrary waveform generator, adapted from samdejong86/agilent33600. It reads `identity`; sets `frequency`, `amplitude`, `offset`, `function` and 2 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/samdejong86__agilent33600
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/samdejong86__agilent33600 --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "agilent33600": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/samdejong86__agilent33600",
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

- **Reads:** `identity`
- **Sets:** `frequency`, `amplitude`, `offset`, `function`, `waveform`, `sample_rate`

## Source and status

- Upstream: [samdejong86/agilent33600](https://github.com/samdejong86/agilent33600) at `262275ddb4e1` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/samdejong86__agilent33600` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/samdejong86__agilent33600`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/samdejong86__agilent33600) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/samdejong86__agilent33600/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/samdejong86__agilent33600/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
