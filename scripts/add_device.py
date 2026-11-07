#!/usr/bin/env python3
"""Add an OpenMHS driver package to the playground.

The upstream repository becomes a shallow submodule at the commit the package's driver.lock.json pins, and
playground/<name>/device.json says which package serves it and how.

    python3 scripts/add_device.py robots/huggingface__gym-pusht [--name gym-pusht]
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRIVERS = ROOT / "mhs" / "MHS" / "drivers"


def git(*args, cwd=ROOT):
    subprocess.run(["git", *args], cwd=cwd, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("package", help="a package under mhs/MHS/drivers, for example robots/huggingface__gym-pusht")
    parser.add_argument("--name", help="folder name under playground/ (default: the repository name)")
    args = parser.parse_args()

    package = DRIVERS / args.package
    result = json.loads((package / "RESULT.json").read_text())
    if result.get("status") != "pass":
        sys.exit(f"{args.package} does not pass the OpenMHS gate (status {result.get('status')})")
    lock = json.loads((package / "driver.lock.json").read_text())
    task = json.loads((package / "task.json").read_text())
    upstream = lock["upstream"]
    name = args.name or args.package.split("/")[-1].split("__", 1)[-1]
    folder = Path("playground") / name
    checkout = folder / "upstream"

    if not (ROOT / checkout).exists():
        git("submodule", "add", "--depth", "1", upstream["repo_url"], str(checkout))
        git("config", "-f", ".gitmodules", f"submodule.{checkout}.shallow", "true")
        git("fetch", "--depth", "1", "origin", upstream["commit"], cwd=ROOT / checkout)
        git("checkout", "-q", upstream["commit"], cwd=ROOT / checkout)

    served = f"mhs/MHS/drivers/{args.package}"
    device = {
        "name": name,
        "mhs_package": served,
        "upstream": {"repo_url": upstream["repo_url"], "commit": upstream["commit"],
                     "license": upstream.get("license_spdx"), "path": str(checkout)},
        "family": task.get("family"),
        "role": task.get("role"),
        "backends": sorted((lock.get("backends") or {}).keys()),
        "serve_http": f"PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve {served} --backend fake --port 7400",
        "serve_mcp": f"PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve {served} --backend fake --mcp",
    }
    (ROOT / folder / "device.json").write_text(json.dumps(device, indent=2) + "\n")
    git("add", str(folder), ".gitmodules")
    print(f"added {name}: {upstream['repo_url']} at {upstream['commit'][:12]}")


if __name__ == "__main__":
    main()
