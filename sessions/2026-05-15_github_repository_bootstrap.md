# 2026-05-15 — GitHub repository bootstrap

## Purpose

Put ACP Quantum under its own GitHub repository while keeping local runtime
state out of version control.

## Actions

- Initialized the project root as a git repository on `main`.
- Added `.gitignore` for `.venv/`, `.DS_Store`, Python caches, Matplotlib font
  caches, scratch files, and local Cowork `metadata.json`.
- Audited for large files over 50 MB; none were included after ignoring
  `.venv/`.
- Ran a lightweight secret-pattern scan; hits were ordinary prose terms rather
  than credentials.
- Committed the initial ACP Quantum snapshot.
- Created private GitHub repository `andrewmureddu/acp-quantum`.
- Pushed `main` to `origin`.

## Notes

- Repository URL: `https://github.com/andrewmureddu/acp-quantum`
- Visibility: private.
- Open problems unchanged.
