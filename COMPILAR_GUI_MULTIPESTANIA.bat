@echo off
chcp 65001 >nul
echo ================================
echo   COMPILANDO GUI MULTIPESTAÑA
echo ================================

set SCRIPT=gui_multipestania.py

if not exist "%SCRIPT%" (
    echo ❌ No se encontró el archivo %SCRIPT%.
    pause
    exit /b
)

pyinstaller --noconfirm --onefile --windowed "%SCRIPT%"

if not exist "EXE" mkdir EXE
move /Y dist\gui_multipestania.exe EXE\ >nul

rd /s /q build
rd /s /q dist
del /q *.spec

echo ✅ Compilación finalizada. EXE generado en carpeta EXE
pause
