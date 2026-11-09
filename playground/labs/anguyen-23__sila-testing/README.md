# PerkinElmer Opera Phenix (PhenixImager SiLA 2 feature)

`labs/anguyen-23__sila-testing` · Optics and microscopy · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence NOASSERTION

PerkinElmer Opera Phenix (PhenixImager SiLA 2 feature), adapted from anguyen-23/sila-testing. It reads `IsConnected`, `DeviceState`, `StagePosition`, `PlateDetected` and 6 more; runs `phenix_connect`, `phenix_disconnect`, `phenix_stagein`, `phenix_stageout` and 5 more. `phenix_connect`: open the RCI connection to the named Phenix host and return the device name. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/anguyen-23__sila-testing
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/anguyen-23__sila-testing --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "sila-testing": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/anguyen-23__sila-testing",
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

- **Reads:** `IsConnected`, `DeviceState`, `StagePosition`, `PlateDetected`, `AvailableProtocols`, `DeviceDescription`, `execution_known`, `execution_uuid`, `acquisition_progress`, `last_progress_info`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `phenix_connect` | Open the RCI connection to the named Phenix host and return the device name. |
| `phenix_disconnect` | Close the RCI connection. |
| `phenix_stagein` | Move the stage from Transfer to Operate (RCI LOAD); a plate must already be on the stage. |
| `phenix_stageout` | Move the stage from Operate to Transfer (RCI EJECT) so the plate can be removed. |
| `phenix_stop` | Stop the running acquisition protocol (RCI STOP); the e-stop of this package. |
| `phenix_goidle` | Return the device to Idle (RCI IDLE). |
| `phenix_gostandby` | Put the device into Standby for DurationSeconds before it wakes up (RCI STANDBY). |
| `phenix_runacquisitionprotocol` | Run a named acquisition protocol on the plate; progress per well; ejects when done. |
| `phenix_displayicon` | Publish the instrument icon PNG as an artifact (a UI icon, not an acquired image). |

## Source and status

- Upstream: [anguyen-23/sila-testing](https://github.com/anguyen-23/sila-testing) at `0b572380e069` (NOASSERTION); fetch it with `python3 scripts/add_device.py labs/anguyen-23__sila-testing` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/anguyen-23__sila-testing`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/anguyen-23__sila-testing) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/anguyen-23__sila-testing/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/anguyen-23__sila-testing/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
