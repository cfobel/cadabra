# Active Context (01 Jul 2025)

* **Focus** – Kick-off: initialise Memory Bank; agree on slug; scaffold repo.
* **Immediate next steps** (see [`techContext.md`](./techContext.md) for stack details)

  1. Pick and register project slug (`cadabra`).
  2. `pixi init --format pyproject` → add FastAPI, CadQuery, pytest.
  3. `pnpm init` → add React, Vite, TypeScript, ESLint, Prettier.
  4. Create multi-stage Dockerfile using `mambaorg/pixi` base.
  5. Set up GitHub Actions (lint, test, docker-build, licence check).

* **Decisions** (see [`systemPatterns.md`](./systemPatterns.md) for full rationale)

  * **Async CAD jobs**: Use FastAPI's `BackgroundTasks` for the MVP.
  * **User project persistence**: Ephemeral file storage for now; S3-compatible later.

> **Note**: The Memory Bank is essential for tracking active decisions and immediate next steps.
