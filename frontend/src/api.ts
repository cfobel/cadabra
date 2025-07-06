// SPDX-License-Identifier: Apache-2.0
import axios from "axios";

export interface TrayRequest {
  depth: number;
  offset: number;
}

export interface TrayStatus {
  job_id: string;
  status: string;
}

export interface TrayDownload {
  job_id: string;
  download_url: string;
}

const client = axios.create({ baseURL: "http://localhost:8000" });

export async function health(): Promise<{ status: string }> {
  const { data } = await client.get("/health");
  return data;
}

export async function startTray(req: TrayRequest): Promise<TrayStatus> {
  const { data } = await client.post("/trays/", req);
  return data;
}

export async function checkTray(jobId: string): Promise<TrayStatus> {
  const { data } = await client.get(`/trays/${jobId}`);
  return data;
}

export async function downloadTray(jobId: string): Promise<TrayDownload> {
  const { data } = await client.get(`/trays/${jobId}/download`);
  return data;
}
