$ErrorActionPreference = "Stop"
if (-not (Test-Path ".venv")) { py -m venv .venv }
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw "Dependency installation failed." }
& ".\.venv\Scripts\python.exe" manage.py migrate
if ($LASTEXITCODE -ne 0) { throw "Database migration failed." }
& ".\.venv\Scripts\python.exe" manage.py runserver
