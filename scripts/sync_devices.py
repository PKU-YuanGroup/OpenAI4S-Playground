#!/usr/bin/env python3
"""Publish every OpenMHS market package: device.json, a README per device and CATALOG.md.

The source of truth is the pinned submodule's market index, ``mhs/MHS/drivers/market.json``
(``python3 -m mhs market build`` in OpenMHS). Upstream checkouts are fetched on demand.
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKET = ROOT / "mhs/MHS/drivers/market.json"
SITE = "https://mhs.openai4s.org"


def read(path):
    return json.loads(path.read_text())


def site_page(package):
    return f"{SITE}/market/{package}/"


def devices():
    existing = {read(path)["mhs_package"]: path.parent.relative_to(ROOT)
                for path in (ROOT / "playground").glob("**/device.json")}
    rows = []
    for entry in read(MARKET)["packages"]:
        key = entry["id"]
        served = f"mhs/MHS/drivers/{key}"
        folder = existing.get(served, Path("playground") / key)
        upstream = entry["upstream"]
        rows.append({
            "name": str(folder.relative_to("playground")), "package": key, "mhs_package": served,
            "title": entry["name"], "category": entry["category"], "topic": entry.get("topic"),
            "intro": entry["intro"], "website": site_page(key),
            "upstream": {"repo_url": upstream["repo_url"], "commit": upstream["commit"],
                         "license": upstream.get("license"), "path": str(folder / "upstream")},
            "family": entry.get("family"), "role": entry.get("role"),
            "mode": entry["mode"], "risk": entry["risk"], "backends": entry["backends"],
            "validation": {"backend": "fake", "status": entry.get("evidence", "contract_checked")},
            "install_openai4s": entry["install"]["openai4s"],
            "serve_http": f"PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve {served} --backend fake --port 7400",
            "serve_mcp": f"PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs serve {served} --backend fake --mcp",
            "_entry": entry,
        })
    return rows


def _names(items):
    return ", ".join(f"`{i}`" for i in items) or "—"


def device_readme(row):
    entry = row["_entry"]
    up = row["upstream"]
    short = row["package"].split("/", 1)[-1].split("__", 1)[-1]
    actions = "\n".join(f"| `{a['name']}` | {(a.get('description') or '').strip()} |" for a in entry["actions"])
    mode = ("simulation" if row["mode"] == "simulated"
            else "hardware driver, served here on its **fake backend** (no instrument needed)")
    mcp = json.dumps({"mcpServers": {short: {
        "command": "python3", "args": ["-m", "mhs", "serve", row["package"], "--mcp"],
        "env": {"PYTHONPATH": "/path/to/OpenMHS/MHS/sdk/src"}}}}, indent=2)
    lines = [
        f"# {row['title']}",
        "",
        f"`{row['package']}` · {row['category']}{' · ' + row['topic'] if row.get('topic') else ''} · {mode} · "
        f"risk {row['risk']} · licence {up['license'] or 'see upstream'}",
        "",
        entry["intro"],
        "",
        "## Install in one command",
        "",
        "Into the OpenAI4S Lab (fake backend; the lab starts and the agent can use it right away):",
        "",
        "```bash",
        row["install_openai4s"],
        "```",
        "",
        "First time? `git clone --recursive https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S && "
        "./setup.sh && source .venv/bin/activate`, then run the line above and `openai4s serve` "
        "(or use the Lab tab → Device market → Install).",
        "",
        "As a standalone OpenMHS endpoint, from this repository:",
        "",
        "```bash",
        "git submodule update --init mhs",
        row["serve_http"],
        "PYTHONPATH=mhs/MHS/sdk/src python3 -m mhs describe --endpoint http://127.0.0.1:7400",
        "```",
        "",
        "In any MCP host (Claude Desktop, Cursor, …):",
        "",
        "```json",
        mcp,
        "```",
        "",
        "## What it exposes",
        "",
        f"- **Reads:** {_names(entry['measures'])}",
        f"- **Sets:** {_names(entry['adjusts'])}",
        "",
    ]
    if actions:
        lines += ["| Action | What it does |", "| --- | --- |", actions, ""]
    lines += [
        "## Source and status",
        "",
        f"- Upstream: [{up['repo_url'].removeprefix('https://github.com/')}]({up['repo_url']}) at "
        f"`{(up['commit'] or '')[:12]}` ({up['license'] or 'licence: see upstream'}); fetch it with "
        f"`python3 scripts/add_device.py {row['package']}` only if you need the native backend.",
        f"- Driver and generated reference: [OpenMHS `MHS/drivers/{row['package']}`]"
        f"(https://github.com/PKU-YuanGroup/OpenMHS/tree/main/MHS/drivers/{row['package']}) · "
        f"[REFERENCE.md](https://github.com/PKU-YuanGroup/OpenMHS/blob/main/MHS/drivers/{row['package']}/REFERENCE.md)",
        f"- Website: {row['website']}",
        "- Validation: contract checked on the fake backend. That is not a hardware qualification; "
        "driving hardware is an explicit operator decision, and a software stop never replaces a hardware e-stop.",
        "",
    ]
    return "\n".join(lines)


def catalog(rows):
    groups = defaultdict(list)
    for row in rows:
        groups[row["category"]].append(row)
    order = sorted(groups, key=lambda c: (-len(groups[c]), c))
    out = [
        "# Device catalog",
        "",
        f"{len(rows)} OpenMHS market devices, grouped by category. Install any of them into the OpenAI4S Lab with",
        "`openai4s lab add <id>`; every page has the standalone and MCP commands too. Search and filter on",
        f"[{SITE}/market/]({SITE}/market/).",
        "",
        " · ".join(f"[{c} ({len(groups[c])})](#{c.lower().replace(' ', '-')})" for c in order),
        "",
    ]
    for category in order:
        out += [f"## {category}", "", "| Device | Mode | Risk | Install |", "| --- | --- | --- | --- |"]
        for row in sorted(groups[category], key=lambda r: r["title"].lower()):
            title = row["title"].replace("|", "\\|")
            out.append(f"| [{title}](playground/{row['name']}/README.md) | {row['mode']} | {row['risk']} | "
                       f"`openai4s lab add {row['package']}` |")
        out.append("")
    return "\n".join(out)


def outputs(rows):
    public = [{k: v for k, v in row.items() if not k.startswith("_")} for row in rows]
    result = {
        ROOT / "devices.json": json.dumps({"website": f"{SITE}/market/", "count": len(public), "devices": public},
                                          indent=2, ensure_ascii=False) + "\n",
        ROOT / "CATALOG.md": catalog(rows),
    }
    for row, doc in zip(rows, public):
        base = ROOT / "playground" / row["name"]
        result[base / "device.json"] = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
        result[base / "README.md"] = device_readme(row)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report catalog drift without writing")
    args = parser.parse_args()
    if not MARKET.is_file():
        parser.error("mhs/MHS/drivers/market.json not found; run `git submodule update --init mhs` "
                     "(an OpenMHS with `mhs market`)")
    rows = devices()
    different = []
    for path, text in outputs(rows).items():
        if not path.is_file() or path.read_text() != text:
            different.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)
    if args.check and different:
        parser.exit(1, "catalog drift: " + ", ".join(different[:10]) + "\n")
    print(f"{len(rows)} market packages; {len(different)} {'stale' if args.check else 'updated'} files")


if __name__ == "__main__":
    main()
