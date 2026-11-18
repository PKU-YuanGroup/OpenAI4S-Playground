#!/usr/bin/env python3
"""Fetch a catalog device's pinned upstream checkout when you need its native backend."""
import argparse
import subprocess

from sync_devices import ROOT, read


def git(*args, cwd):
    subprocess.run(["git", *args], cwd=cwd, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", help="a catalog package, e.g. robots/huggingface__gym-pusht")
    args = parser.parse_args()
    rows = {row["package"]: row for row in read(ROOT / "devices.json")["devices"]}
    if args.package not in rows:
        parser.error("package is not in devices.json; run scripts/sync_devices.py after updating mhs")
    row = rows[args.package]
    upstream = row["upstream"]
    checkout = ROOT / upstream["path"]
    # A checkout has its own .git. A featured submodule that was never initialised is an empty directory: git would
    # answer "rev-parse HEAD" there with this repository's commit.
    if not (checkout / ".git").exists():
        if checkout.exists() and any(checkout.iterdir()):
            parser.error(f"{upstream['path']} exists, is not empty and is not a git checkout")
        tracked = subprocess.check_output(["git", "ls-files", "--stage", "--", upstream["path"]], cwd=ROOT, text=True)
        if tracked.startswith("160000 "):  # one of the featured submodules
            git("submodule", "update", "--init", "--depth", "1", "--", upstream["path"], cwd=ROOT)
        else:
            checkout.parent.mkdir(parents=True, exist_ok=True)
            git("clone", "--no-checkout", "--depth", "1", upstream["repo_url"], str(checkout), cwd=ROOT)
            git("fetch", "--depth", "1", "origin", upstream["commit"], cwd=checkout)
            git("checkout", "--detach", upstream["commit"], cwd=checkout)
    actual = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=checkout, text=True).strip()
    if actual != upstream["commit"]:
        parser.error(f"the checkout is at {actual}; the catalog expects {upstream['commit']}")
    print(f"{row['package']}: {checkout.relative_to(ROOT)} at {upstream['commit']}")


if __name__ == "__main__":
    main()
