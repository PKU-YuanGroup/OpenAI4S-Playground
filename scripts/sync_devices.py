#!/usr/bin/env python3
"""Publish every passing OpenMHS package; upstream checkouts are fetched on demand."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRIVERS = ROOT / "mhs/MHS/drivers"


def read(path):
    return json.loads(path.read_text())


def devices():
    existing = {read(path)["mhs_package"]: path.parent.relative_to(ROOT)
                for path in (ROOT / "playground").glob("**/device.json")}
    rows = []
    for result_path in sorted(DRIVERS.glob("*/*/RESULT.json")):
        if read(result_path)["status"] != "pass":
            continue
        package = result_path.parent
        key = package.relative_to(DRIVERS).as_posix()
        served = f"mhs/MHS/drivers/{key}"
        folder = existing.get(served, Path("playground") / key)
        lock = read(package / "driver.lock.json")
        task = read(package / "task.json")
        reference = read(package / "reference.json")
        upstream = lock["upstream"]
        rows.append({
            "name": str(folder.relative_to("playground")), "package": key, "mhs_package": served,
            "website": "https://mhs.openai4s.org",
            "upstream": {"repo_url": upstream["repo_url"], "commit": upstream["commit"],
                         "license": upstream.get("license_spdx"), "path": str(folder / "upstream")},
            "family": task.get("family"), "role": task.get("role"),
            "mode": reference["device"]["mode"], "risk": reference["device"]["risk"],
            "backends": sorted(lock["backends"]),
            "validation": {"backend": "fake", "status": "contract_checked"},
            "serve_http": f"PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve {served} --backend fake --port 7400",
            "serve_mcp": f"PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve {served} --backend fake --mcp",
        })
    return rows


def outputs(rows):
    result = {ROOT / "devices.json": {"website": "https://mhs.openai4s.org", "count": len(rows), "devices": rows}}
    for row in rows:
        result[ROOT / "playground" / row["name"] / "device.json"] = row
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report catalog drift without writing")
    args = parser.parse_args()
    rows = devices()
    if not rows:
        parser.error("no passing packages found; initialize the mhs submodule first")
    different = []
    for path, document in outputs(rows).items():
        text = json.dumps(document, indent=2, ensure_ascii=False) + "\n"
        if not path.is_file() or path.read_text() != text:
            different.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)
    if args.check and different:
        parser.exit(1, "catalog drift: " + ", ".join(different[:10]) + "\n")
    print(f"{len(rows)} passing packages; {len(different)} {'stale' if args.check else 'updated'} files")


if __name__ == "__main__":
    main()
