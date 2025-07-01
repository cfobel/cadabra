# Tech Context

This document details the technology choices that fulfill the requirements in the [`projectbrief.md`](./projectbrief.md).
See [`systemPatterns.md`](./systemPatterns.md) for the rationale behind these decisions.

| Area                  | Choice / Version                  | Notes |
| --------------------- | --------------------------------- | ----- |
| **Frontend**          | React 18 + TypeScript, Vite build | Managed by **pnpm** |
| **Backend API**       | FastAPI 0.111 (Python 3.12)       | JSON over HTTPS |
| **CAD Engine**        | CadQuery 2 + OCCT 7.7             | Runs in backend worker |
| **Dependency Mgmt**   | **Pixi** for Python, **pnpm** for Node | Pixi lockfile for reproducibility |
| **Containerisation**  | Multi-stage Docker; Pixi base     | Final image < 200 MB |
| **CI/CD**             | GitHub Actions                    | Lint, test, build, push image |
| **Auth**              | Anonymous for MVP; JWT planned    | |
| **Storage**           | In-memory + temp dir for MVP; S3-compatible later | |
| **Licence**           | Apache-2.0                        | SPDX headers required |

> **Note**: The Memory Bank is critical for project continuity and must be updated regularly to reflect changes in the tech stack and decisions.
