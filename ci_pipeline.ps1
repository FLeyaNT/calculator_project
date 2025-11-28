Write-Host "=== Starting CI Pipeline ===" -ForegroundColor Green

try {
    Write-Host "1. Pulling latest changes..." -ForegroundColor Yellow
    git pull origin main
    
    Write-Host "2. Building project..." -ForegroundColor Yellow
    
    $pythonPath = Get-Command python -ErrorAction SilentlyContinue
    if (-not $pythonPath) {
        throw "Python not found in PATH"
    }
    
    if (-not (Test-Path "venv")) {
        python -m venv venv
    }
    
    .\venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install PyQt6
    pip install -r requirements.txt
    pip install pytest pytest-qt
    
    Write-Host "3. Running unit tests..." -ForegroundColor Yellow
    pytest
    
    if ($LASTEXITCODE -ne 0) {
        throw "Tests failed with exit code: $LASTEXITCODE"
    }
    
    Write-Host "All tests passed!" -ForegroundColor Green
    
    Write-Host "4. Creating installer..." -ForegroundColor Yellow
    
    $nsisPath = "C:\Program Files (x86)\NSIS\makensis.exe"
    $installer = $null
    
    if ($nsisPath) {
        makensis installer.nsi
        $installer = "CalculatorSetup.exe"
        Write-Host "Installer created: $installer" -ForegroundColor Green
    } else {
        Write-Warning "NSIS not found, skipping installer creation"
    }
    
    Write-Host "5. Installing application..." -ForegroundColor Yellow
    
    if ($installer -and (Test-Path $installer)) {
        Write-Host "Running installer silently..." -ForegroundColor Green
        Start-Process -Wait -FilePath $installer -ArgumentList "/S"
        Write-Host "Application installed successfully!" -ForegroundColor Green
    } else {
        Write-Host "Installer not found, manual installation required" -ForegroundColor Yellow
        Write-Host "You can run the application with: python src\main.py" -ForegroundColor Cyan
    }
    
    Write-Host "=== CI Pipeline Completed Successfully ===" -ForegroundColor Green
    
} catch {
    Write-Host "ERROR: $_" -ForegroundColor Red
    exit 1
}