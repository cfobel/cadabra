# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, BackgroundTasks

from ..models.trays import TrayDownload, TrayRequest, TrayStatus
from ..services.trays import build_tray

router = APIRouter(prefix="/trays", tags=["trays"])


@router.post("/", response_model=TrayStatus)
def start_tray(request: TrayRequest, background_tasks: BackgroundTasks) -> TrayStatus:
    job_id = str(uuid4())
    background_tasks.add_task(build_tray, job_id)
    return TrayStatus(job_id=job_id, status="queued")


@router.get("/{job_id}", response_model=TrayStatus)
def check_tray(job_id: str) -> TrayStatus:
    path = Path("/tmp/trays") / job_id / "tray.stl"
    if path.exists():
        status = "complete"
    else:
        status = "queued"
    return TrayStatus(job_id=job_id, status=status)


@router.get("/{job_id}/download", response_model=TrayDownload)
def download_tray(job_id: str) -> TrayDownload:
    return TrayDownload(job_id=job_id, download_url=f"/tmp/trays/{job_id}/tray.stl")
