<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- docs/ROADMAP.md -->
# Cadabra • Implementation Roadmap

Below is a **phase-by-phase implementation plan** that lines up with the current repo layout (Memory Bank + bootstrap script).
Each phase ends in a demo-able increment; every sub-task is scoped so a junior engineer can finish it in *≤ 2 days* and raise a PR that passes CI.

---

## Phase 0 • Repo bootstrap & working agreements (½ sprint)

| ID  | Deliverable                                       | Sub-tasks                                                                                                                                                     |
| --- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0-1 | **Clean repo structure**                          | ① Delete any stray files; keep only `/memory-bank`, root docs, `.gitignore`<br>② Create empty `backend/`, `frontend/`, `.github/workflows/`, `infra/` folders |
| 0-2 | **Project slug & licence committed**              | ① Rename project to **cadabra** everywhere (`projectbrief.md`, README)<br>② Add `LICENSE` (Apache-2.0) with SPDX header check pre-commit                      |
| 0-3 | **Dev-env one-command setup**                     | ① `pixi init --format pyproject` → add FastAPI, CadQuery, pytest<br>② `pnpm init --yes` in `frontend/`<br>③ Create `bootstrap.sh` that runs *both* commands   |
| 0-4 | **Pre-commit & code-style**                       | ① Add Black, Ruff, Isort configs<br>② Add ESLint + Prettier configs<br>③ `pre-commit` config calling all linters                                              |
| 0-5 | **Conventional Commits guide in CONTRIBUTING.md** | Lift guidance from `AGENTS.md` templates into a quick-start section                                                                                           |

---

## Phase 1 • Backend skeleton (1 sprint)

| ID  | Deliverable                     | Sub-tasks                                                                                                          |
| --- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1-1 | **FastAPI app booting locally** | ① `backend/main.py` with `create_app()` and `/health` route<br>② Uvicorn entry-point<br>③ PyTest health-check test |
| 1-2 | **Domain package layout**       | Create `backend/cadabra/` with `api/`, `services/`, `models/` packages                                             |
| 1-3 | **Background task stub**        | Implement FastAPI `BackgroundTasks` handler for “build\_tray” that just writes a placeholder STL file              |
| 1-4 | **Pydantic DTOs**               | Define `TrayRequest`, `TrayStatus`, `TrayDownload` schemas                                                         |
| 1-5 | **OpenAPI docs auto-generated** | Enable tags, description from Memory Bank text                                                                     |

---

## Phase 2 • Frontend skeleton (1 sprint)

| ID  | Deliverable                                    | Sub-tasks                                                    |
| --- | ---------------------------------------------- | ------------------------------------------------------------ |
| 2-1 | **Vite + React app boots**                     | Scaffold with TypeScript strict mode; “Hello cadabra” screen |
| 2-2 | **API client wrapper**                         | Axios wrapper with typed responses for `/health`, `/trays`   |
| 2-3 | **Upload & param form**                        | Drag-and-drop photo, sliders for depth/offset (UI only)      |
| 2-4 | **Build tray flow hooked**                     | POST to backend, poll `/status`, download link appears       |
| 2-5 | **ESLint/Prettier wired into pre-commit & CI** |                                                              |

---

## Phase 3 • DevOps foundations (1 sprint)

| ID  | Deliverable                      | Sub-tasks                                                                                             |
| --- | -------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 3-1 | **Multi-stage Dockerfile**       | Stage 1: `mambaorg/pixi` build env → Stage 2: slim runtime ʻpython:3.12-slimʼ with compiled OCCT libs |
| 3-2 | **Docker-compose for local dev** | `backend`, `frontend` (served by Vite), reverse-proxy nginx for SSE                                   |
| 3-3 | **GitHub Actions CI**            | Workflow: lint → test → build containers → licence scan                                               |
| 3-4 | **Artefact registry push**       | Push images to GitHub Container Registry (ghcr.io) with version tags                                  |

---

## Phase 4 • MVP silhouette → model pipeline (2 sprints)

| ID  | Deliverable                   | Sub-tasks                                                                   |
| --- | ----------------------------- | --------------------------------------------------------------------------- |
| 4-1 | **2-D contour storage**       | Accept SVG or JSON polyline from UI; validate & persist in `/tmp/jobs/{id}` |
| 4-2 | **CadQuery script generator** | Generate parametric script from contour + settings                          |
| 4-3 | **Worker builds STL/STEP**    | Run CadQuery headless; save artefacts; record success/fail                  |
| 4-4 | **Status endpoint**           | Expose `queued / running / failed / complete` with percent dummy            |
| 4-5 | **Frontend contour editor**   | Integrate `react-svg-pan-zoom` (or similar) for manual trace                |
| 4-6 | **Download UX**               | Signed URL (local FS now, S3 later); browser saves file                     |

---

## Phase 5 • Live preview & advanced UX (1 sprint)

| ID  | Deliverable                    | Sub-tasks                                               |
| --- | ------------------------------ | ------------------------------------------------------- |
| 5-1 | **Quick-render PNG endpoint**  | Run low-res CadQuery render (<0.5 s) in background task |
| 5-2 | **Server-Sent Events channel** | Push job progress & previews                            |
| 5-3 | **Frontend live canvas**       | Show preview, throttle updates, animate depth slider    |
| 5-4 | **Error display & retry**      | Bubble worker exceptions to UI with friendly messages   |

---

## Phase 6 • Persistence & cloud storage (1 sprint)

| ID  | Deliverable              | Sub-tasks                                                       |
| --- | ------------------------ | --------------------------------------------------------------- |
| 6-1 | **S3 adapter**           | Abstract storage interface → impl `LocalFSStorage`, `S3Storage` |
| 6-2 | **Signed download URLs** | Presign for 10 min; fall back to proxy endpoint if local        |
| 6-3 | **Terraform sample**     | Module that provisions bucket + IAM for staging env             |

---

## Phase 7 • Auth & user projects (1 sprint)

| ID  | Deliverable                           | Sub-tasks                                    |
| --- | ------------------------------------- | -------------------------------------------- |
| 7-1 | **JWT login (Auth0 stub)**            | Middleware in FastAPI; React login flow      |
| 7-2 | **Project table (SQLite → Postgres)** | CRUD endpoints for trays scoped to `user_id` |
| 7-3 | **My Projects page**                  | List, filter, delete, regenerate             |

---

## Phase 8 • Scalable async queue (1 sprint, optional)

| ID  | Deliverable                  | Sub-tasks                                               |
| --- | ---------------------------- | ------------------------------------------------------- |
| 8-1 | **Switch to Celery + Redis** | Replace BackgroundTasks adapter; auto-scale worker pods |
| 8-2 | **Retry & timeout policy**   | Exponential back-off; alert on repeated failure         |
| 8-3 | **Tracing & metrics**        | Prometheus exporter, Grafana dashboard                  |

---

## Phase 9 • Testing & QA hardening (ongoing, dedicate 20 % bandwidth)

| ID  | Deliverable                           | Sub-tasks                                        |
| --- | ------------------------------------- | ------------------------------------------------ |
| 9-1 | **Backend unit tests (>80 % cov)**    | Model generator, error paths                     |
| 9-2 | **Frontend component tests (Vitest)** | Form validation, state management                |
| 9-3 | **Playwright e2e suite**              | Upload-to-download happy path in headless Chrome |
| 9-4 | **Load test script (Locust)**         | Benchmark 100 concurrent tray builds             |

---

## Phase 10 • Docs, onboarding & first public release (½ sprint)

| ID   | Deliverable                       | Sub-tasks                                                                        |
| ---- | --------------------------------- | -------------------------------------------------------------------------------- |
| 10-1 | **README complete**               | Quick-start, architecture diagram, screenshots                                   |
| 10-2 | **Memory Bank updated**           | `activeContext.md` summarises current focus; `progress.md` statuses flipped to ✅ |
| 10-3 | **Contributor guide**             | End-to-end “fix a typo” walk-through, Conventional Commit cheat-sheet            |
| 10-4 | **Version v0.1 tag & GH release** | Attach built images & changelog                                                  |

---

## Phase 1 → Phase 10 (overview)

| Phase | Theme                  | Outcome                                            |
| ----- | ---------------------- | -------------------------------------------------- |
| 1     | **Backend skeleton**   | FastAPI app boots locally, health-check passes     |
| 2     | **Frontend skeleton**  | Vite + React app talks to API                      |
| 3     | **DevOps foundations** | Multi-stage Dockerfile, compose stack, CI pipeline |
| 4     | **MVP model pipeline** | Contour → CadQuery → STL/STEP                      |
| 5     | **Live preview**       | Quick PNG previews over SSE                        |
| 6     | **Cloud storage**      | Pluggable S3 adapter + Terraform sample            |
| 7     | **Auth & projects**    | JWT login, user-scoped CRUD                        |
| 8     | **Async queue**        | Celery + Redis workers, retries                    |
| 9     | **Testing & QA**       | > 80 % backend coverage, Playwright E2E            |
| 10    | **Docs & release**     | v0.1 tag, screenshots, onboarding docs             |

See the full, task-level table above for exact ticket breakdown.

---

## How to use this roadmap

1. Create GitHub issues for every sub-task (or group of sub-tasks as requested); label with phase (`P4`) and area (`backend`, `frontend`, `devops`, `docs`).
2. Assign one issue per junior; pair-program on unfamiliar tech.
3. **Definition of Done** = code + tests + docs + green CI.
4. Update `memory-bank/progress.md` and any other memory bank docs as needed at the end of each phase.
