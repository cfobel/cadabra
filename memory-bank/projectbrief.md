# Project Brief — “cadabra”

We are building a **web-first application** that lets a hobbyist photograph an object,
manually (and in future, AI-assisted) trace its top-down contour, tweak a handful of
parametric tray settings, and instantly receive an STL or STEP *“shell”* model suitable
for 3-D printing or CNC foam cutting.

Key requirements (May → Jul 2025 synthesis)

* **Open & Permissive** – Apache-2.0 licence.
* **Server-side modelling** – [FastAPI service running CadQuery/OCCT](./techContext.md); browser stays
  lightweight.
* **Modern tool-chain** –
  *Python 3.12* managed with **Pixi** (`pixi init --format pyproject`) and
  *Node 18 LTS* + **pnpm** for a TypeScript/React front-end.
* **User-defined fiducials** – Users can import/export custom reference
  markers to aid alignment.
* **Multi-stage Docker** – Use the official [Pixi base image](./techContext.md) to freeze Python
  deps; copy artefacts into a slim runtime stage.
* **Future-proof** – The silhouette tracing step is deliberately modular so an
  AI/VLM helper can replace manual tracing later.

> **Note**: The Memory Bank serves as the foundation for maintaining clarity on project scope and requirements.
