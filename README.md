# Telegram_Session_Manager
🔁 Herramienta para automatizar la gestión de sesiones de Telegram y la conversión de scripts .py y .bat a .exe.

# 🔁 Transformación de Datos y Gestión de Sesiones Telegram

Este repositorio contiene una suite de herramientas para automatizar y transformar scripts `.py` y `.bat`, además de gestionar sesiones de Telegram con control, duplicación y restauración segura.

## ✨ Funcionalidades principales

### 1. 🔧 Transformador de Scripts (GUI)
- `.py` ➜ `.exe`
- `.py` ➜ `.bat`
- `.bat` ➜ `.exe` (requiere Bat_To_Exe_Converter.exe)
- `.bat` ➜ `.py`
- Interfaz visual intuitiva y compilable.

### 2. 🔐 Gestor de sesiones Telegram
- Duplica `.session` activos a carpeta `copias/`.
- Restaura sesiones desde backup.
- Lista sesiones disponibles.
- Preparado para escalar con token de seguridad en próximas versiones.

### 3. 📁 Organización automática
- Script `.bat` para dejar tu carpeta ordenada:
  - `EXE/`, `BAT/`, `PY/`, `copias/`, `OLD/`

## 📦 Instalación
Requiere Python 3.11+ y `pyinstaller`.

```bash
pip install pyinstaller

pyinstaller --noconfirm --onefile --windowed transformador_gui_final.py
pyinstaller --noconfirm --onefile gestionar_sesiones_telegram_FINAL.py
