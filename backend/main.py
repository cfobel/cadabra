# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI

from .cadabra.api import trays


def load_description() -> str:
    root = Path(__file__).resolve().parents[1]
    path = root / "memory-bank" / "projectbrief.md"
    return path.read_text()


def create_app() -> FastAPI:
    description = load_description()
    tags_metadata = [
        {"name": "health", "description": "Service status check"},
        {
            "name": "trays",
            "description": "Generate custom trays from object silhouettes",
        },
    ]
    app = FastAPI(
        title="cadabra API",
        description=description,
        openapi_tags=tags_metadata,
    )

    @app.get("/health", tags=["health"])
    def health() -> dict[str, str]:
        return {"status": "ok"}

    app.include_router(trays.router)
    return app
