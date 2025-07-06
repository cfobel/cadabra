# Active Context (06 Jul 2025)

* **Focus** – Backend skeleton complete; start Docker and frontend scaffolding.
* **Immediate next steps** (see [`techContext.md`](./techContext.md) for stack details)

  1. Create multi-stage Dockerfile using `mambaorg/pixi` base.
  2. Add docker-compose for local dev.
  3. Scaffold React frontend with Vite + TypeScript.
  4. Extend GitHub Actions to build and push Docker images.

* **Decisions** (see [`systemPatterns.md`](./systemPatterns.md) for full rationale)

  * **Async CAD jobs**: Use FastAPI's `BackgroundTasks` for the MVP.
  * **User project persistence**: Ephemeral file storage for now; S3-compatible later.

> **Note**: The Memory Bank is essential for tracking active decisions and immediate next steps.
