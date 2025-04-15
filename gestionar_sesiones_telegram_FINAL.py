import os
import shutil

CARPETA_COPIAS = "copias"

# Sesiones a duplicar
COPIAS = {
    "telegram_session_VIDEOS.session": [
        "telegram_session_VIDEOS_COPY.session",
        "telegram_session_EXTRA_1.session"
    ],
    "telegram_session_IMAGENES.session": [
        "telegram_session_IMAGENES_COPY.session",
        "telegram_session_EXTRA_2.session"
    ],
    "telegram_session_2.session": [
        "telegram_session_2_COPY.session",
        "telegram_session_BACKUP_2.session"
    ]
}

def duplicar_sesiones():
    os.makedirs(CARPETA_COPIAS, exist_ok=True)
    creadas = []

    for original, nuevos in COPIAS.items():
        if not os.path.exists(original):
            print(f"⚠️ No se encontró el archivo original: {original}")
            continue
        for nuevo in nuevos:
            destino = os.path.join(CARPETA_COPIAS, nuevo)
            try:
                shutil.copy(original, destino)
                creadas.append(destino)
                print(f"✅ Copiado: {destino}")
            except Exception as e:
                print(f"❌ Error al copiar {original} → {destino}: {e}")

    if not creadas:
        print("\n⚠️ No se creó ninguna sesión. Verificá que existan los archivos originales.")
    else:
        print("\n🎉 Sesiones duplicadas correctamente en carpeta 'copias':")
        for f in creadas:
            print(f"- {f}")

def restaurar_desde_copia():
    if not os.path.exists(CARPETA_COPIAS):
        print("❌ No existe la carpeta 'copias'. Primero hay que generar las copias.")
        return

    archivos = [f for f in os.listdir(CARPETA_COPIAS) if f.endswith('.session')]
    if not archivos:
        print("⚠️ No hay archivos .session en la carpeta 'copias'.")
        return

    print("\n📦 Sesiones disponibles para restaurar:")
    for idx, nombre in enumerate(archivos, 1):
        print(f"[{idx}] {nombre}")

    seleccion = input("\nIngresá el número del archivo que querés restaurar: ")
    if not seleccion.isdigit() or int(seleccion) < 1 or int(seleccion) > len(archivos):
        print("❌ Selección inválida.")
        return

    elegido = archivos[int(seleccion)-1]
    origen = os.path.join(CARPETA_COPIAS, elegido)
    destino = elegido

    try:
        shutil.copy(origen, destino)
        print(f"✅ Restaurado correctamente: {destino}")
    except Exception as e:
        print(f"❌ Error al restaurar {elegido}: {e}")

def listar_sesiones_disponibles():
    print("\n📂 Sesiones .session en la carpeta actual:")
    sesiones = [f for f in os.listdir() if f.endswith('.session')]
    if not sesiones:
        print("⚠️ No se encontraron archivos .session.")
    else:
        for s in sesiones:
            print(f"- {s}")

if __name__ == "__main__":
    print("""
🛠️ Herramienta de gestión de sesiones Telegram
1. Duplicar sesiones activas a carpeta 'copias'
2. Restaurar una sesión desde carpeta 'copias'
3. Ver sesiones actuales en esta carpeta
4. Salir
""")

    opcion = input("Elegí una opción (1-4): ")

    if opcion == "1":
        duplicar_sesiones()
    elif opcion == "2":
        restaurar_desde_copia()
    elif opcion == "3":
        listar_sesiones_disponibles()
    else:
        print("👋 Salida del programa")

    input("\nPresioná Enter para cerrar...")
