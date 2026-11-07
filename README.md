# OpenAI4S-Playground

Devices and simulators that [OpenAI4S](https://github.com/PKU-YuanGroup/OpenAI4S) can use through
[OpenMHS](https://github.com/PKU-YuanGroup/OpenMHS), an open standard and SDK for model-to-hardware control.
OpenMHS is an independent open-source project, not affiliated with or endorsed by Anthropic.

## Layout

| Path | What it holds |
|---|---|
| `mhs/` | OpenMHS as a submodule: the specification, the standard-library SDK and its driver packages. |
| `playground/<device>/upstream/` | The device's own repository as a shallow submodule, pinned to the commit its OpenMHS package was checked against. |
| `playground/<device>/device.json` | The OpenMHS package that serves the device, and the commands that serve it. |
| `scripts/add_device.py` | Adds another OpenMHS package and its upstream repository. |

## Quick start

Python 3.10 or newer; the SDK needs no third-party package.

```bash
git clone --recurse-submodules --shallow-submodules https://github.com/PKU-YuanGroup/OpenAI4S-Playground.git
cd OpenAI4S-Playground
export PYTHONPATH=mhs/MHS/sdk/src
python3 -m mhs serve mhs/MHS/drivers/robots/huggingface__gym-pusht --backend fake --port 7400
# in a second terminal
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

Each `device.json` lists the same commands for its device (`serve_http`, and `serve_mcp` for the MCP projection on
stdio).

## Devices

| Device | OpenMHS package | Upstream (licence) |
|---|---|---|
| Gymnasium CartPole-v1 (classic control) | `robots/farama-foundation__gymnasium` | farama-foundation/gymnasium (MIT) |
| PushT 2D manipulation (PushT-v0) | `robots/huggingface__gym-pusht` | huggingface/gym-pusht (Apache-2.0) |
| ALOHA bimanual insertion (AlohaInsertion-v0) | `robots/huggingface__gym-aloha` | huggingface/gym-aloha (Apache-2.0) |
| RWARE warehouse with one agent | `robots/semitable__robotic-warehouse` | semitable/robotic-warehouse (MIT) |
| UR5 with a Jaco hand in CoppeliaSim | `robots/pnnayyeri__gym-ur5` | pnnayyeri/gym-ur5 (MIT) |
| Discrete Muller-Brown potential | `labs/jjgoings__gym-muller_brown` | jjgoings/gym-muller_brown (MIT) |

All six are simulations at risk R0 whose packages pass the OpenMHS gate.

## Connecting OpenAI4S

OpenAI4S reaches each served device as an MCP connector. The integration is experimental and disabled by default. See
[`mhs/integration/openai4s/README.md`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/integration/openai4s) for the
reference host and the OpenAI4S guide `docs/openmhs.md`.

## Safety

- The `fake` backend runs without the upstream code. The `sim` backend needs the upstream package installed from
  `playground/<device>/upstream`.
- No device here drives hardware. An OpenMHS hardware backend needs a human reviewer's signature (`reviewed_by`) and an
  explicit operator decision (`--allow-hardware --arm`) before it starts.
- OpenMHS is a supervisory software contract, not a safety certification, and never replaces a hardware emergency stop.

## Adding a device

```bash
python3 scripts/add_device.py robots/<owner>__<repo> [--name <folder>]
```

The script accepts only packages that pass the OpenMHS gate. Check the upstream licence before you add a repository.
