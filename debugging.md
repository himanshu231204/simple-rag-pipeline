# Debugging Log

This file tracks debugging issues, fixes, and current status for this project.
We will keep appending updates here.

## 2026-03-23

### 1) Git ignore update for vector store artifacts
- Issue: FAISS store files should not be tracked by git.
- Action taken:
  - Added ignore entries in .gitignore:
    - faiss_store/
    - fassi_store/
- Status: Resolved for new/untracked files.

### 2) Running src.search in virtual environment
- Issue: Direct run failed with import error.
- Error: ModuleNotFoundError: No module named 'src'
- Action taken:
  - Used module execution instead of direct file execution.
  - Working command:
    - .\\ragenv\\Scripts\\python.exe -m src.search
- Status: Resolved.

### 3) PDF parsing failure during vector store build
- File involved:
  - data/Artificial Intelligence - A Modern Approach (3rd Edition).pdf
- Issue: PDF parser error from pypdf on one PDF.
- Action taken in src/data_loader.py:
  - Added robust PDF loader strategy:
    - Primary: PyMuPDFLoader
    - Fallback: PyPDFLoader
    - If both fail: skip file and continue
- Status: PDF loading path improved and no longer blocked at initial parse stage.

### 4) Current runtime bottleneck
- Issue: Long embedding run interrupted during chunk embedding.
- Observed state:
  - Documents loaded successfully.
  - Large chunk volume causes long processing time.
- Status: Open (performance/timeout/interrupt related), not a code-crash at PDF load step.

## Next updates
- Add each new issue in this format:
  - Issue
  - Root cause
  - Action taken
  - Final status
