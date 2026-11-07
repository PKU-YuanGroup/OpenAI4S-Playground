# OpenAI4S-Playground

The device catalog for [OpenAI4S](https://github.com/PKU-YuanGroup/OpenAI4S), powered by
[OpenMHS — Model Hardware Standard](https://mhs.openai4s.org).

All **746 passing adaptations** are included: laboratory instruments, robots and simulators.
Browse [devices.json](devices.json), or the `device.json` files under [playground/](playground/).
Each entry gives its upstream commit and license, declared mode and risk, and commands to serve its fake backend.
The catalog is generated from the pinned OpenMHS submodule; blocked packages stay in OpenMHS's registry.

## Quick start

Python 3.10 or newer. The fake backend needs only the standard library.

```bash
git clone https://github.com/PKU-YuanGroup/OpenAI4S-Playground.git
cd OpenAI4S-Playground
git submodule update --init mhs
export PYTHONPATH=mhs/MHS/sdk/src
python3 -m mhs serve mhs/MHS/drivers/robots/huggingface__gym-pusht --backend fake --port 7400
# In another terminal
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

Use any catalog entry's `serve_http` or `serve_mcp` command to start another package.
Commands use the fake backend by default. `validation` records fake contract checks; native simulation and
hardware use require their own environment and device setup.

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
python3 scripts/sync_devices.py
python3 scripts/sync_devices.py --check
```

Passing packages are included regardless of historical internal publication-review labels.
Each upstream repository retains its own license; this catalog records it without relicensing its sources.

## Connect OpenAI4S

Follow the [OpenAI4S integration guide](https://github.com/PKU-YuanGroup/OpenAI4S/blob/feat/openmhs-integration/docs/openmhs.md)
to enable the MCP connector. The [reference host guide](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/integration/openai4s)
covers endpoint configuration and evidence.

Hardware access remains an explicit operator choice. The endpoint enforces limits, interlocks and emergency stops;
a software stop does not replace a hardware emergency stop.
