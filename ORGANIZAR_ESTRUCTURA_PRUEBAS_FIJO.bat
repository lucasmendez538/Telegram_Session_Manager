@echo off
chcp 65001 >nul
echo =======================================
echo   ORDENANDO CARPETA "Pruebas"
echo =======================================

REM Crear carpetas si no existen
if not exist "OLD" mkdir "OLD"
if not exist "EXE" mkdir "EXE"
if not exist "BAT" mkdir "BAT"
if not exist "PY" mkdir "PY"
if not exist "copias" mkdir "copias"

REM Mover scripts y archivos antiguos a OLD
if exist "check_sesiones_telegram.py" move /Y "check_sesiones_telegram.py" "OLD\"
if exist "script.py" move /Y "script.py" "OLD\"
if exist "script2.py" move /Y "script2.py" "OLD\"
if exist "COMPILAR_GESTIONAR_SESIONES.bat" move /Y "COMPILAR_GESTIONAR_SESIONES.bat" "OLD\"
if exist "telegram_session.session" move /Y "telegram_session.session" "OLD\"

REM Limpiar residuos de compilación
if exist "build" rd /s /q "build"
if exist "dist" rd /s /q "dist"
del /q *.spec >nul 2>nul

echo ✅ Carpetas y archivos organizados.
echo ---------------------------------------
echo 🧩 Estructura recomendada:
echo - EXE\
echo - BAT\
echo - PY\
echo - copias\
echo - OLD\
echo ---------------------------------------
pause
