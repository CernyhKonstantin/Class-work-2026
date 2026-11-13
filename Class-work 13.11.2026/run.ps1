$ErrorActionPreference = "Stop"
Write-Host "=== Class-work 13.11.2026 ===" -ForegroundColor Cyan
py --version
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    py -m venv .venv
}
$python = ".\.venv\Scripts\python.exe"
Write-Host "Installing project requirements..." -ForegroundColor Yellow
& $python -m pip install --upgrade pip
& $python -m pip install -r requirements.txt
Write-Host "Applying database migrations..." -ForegroundColor Yellow
& $python manage.py migrate
Write-Host "Starting Django development server..." -ForegroundColor Green
& $python manage.py runserver
