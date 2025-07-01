# Product Context

## Why it exists
Enthusiasts who own 3-D printers or CNC cutters often need **bespoke trays, inlays
or organisers** that match the silhouette of real-world objects. Traditional CAD
packages (Fusion 360, SolidWorks) demand expertise and paid licences, while AI tools
usually return *uneditable meshes*. Our application, **cadabra**, bridges that gap by generating
**parametric CAD** (see [`projectbrief.md`](./projectbrief.md)) that users (or AI agents) can re-edit later.

## Problems solved
1. **Ease-of-use** – Drag-and-drop photo → tweak a few sliders → download model.
2. **Editability** – Output is STEP/STL generated from a [`CadQuery` script](./techContext.md), not a frozen
   mesh.
3. **Repeatability** – Users can store profiles & fiducials and regenerate trays for
   different depths / materials.
4. **Shareability** – Open licence encourages remixing; trays can be shared or sold
   without restriction.

## UX Goals
* < 60 s from photo upload to downloadable model.
* No local installation; works on desktop & mobile.
* Live preview updating within 250 ms of parameter change.
* Clear “expert-mode” toggle exposing raw CadQuery script (see [`techContext.md`](./techContext.md)) for power users.

> **Note**: The Memory Bank is vital for documenting the product's purpose, problems solved, and UX goals.
