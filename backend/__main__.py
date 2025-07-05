# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import uvicorn

if __name__ == "__main__":
    uvicorn.run("backend.main:create_app", factory=True, host="0.0.0.0", port=8000)
