// gta6-meme-x-01 v6 — Leonida DMV Driver's License Renewal
// Entrypoint: reads POST.json from the repo root and writes it to
// MAKEFUN_OUTPUT_DIR (never inside the repo — the grader mounts /bot read-only).
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const root = new URL(".", import.meta.url).pathname;
const outDir = process.env.MAKEFUN_OUTPUT_DIR || join(root, "output");
mkdirSync(outDir, { recursive: true });

const post = readFileSync(join(root, "POST.json"), "utf-8");
writeFileSync(join(outDir, "POST.json"), post);

// Read-back self-check: the written POST.json must round-trip byte-identical.
const written = readFileSync(join(outDir, "POST.json"), "utf-8");
if (written !== post) {
  throw new Error("POST.json round-trip mismatch: written bytes differ from source");
}
const parsed = JSON.parse(written);
if (typeof parsed.text !== "string" || !parsed.text.includes("Lucia Caminos")) {
  throw new Error("POST.json self-check failed: post text missing or malformed");
}
console.log("wrote POST.json to", outDir, "- self-check OK (byte-identical round-trip)");
