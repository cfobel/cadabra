# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from pathlib import Path

placeholder_stl = "solid placeholder\nendsolid placeholder\n"


def build_tray(job_id: str) -> None:
    out_dir = Path("/tmp/trays") / job_id
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "tray.stl").write_text(placeholder_stl)
