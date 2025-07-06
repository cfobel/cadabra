# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from pydantic import BaseModel


class TrayRequest(BaseModel):
    depth: float = 0.0
    offset: float = 0.0


class TrayStatus(BaseModel):
    job_id: str
    status: str


class TrayDownload(BaseModel):
    job_id: str
    download_url: str
