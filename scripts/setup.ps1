# PowerShell setup script for Windows
Write-Host "Setting up AI Pair Programming Tool..." -ForegroundColor Green

# Check if Python is installed
try {
    $pythonVersion = python --version
    Write-Host "Found Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Python not found! Please install Python first." -ForegroundColor Red
    exit 1
}

# Create virtual environment if it doesn't exist
if (-Not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
} else {
    Write-Host "Virtual environment already exists." -ForegroundColor Green
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install dependencies
Write-Host "Installing Jac language..." -ForegroundColor Yellow
pip install jaclang

Write-Host "Installing other dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "To run the tool:" -ForegroundColor Cyan
Write-Host "1. Activate the environment: .\venv\Scripts\Activate.ps1" -ForegroundColor Cyan
Write-Host "2. Run the tool: jac run ai_pair_programmer.jac" -ForegroundColor Cyan
