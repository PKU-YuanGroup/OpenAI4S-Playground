# RIGOL DP832A DC power supply

`labs/majidbenk__interfaz-virtual-control-remoto-instrumentos-rigol` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

RIGOL DP832A DC power supply, adapted from majidbenk/interfaz-virtual-control-remoto-instrumentos-rigol. It reads `measured_voltage_1`, `measured_voltage_2`, `measured_voltage_3`, `measured_current_1` and 5 more; sets `voltage_1`, `voltage_2`, `voltage_3`, `current_1` and 11 more; runs `output_off`. `output_off`: disable all three channel outputs; the safe state of the supply. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/majidbenk__interfaz-virtual-control-remoto-instrumentos-rigol
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/majidbenk__interfaz-virtual-control-remoto-instrumentos-rigol --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "interfaz-virtual-control-remoto-instrumentos-rigol": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/majidbenk__interfaz-virtual-control-remoto-instrumentos-rigol",
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

- **Reads:** `measured_voltage_1`, `measured_voltage_2`, `measured_voltage_3`, `measured_current_1`, `measured_current_2`, `measured_current_3`, `measured_power_1`, `measured_power_2`, `measured_power_3`
- **Sets:** `voltage_1`, `voltage_2`, `voltage_3`, `current_1`, `current_2`, `current_3`, `ovp_1`, `ovp_2`, `ovp_3`, `ocp_1`, `ocp_2`, `ocp_3`, `out_1`, `out_2`, `out_3`

| Action | What it does |
| --- | --- |
| `output_off` | Disable all three channel outputs; the safe state of the supply |

## Source and status

- Upstream: [majidbenk/interfaz-virtual-control-remoto-instrumentos-rigol](https://github.com/majidbenk/interfaz-virtual-control-remoto-instrumentos-rigol) at `770ab3a1f816` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/majidbenk__interfaz-virtual-control-remoto-instrumentos-rigol` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/majidbenk__interfaz-virtual-control-remoto-instrumentos-rigol`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/majidbenk__interfaz-virtual-control-remoto-instrumentos-rigol) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/majidbenk__interfaz-virtual-control-remoto-instrumentos-rigol/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/majidbenk__interfaz-virtual-control-remoto-instrumentos-rigol/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
