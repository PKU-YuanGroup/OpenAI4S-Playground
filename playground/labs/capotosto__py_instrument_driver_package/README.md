# Keysight E4980A precision LCR meter

`labs/capotosto__py_instrument_driver_package` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

Keysight E4980A precision LCR meter, adapted from capotosto/py_instrument_driver_package. It reads `aperture_mode`, `aperture_averages`, `dc_bias_autorange`, `correction_method` and 7 more; sets `measurement_function`, `frequency`, `voltage_level`, `current_level` and 5 more; runs `fetch_formatted`, `fetch_impedance`, `fetch_vac`, `fetch_iac` and 4 more. `fetch_formatted`: fetch the latest formatted measurement: primary value, secondary value and status code. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/capotosto__py_instrument_driver_package
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/capotosto__py_instrument_driver_package --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "py_instrument_driver_package": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/capotosto__py_instrument_driver_package",
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

- **Reads:** `aperture_mode`, `aperture_averages`, `dc_bias_autorange`, `correction_method`, `data_format`, `ascii_long`, `exponent_digits`, `trigger_source`, `trigger_delay`, `initiate_continuous`, `impedance_autorange`
- **Sets:** `measurement_function`, `frequency`, `voltage_level`, `current_level`, `alc`, `dc_bias_state`, `dc_bias_voltage`, `cable_length`, `impedance_range`

| Action | What it does |
| --- | --- |
| `fetch_formatted` | Fetch the latest formatted measurement: primary value, secondary value and status code |
| `fetch_impedance` | Fetch corrected impedance as resistance and reactance |
| `fetch_vac` | Fetch the monitored AC voltage (:FETCh:SMONitor:VAC?) |
| `fetch_iac` | Fetch the monitored AC current (:FETCh:SMONitor:IAC?) |
| `fetch_vdc` | Fetch the monitored DC voltage (:FETCh:SMONitor:VDC?) |
| `fetch_idc` | Fetch the monitored DC current (:FETCh:SMONitor:IDC?) |
| `read_error` | Read and remove one entry of the instrument error queue (:SYSTem:ERRor?) |
| `set_aperture` | Set the measurement time mode and averaging rate |

## Source and status

- Upstream: [capotosto/py_instrument_driver_package](https://github.com/capotosto/py_instrument_driver_package) at `1512bb3c1d76` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/capotosto__py_instrument_driver_package` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/capotosto__py_instrument_driver_package`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/capotosto__py_instrument_driver_package) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/capotosto__py_instrument_driver_package/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/capotosto__py_instrument_driver_package/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
