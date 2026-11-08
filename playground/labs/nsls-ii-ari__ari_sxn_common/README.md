# ARI M1 mirror section (ari_sxn_common, read only)

`labs/nsls-ii-ari__ari_sxn_common` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R0 · licence BSD-3-Clause

ARI M1 mirror section (ari_sxn_common, read only), adapted from nsls-ii-ari/ari_sxn_common. It reads `ry_coarse`, `ry_fine`, `rz`, `x` and 20 more. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/nsls-ii-ari__ari_sxn_common
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/nsls-ii-ari__ari_sxn_common --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "ari_sxn_common": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/nsls-ii-ari__ari_sxn_common",
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

- **Reads:** `ry_coarse`, `ry_fine`, `rz`, `x`, `y`, `slit_top`, `slit_bottom`, `slit_inboard`, `slit_outboard`, `diag_blade`, `diag_filter`, `diag_current1`, `diag_current2`, `diag_current3`, `diag_current4`, `slit_current1`, `slit_current2`, `slit_current3`, `slit_current4`, `vacuum_ccg`, `vacuum_tcg`, `vacuum_ip`, `locations`, `read_photocurrent`
- **Sets:** —

## Source and status

- Upstream: [nsls-ii-ari/ari_sxn_common](https://github.com/nsls-ii-ari/ari_sxn_common) at `13892fc39dd2` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/nsls-ii-ari__ari_sxn_common` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/nsls-ii-ari__ari_sxn_common`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/nsls-ii-ari__ari_sxn_common) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/nsls-ii-ari__ari_sxn_common/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/nsls-ii-ari__ari_sxn_common/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
