# Siglent SDG 2042X function/arbitrary waveform generator

`labs/quantumllama__python-lab-drivers` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Siglent SDG 2042X function/arbitrary waveform generator, adapted from quantumllama/python-lab-drivers. It sets `output`, `waveform`, `frequency`, `amplitude` and 2 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/quantumllama__python-lab-drivers
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/quantumllama__python-lab-drivers --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "python-lab-drivers": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/quantumllama__python-lab-drivers",
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
- **Sets:** `output`, `waveform`, `frequency`, `amplitude`, `offset`, `duty_cycle`

## Source and status

- Upstream: [quantumllama/python-lab-drivers](https://github.com/quantumllama/python-lab-drivers) at `3fee8226c25d` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/quantumllama__python-lab-drivers` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/quantumllama__python-lab-drivers`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/quantumllama__python-lab-drivers) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/quantumllama__python-lab-drivers/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/quantumllama__python-lab-drivers/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
