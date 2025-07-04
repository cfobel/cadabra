#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
import sys
from pathlib import Path

MISSING = []
for fname in sys.argv[1:]:
    path = Path(fname)
    if path.name == "LICENSE":
        continue
    if (
        path.suffix == ".json"
        or path.suffix == ".yaml"
        and path.name.endswith("-lock.yaml")
    ):
        continue
    text = path.read_text(errors="ignore")
    lines = text.splitlines()[:5]
    if not any("SPDX-License-Identifier: Apache-2.0" in ln for ln in lines):
        MISSING.append(fname)

if MISSING:
    print("Missing SPDX header in:")
    for f in MISSING:
        print(f"  {f}")
    sys.exit(1)
