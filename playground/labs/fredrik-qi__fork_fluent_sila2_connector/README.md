# Tecan Fluent liquid handler

`labs/fredrik-qi__fork_fluent_sila2_connector` · Liquid handling and fluidics · hardware driver, served here on its **fake backend** (no instrument needed) · risk R2 · licence BSD-3-Clause

Tecan Fluent liquid handler, adapted from fredrik-qi/fork_fluent_sila2_connector. It reads `state`, `progress`, `last_error`, `runnable_methods` and 1 more; runs `start_fluent`, `prepare_method`, `run_method`, `pause_run` and 9 more. `start_fluent`: start FluentControl or attach to a running instance without credentials; the connector may wait without a timeout and then prepares the method 'Method to prepare'. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/fredrik-qi__fork_fluent_sila2_connector
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/fredrik-qi__fork_fluent_sila2_connector --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "fork_fluent_sila2_connector": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/fredrik-qi__fork_fluent_sila2_connector",
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

- **Reads:** `state`, `progress`, `last_error`, `runnable_methods`, `variable_names`
- **Sets:** —

| Action | What it does |
| --- | --- |
| `start_fluent` | Start FluentControl or attach to a running instance without credentials; the connector may wait without a timeout and then prepares the method 'Method to prepare' |
| `prepare_method` | Prepare a FluentControl method; the connector deletes the Journaling/000 and Journaling/ToDelete directories before preparing |
| `run_method` | Run the currently prepared FluentControl method |
| `pause_run` | Pause the current FluentControl method; this is not the safe-state stop |
| `resume_run` | Resume a method paused by pause_run |
| `stop_method` | Stop the running method (SilaFluentController.StopMethod) and confirm that State reads RunModeRunFinished or EditMode; it takes no input |
| `aspirate` | Aspirate with the connector's fixed 8-tip A1 selection; it requires a live execution channel and passes the volume, labware, liquid class and well offset through unchanged |
| `dispense` | Dispense with the connector's fixed A1-H1 8-tip selection; it requires a live execution channel and passes the volume, labware, liquid class and well offset through unchanged |
| `drop_tips` | Drop the mounted disposable tips into the named labware |
| `set_location` | Set the location of a labware on the worktable |
| `transfer_labware` | Transfer labware on the worktable with the RGA |
| `transfer_labware_back_to_base` | Transfer labware back to the spot where it was added to the worktable |
| `set_variable_value` | Set a variable of the prepared method and read it back |

## Source and status

- Upstream: [fredrik-qi/fork_fluent_sila2_connector](https://github.com/fredrik-qi/fork_fluent_sila2_connector) at `4a2f857c619c` (BSD-3-Clause); fetch it with `python3 scripts/add_device.py labs/fredrik-qi__fork_fluent_sila2_connector` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/fredrik-qi__fork_fluent_sila2_connector`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/fredrik-qi__fork_fluent_sila2_connector) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/fredrik-qi__fork_fluent_sila2_connector/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/fredrik-qi__fork_fluent_sila2_connector/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
