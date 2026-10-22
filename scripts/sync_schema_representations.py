#!/usr/bin/env python3
"""Keep the published YAML schema representation identical to odps.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
JSON_SCHEMA = ROOT / "source" / "schema" / "odps.json"
YAML_SCHEMA = ROOT / "source" / "schema" / "odps.yaml"
GENERATED_HEADER = (
    "# Generated from source/schema/odps.json. "
    "Run python3 scripts/sync_schema_representations.py --write to refresh.\n"
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="regenerate source/schema/odps.yaml from odps.json")
    args = parser.parse_args()

    json_schema = json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))
    if args.write:
        YAML_SCHEMA.write_text(
            GENERATED_HEADER
            + yaml.safe_dump(
                json_schema,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,
                width=120,
            ),
            encoding="utf-8",
        )
        print(f"Wrote {YAML_SCHEMA.relative_to(ROOT)} from {JSON_SCHEMA.relative_to(ROOT)}.")
        return 0

    yaml_schema = yaml.safe_load(YAML_SCHEMA.read_text(encoding="utf-8"))
    if json_schema != yaml_schema:
        print("Schema representations differ. Run python3 scripts/sync_schema_representations.py --write.")
        return 1

    print("Schema representations are identical.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
