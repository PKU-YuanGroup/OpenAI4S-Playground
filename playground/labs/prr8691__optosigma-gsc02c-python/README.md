# OptoSigma GSC-02C delay stage (optosigma_gsc02c.GSC02C)

`labs/prr8691__optosigma-gsc02c-python` · Motion control · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence NOASSERTION

OptoSigma GSC-02C delay stage (optosigma_gsc02c.GSC02C), adapted from prr8691/optosigma-gsc02c-python. It reads `position_mm`, `position_pulses`, `busy` and `status`; runs `configure_motion`, `move_absolute_mm`, `move_relative_mm`, `move_absolute_pulses` and 3 more. `configure_motion`: set the D: motion ramp used by later moves. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/prr8691__optosigma-gsc02c-python
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/prr8691__optosigma-gsc02c-python --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "optosigma-gsc02c-python": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/prr8691__optosigma-gsc02c-python",
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

- **Reads:** `position_mm`, `position_pulses`, `busy`, `status`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `configure_motion` | Set the D: motion ramp used by later moves |
| `move_absolute_mm` | Move to an absolute position in millimetres (A: then G:) |
| `move_relative_mm` | Move by a distance in millimetres (M: then G:) |
| `move_absolute_pulses` | Move to an absolute controller coordinate in pulses (A: then G:) |
| `move_relative_pulses` | Move by a signed number of pulses (M: then G:) |
| `home` | Run the controller's mechanical-origin search (H:) |
| `stop_motion` | Stop motion with the controller's native controlled deceleration (L:) |

## Source and status

- Upstream: [prr8691/optosigma-gsc02c-python](https://github.com/prr8691/optosigma-gsc02c-python) at `d3403dc83f62` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/prr8691__optosigma-gsc02c-python` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/prr8691__optosigma-gsc02c-python`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/prr8691__optosigma-gsc02c-python) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/prr8691__optosigma-gsc02c-python/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/prr8691__optosigma-gsc02c-python/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
