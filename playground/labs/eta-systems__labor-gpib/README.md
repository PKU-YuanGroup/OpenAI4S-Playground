# Rohde & Schwarz NGMO2 channel A

`labs/eta-systems__labor-gpib` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

Rohde & Schwarz NGMO2 channel A, adapted from eta-systems/labor-gpib. It reads `identity` and `status_byte`; sets `voltage_setpoint`, `current_limit`, `measurement_interval`, `averaging_samples` and 5 more; runs `measure_voltage`, `measure_current`, `output_off` and `scpi_rst`. `measure_voltage`: measure a DC or RMS voltage on a declared channel or terminal pair and return the value with its sampling timestamp and measurement range. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/eta-systems__labor-gpib
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/eta-systems__labor-gpib --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "labor-gpib": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/eta-systems__labor-gpib",
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

- **Reads:** `identity`, `status_byte`
- **Sets:** `voltage_setpoint`, `current_limit`, `measurement_interval`, `averaging_samples`, `output_enabled`, `sense_function`, `current_range`, `output_format`, `display_enabled`

| Action | What it does |
| --- | --- |
| `measure_voltage` | Measure a DC or RMS voltage on a declared channel or terminal pair and return the value with its sampling timestamp and measurement range. |
| `measure_current` | Measure current on a declared channel and return the value with its timestamp and range. |
| `output_off` | Send :OUT:A OFF: the safe state, with no input and no read-back wait |
| `scpi_rst` | Call device.reset (src/devices/rohde_schwarz_ngmo2.py:85-86). rst writes *RST (lines 81-83) and cls writes *CLS (lines 30-31). The comment on rst says this returns the supply to the *RST default conditions and does not state the output, the voltage, the current or the averaging. An ordinary command: the safety reset does not call it, and it is not a re-enable or a safe-state action. The three cached set points are refused before device.reset is called, including when that call raises, until this driver writes them. The operator confirms the instrument, including whether an output is enabled. |

## Source and status

- Upstream: [eta-systems/labor-gpib](https://github.com/eta-systems/labor-gpib) at `d5fe1b230344` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/eta-systems__labor-gpib` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/eta-systems__labor-gpib`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/eta-systems__labor-gpib) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/eta-systems__labor-gpib/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/eta-systems__labor-gpib/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
