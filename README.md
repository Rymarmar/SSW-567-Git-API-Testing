# SSW-567 Git API Testing

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Rymarmar/SSW-567-Git-API-Testing/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/Rymarmar/SSW-567-Git-API-Testing/tree/main)

**HW 03a files live here →** [`GitHubApi567-hw3a/`](GitHubApi567-hw3a/)

- App: `github_api.py`  
- Tests: `test_github_api.py`  
- Requirements: `requirements.txt`  
- HW 03a README (details + how to run) is inside that folder.

## HW 03b (Mocking) branch badge
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Rymarmar/SSW-567-Git-API-Testing/tree/HW03a_Mocking.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/Rymarmar/SSW-567-Git-API-Testing/tree/HW03a_Mocking)

## HW 03c — Static Analysis & Coverage (Triangles)

- Source: `GitHubApi567-hw3a/triangles.py`  
- Tests (pytest): `GitHubApi567-hw3a/test_triangles.py`  
- Static analysis: **Pylint**  
- Coverage: **Coverage.py** (HTML report)  
- **Final results:** Pylint **10.00/10**, Coverage **100%**

**Artifacts (before/after outputs & screenshots):**
- `docs/hw03c/pylint-before.txt` / `pylint-after.txt`
- `docs/hw03c/coverage-before.txt` / `coverage-after.txt`
- `docs/hw03c/*.png` (screenshots)

---

## Run Locally

```bash
python -m venv .venv
# Windows PowerShell:
. .venv/Scripts/Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -U pip
# If present:
pip install -r GitHubApi567-hw3a/requirements.txt || true
# Tools for HW03c:
pip install pylint coverage pytest

# Static analysis
pylint GitHubApi567-hw3a/triangles.py GitHubApi567-hw3a/test_triangles.py

# Coverage + tests
coverage erase
coverage run -m pytest -q GitHubApi567-hw3a
coverage report
coverage html   # opens htmlcov/index.html
