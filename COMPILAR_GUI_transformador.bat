@echo off
chcp 65001 >nul
echo ===============================
echo   COMPILANDO TRANSFORMADOR GUI
echo ===============================

REM Nombre del archivo principal
set SCRIPT=transformador_gui_final.py

REM Verificar si el script existe
if not exist "%SCRIPT%" (
    echo ❌ No se encontró %SCRIPT%.
    pause
    exit /b
)

REM Compilar con PyInstaller
pyinstaller --noconfirm --onefile --windowed "%SCRIPT%"

REM Mover el resultado a carpeta EXE
if not exist "EXE" mkdir EXE
move /Y dist\transformador_gui_final.exe EXE\ >nul

REM Limpiar residuos
rd /s /q build
rd /s /q dist
del /q *.spec

echo ✅ Compilación completada. EXE generado en carpeta EXE
pause
