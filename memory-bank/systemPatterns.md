# System Patterns

> How the pieces fit together, why we chose them, and how they talk to each other.

This document outlines the system architecture for the application described in the [`projectbrief.md`](./projectbrief.md).

---

## 1 · System Architecture (C4)

### C4 Level 1 – System Context

```mermaid
flowchart TB
    subgraph External
        DIY["**DIY Maker**<br>Captures object silhouette and tweaks parameters<br>[Human actor]"]
        Printer["**3-D Printer / CNC**<br>Consumes STL/STEP models to manufacture parts<br>[Hardware]"]
    end

    App["**cadabra**<br>Web service turning photos into parametric 3-D trays<br>[React · FastAPI · CadQuery]"]

    DIY -->|"Uses via web browser<br>[HTTPS]"| App
    App -->|"Returns STL/STEP download<br>[HTTPS]"| DIY
    App -->|"Sends exported models<br>[STL / STEP]"| Printer
```

### C4 Level 2 – Container Diagram

```mermaid
flowchart TB
    subgraph Browser
        FE["**Web Frontend**<br>Single-page React application served statically<br>[React · TypeScript · Vite]"]
    end

    subgraph Cloud["**cadabra** Deployment"]
        API["**API Gateway + FastAPI**<br>Handles HTTP requests, validation, auth, queues jobs<br>[FastAPI · Uvicorn]"]
        Worker["**CAD Worker**<br>Runs CadQuery/OCCT to build parametric models<br>[Python · CadQuery · OCCT]"]
        Store["**Temp Storage**<br>Stores uploaded images & generated files<br>[Filesystem → S3 later]"]
    end

    FE -->|"Submits create-tray request<br>[JSON POST]"| API
    API -->|"Enqueues modelling task<br>[Async queue]"| Worker
    Worker -->|"Writes STL/STEP to<br>temp storage<br>[File I/O]"| Store
    API -->|"Streams file back to user<br>[HTTPS download]"| FE
    FE -->|"Shows live status SSE<br>[Server-Sent Events]"| API
```

> **Notation**
> *Nodes*: `**Bold title**<br>tweet-length description<br>[tech footer]`
> *Edges*: `Action description<br>[tech footer]`

---

## 2 · Key Technical Decisions

| Area                 | Decision                                                           | Rationale                                                        |
| -------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **Server-side CAD**  | CadQuery 2 + OCCT in a worker container                            | Keeps browser light; leverages parametric solids.                |
| **Job Dispatch**     | FastAPI background task for MVP; pluggable queue later (Celery/RQ) | Simplicity first, upgrade path ready.                            |
| **File Storage**     | Ephemeral disk → S3-compatible bucket                              | Works locally, scales to cloud.                                  |
| **Dependency Mgmt**  | `pixi` for Python, `pnpm` for Node                                 | Reproducible, fast, lock-file-based workflows.                   |
| **Containerisation** | Multi-stage Docker using `mambaorg/pixi` base                      | Tiny runtime image (< 200 MB) while retaining compiled CAD libs. |
| **Auth**             | Anonymous download for MVP, signed URLs; JWT planned               | Remove barriers to first-use, phased security.                   |

---

## 3 · Design Patterns in Use

* **Client-Server + Async Worker** – keeps UI snappy while heavy CAD runs off-thread.
* **CQRS-lite** – read path (download) separated from write path (create job).
* **Pipes & Filters** – photo → contour → model pipeline; each filter is replaceable.
* **Hexagonal / Ports-and-Adapters** – storage and queue are accessed through adapters, easing future vendor swaps.
* **Twelve-Factor Config** – all secrets & tuning via env-vars; zero hard-coded paths.

---

## 4 · Component Relationships (logical view)

```mermaid
flowchart LR
    subgraph Frontend
        FE_UI["**Silhouette UI**<br>Photo upload, contour editor, live preview<br>[React]"]
    end
    subgraph Backend
        API["**FastAPI Edge**<br>Validation, auth, REST+SSE<br>[FastAPI]"]
        Service["**Tray Service**<br>Owns domain logic & job orchestration<br>[Python]"]
        Modeler["**CadQuery Modeler**<br>Builds parametric solids<br>[CadQuery]"]
        Storage["**Artifact Store**<br>Images, STL, STEP<br>[S3 / FS]"]
    end

    FE_UI -->|"REST calls"| API
    API -->|"Dispatch job"| Service
    Service -->|"Invoke"| Modeler
    Modeler -->|"Write files"| Storage
    API -->|"Signed URLs"| FE_UI
```

---

## 5 · Core Sequence Diagrams

### 5.1 Generate Tray Workflow

```mermaid
sequenceDiagram
    participant U as DIY Maker (Browser)
    participant FE as Web Frontend
    participant API as FastAPI Gateway
    participant W as CAD Worker
    participant S as Temp Storage

    U->>FE: Upload photo + parameters
    FE->>API: POST /trays
    API-->>U: 202 Accepted + job ID
    API->>W: Dispatch "build tray" job
    W->>S: Write STL/STEP file
    W-->>API: Job complete + file path
    API->>FE: SSE: job status = completed
    FE->>API: GET /trays/{id}/download
    API->>S: Read file
    API-->>FE: Stream STL/STEP
    FE-->>U: Browser saves model
```

### 5.2 Live Preview Parameter Tweak

```mermaid
sequenceDiagram
    participant U as DIY Maker
    participant FE as Frontend
    participant API as FastAPI
    participant W as CAD Worker

    U->>FE: Drag depth slider
    FE->>API: POST /trays/{id}/preview
    API->>W: Background quick-model request
    W-->>API: 2-D PNG preview
    API-->>FE: 200 OK + PNG
    FE-->>U: Canvas refresh
```
