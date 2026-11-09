# DvG Arduino lock-in amplifier (Alia_protocol_serial.Alia)

`labs/dennis-van-gils__dvg_arduino_lock-in_amp` · Electronics and measurement · hardware driver, served here on its **fake backend** (no instrument needed) · risk R1 · licence MIT

DvG Arduino lock-in amplifier (Alia_protocol_serial.Alia), adapted from dennis-van-gils/dvg_arduino_lock-in_amp. It reads `ref_clipping_high`, `ref_clipping_low`, `adc_autocal_valid`, `adc_autocal_gaincorr` and 4 more; sets `ref_waveform`, `ref_freq`, `ref_offset`, `ref_amplitude` and 1 more; runs `start_acquisition` and `stop_acquisition`. `start_acquisition`: start the lock-in acquisition (the native on command); it takes no input. A hardware driver: the market serves its fake backend, so no instrument is needed.

## Install in one command

Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):

```bash
openai4s lab add labs/dennis-van-gils__dvg_arduino_lock-in_amp
```

First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && ./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` (or use the Lab tab → Device market → Install).

As a standalone OpenMHS endpoint, from this repository:

```bash
git submodule update --init mhs
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve mhs/MHS/drivers/labs/dennis-van-gils__dvg_arduino_lock-in_amp --backend fake --port 7400
PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400
```

In any MCP host (Claude Desktop, Cursor, …):

```json
{
  "mcpServers": {
    "dvg_arduino_lock-in_amp": {
      "command": "python3",
      "args": [
        "-m",
        "mhs",
        "serve",
        "labs/dennis-van-gils__dvg_arduino_lock-in_amp",
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

- **Reads:** `ref_clipping_high`, `ref_clipping_low`, `adc_autocal_valid`, `adc_autocal_gaincorr`, `adc_autocal_offsetcorr`, `sampling_rate`, `block_size`, `running`
- **Sets:** `ref_waveform`, `ref_freq`, `ref_offset`, `ref_amplitude`, `ref_amplitude_rms`

| Action | What it does |
| --- | --- |
| `start_acquisition` | Start the lock-in acquisition (the native on command); it takes no input |
| `stop_acquisition` | Stop the lock-in acquisition (the native off command, the safe state); it takes no input |

## Source and status

- Upstream: [dennis-van-gils/dvg_arduino_lock-in_amp](https://github.com/dennis-van-gils/dvg_arduino_lock-in_amp) at `64c0f18f9111` (MIT); fetch it with `python3 scripts/add_device.py labs/dennis-van-gils__dvg_arduino_lock-in_amp` only if you need the native backend.
- Driver and generated reference: [OpenMHS `MHS/drivers/labs/dennis-van-gils__dvg_arduino_lock-in_amp`](https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/labs/dennis-van-gils__dvg_arduino_lock-in_amp) · [REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/labs/dennis-van-gils__dvg_arduino_lock-in_amp/REFERENCE.md)
- Website: https://mhs.openai4s.org/market/labs/dennis-van-gils__dvg_arduino_lock-in_amp/
- Validation: contract checked on the fake backend. That is not a hardware qualification; driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.
