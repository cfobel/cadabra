// SPDX-License-Identifier: Apache-2.0
import React, { useState } from "react";
import { startTray, checkTray, downloadTray } from "./api";

function App() {
  const [depth, setDepth] = useState(0);
  const [offset, setOffset] = useState(0);
  const [file, setFile] = useState<File | null>(null);
  const [job, setJob] = useState<string | null>(null);
  const [downloadUrl, setDownloadUrl] = useState<string | null>(null);
  const [status, setStatus] = useState<string>("idle");

  const handleFile = (f: File) => {
    setFile(f);
  };

  const submit = async () => {
    const res = await startTray({ depth, offset });
    setJob(res.job_id);
    setStatus(res.status);
    const id = res.job_id;
    const interval = setInterval(async () => {
      const st = await checkTray(id);
      setStatus(st.status);
      if (st.status === "complete") {
        clearInterval(interval);
        const dl = await downloadTray(id);
        setDownloadUrl(dl.download_url);
      }
    }, 1000);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>Hello cadabra</h1>
      <div
        onDragOver={(e) => e.preventDefault()}
        onDrop={(e) => {
          e.preventDefault();
          if (e.dataTransfer.files[0]) handleFile(e.dataTransfer.files[0]);
        }}
        style={{
          border: "1px dashed #ccc",
          padding: "1rem",
          marginBottom: "1rem",
        }}
      >
        {file ? file.name : "Drop photo here"}
      </div>
      <label>
        Depth: {depth}
        <input
          type="range"
          min="0"
          max="10"
          step="0.1"
          value={depth}
          onChange={(e) => setDepth(parseFloat(e.target.value))}
        />
      </label>
      <br />
      <label>
        Offset: {offset}
        <input
          type="range"
          min="0"
          max="10"
          step="0.1"
          value={offset}
          onChange={(e) => setOffset(parseFloat(e.target.value))}
        />
      </label>
      <br />
      <button onClick={submit} disabled={!file}>
        Build Tray
      </button>
      <p>Status: {status}</p>
      {downloadUrl && (
        <p>
          <a href={downloadUrl} download>
            Download Tray
          </a>
        </p>
      )}
    </div>
  );
}

export default App;
