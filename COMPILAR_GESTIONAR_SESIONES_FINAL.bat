@echo off
chcp 65001 >nul
echo ================================
echo   COMPILANDO SESIONES TELEGRAM
echo ================================

set SCRIPT=gestionar_sesiones_telegram_FINAL.py

if not exist "%SCRIPT%" (
    echo ❌ No se encontró %SCRIPT%.
    pause
    exit /b
)

pyinstaller --noconfirm --onefile "%SCRIPT%"

if not exist "EXE" mkdir EXE
move /Y dist\gestionar_sesiones_telegram_FINAL.exe EXE\ >nul

rd /s /q build
rd /s /q dist
del /q *.spec

echo ✅ Compilación completada. EXE generado en carpeta EXE
pause
