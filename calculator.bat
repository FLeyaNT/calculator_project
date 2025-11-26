@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Calculator

echo ================================
echo        Calculator App
echo ================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python не установлен или не добавлен в PATH
    echo.
    echo Установите Python 3.11+ по ссылке:
    echo https://www.python.org/downloads/
    echo.
    echo При установке выберите:
    echo [x] Add Python to PATH
    echo.
    pause
    exit /b 1
)

echo [INFO] Found Python:
python --version

echo.
echo [INFO] Checking dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo [ERROR] Ошибка при загрузке зависимостей!
    pause
    exit /b 1
)

echo.
echo [INFO] Запуск Calculator...
echo.

python -m src.main
