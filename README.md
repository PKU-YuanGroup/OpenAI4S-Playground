# OpenAI4S-Playground

The device market for [OpenAI4S](https://github.com/PKU-YuanGroup/OpenAI4S), powered by
[OpenMHS — Model Hardware Standard](https://mhs.openai4s.org).

**746 devices** — laboratory instruments, robots and simulators — each with an introduction and a one-line install.
Browse them in **[CATALOG.md](CATALOG.md)** (by category), on **[mhs.openai4s.org/market](https://mhs.openai4s.org/market/)**
(search and filters), or in [devices.json](devices.json). Every device folder under [playground/](playground/) has a
`README.md` with what it does and how to run it, and a `device.json`.

## Install a device in one command

Into the OpenAI4S Lab, where the agent can use it right away:

```bash
git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git
cd OpenAI4S && ./setup.sh && source .venv/bin/activate
openai4s lab add labs/tiagocoutinho__julabo     # any id from CATALOG.md
openai4s serve                                 # open the Lab tab
```

Or, in the workbench: **Lab** tab → **Device market** → **Install**. Each device runs on its fake backend (hardware
drivers) or a pure-Python stand-in (simulators), so no instrument, simulator install or upstream checkout is needed.

## Run a device without OpenAI4S

Python 3.10 or newer, standard library only:

```bash
git clone https://github.com/PKU-YuanGroup/OpenAI4S-Playground.git
cd OpenAI4S-Playground
git submodule update --init mhs
export PYTHONPATH=mhs/MHS/sdk/src
python3 -m mhs market search pipette                            # find devices
python3 -m mhs serve labs/tiagocoutinho__julabo --port 7400      # serve one (fake backend)
python3 -m mhs describe --endpoint http://127.0.0.1:7400         # in another terminal
```

`python3 -m mhs serve <id> --mcp` serves the MCP projection for any MCP host; each device README has a ready
`mcpServers` snippet. `validation` in `device.json` records the fake contract check; native simulation and hardware use
need their own environment and device setup.

## Upstream sources on demand

The adapted drivers ship in `mhs/`; you can use their fake backends immediately.
Fetch an upstream checkout only when needed:

```bash
python3 scripts/add_device.py robots/huggingface__gym-pusht
```

The script checks out the exact commit in the catalog. Install upstream dependencies according to its README.
The original six featured simulator submodules remain available with `git submodule update --init --depth 1`.

## Update the catalog

```bash
git -C mhs pull --ff-only
python3 scripts/sync_devices.py          # devices.json, CATALOG.md, playground/*/device.json and README.md
python3 scripts/sync_devices.py --check
```

The catalog is generated from the pinned OpenMHS submodule's market index (`mhs/MHS/drivers/market.json`): every
package whose gate passed. Blocked packages stay in OpenMHS's registry.
Each upstream repository retains its own license; this catalog records it without relicensing its sources.

## Connect OpenAI4S

Follow the [OpenAI4S OpenMHS guide](https://github.com/PKU-YuanGroup/OpenAI4S/blob/main/docs/openmhs.md):
`openai4s lab add <id>` installs a device through an MCP connector (default) or the native MHS tools (`--via mhs`). The [reference host guide](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/integration/openai4s)
covers endpoint configuration and evidence.

Hardware access remains an explicit operator choice. The endpoint enforces limits, interlocks and emergency stops;
a software stop does not replace a hardware emergency stop.
