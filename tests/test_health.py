# SPDX-License-Identifier: Apache-2.0
from fastapi.testclient import TestClient

from backend.main import create_app


def test_health() -> None:
    client = TestClient(create_app())
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

