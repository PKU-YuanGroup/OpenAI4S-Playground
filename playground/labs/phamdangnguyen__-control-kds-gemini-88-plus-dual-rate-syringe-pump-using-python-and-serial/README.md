# KDS Gemini 88 Plus dual-rate syringe pump

`labs/phamdangnguyen__-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

KDS Gemini 88 Plus dual-rate syringe pump, adapted from phamdangnguyen/-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial. It reads `status` and `running`; sets `syringe_volume`, `diameter`, `target_time`, `target_volume` and 1 more; runs `syringe`, `run` and `stop_pump`. `syringe`: select the syringe for both channels with 'syr {channel} {code} {index}'. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/phamdangnguyen__-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/phamdangnguyen__-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/phamdangnguyen__-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial",
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

- **Reads:** `status`, `running`
- **Sets:** `syringe_volume`, `diameter`, `target_time`, `target_volume`, `flow_rate`

| Action | What it does |
| --- | --- |
| `syringe` | Select the syringe for both channels with 'syr {channel} {code} {index}' |
| `run` | Run the configured pump program on the selected channel(s) with 'run {channel}' |
| `stop_pump` | Stop both pump channels with 'stop ab' (the native stop and the safe state); takes no input |

## Source and status

- Upstream: [phamdangnguyen/-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial](https://github.com/phamdangnguyen/-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial) at `ab6a02be981e` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/phamdangnguyen__-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/phamdangnguyen__-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/phamdangnguyen__-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/phamdangnguyen__-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/phamdangnguyen__-control-kds-gemini-88-plus-dual-rate-syringe-pump-using-python-and-serial/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
