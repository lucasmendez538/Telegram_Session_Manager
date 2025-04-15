import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
import subprocess

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Telegram Session & Script Manager")
        self.geometry("600x400")
        self.create_tabs()

    def create_tabs(self):
        tab_control = ttk.Notebook(self)

        self.tab_py_to_exe = ttk.Frame(tab_control)
        self.tab_bat_to_exe = ttk.Frame(tab_control)
        self.tab_session_manager = ttk.Frame(tab_control)

        tab_control.add(self.tab_py_to_exe, text='PY ➜ EXE')
        tab_control.add(self.tab_bat_to_exe, text='BAT ➜ EXE')
        tab_control.add(self.tab_session_manager, text='Gestión de Sesiones')

        tab_control.pack(expand=1, fill='both')

        self.build_py_to_exe_tab()
        self.build_bat_to_exe_tab()
        self.build_session_manager_tab()

    def build_py_to_exe_tab(self):
        label = tk.Label(self.tab_py_to_exe, text="Seleccioná un archivo .py para compilar")
        label.pack(pady=10)

        btn = tk.Button(self.tab_py_to_exe, text="Seleccionar .py", command=self.compile_py)
        btn.pack()

    def build_bat_to_exe_tab(self):
        label = tk.Label(self.tab_bat_to_exe, text="Seleccioná un archivo .bat para convertir")
        label.pack(pady=10)

        btn = tk.Button(self.tab_bat_to_exe, text="Seleccionar .bat", command=self.convert_bat)
        btn.pack()

    def build_session_manager_tab(self):
        label = tk.Label(self.tab_session_manager, text="Duplicar sesión desde archivo existente")
        label.pack(pady=10)

        btn = tk.Button(self.tab_session_manager, text="Duplicar sesión", command=self.duplicar_sesion)
        btn.pack(pady=5)

        label2 = tk.Label(self.tab_session_manager, text="Restaurar sesión desde copias")
        label2.pack(pady=10)

        btn2 = tk.Button(self.tab_session_manager, text="Restaurar sesión", command=self.restaurar_sesion)
        btn2.pack(pady=5)

    def compile_py(self):
        file = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if file:
            os.system(f"pyinstaller --noconfirm --onefile --windowed \"{file}\"")
            messagebox.showinfo("Compilado", "Script compilado y guardado en /dist")

    def convert_bat(self):
        file = filedialog.askopenfilename(filetypes=[("Batch files", "*.bat")])
        if file:
            converter = "Bat_To_Exe_Converter.exe"
            if not os.path.exists(converter):
                messagebox.showerror("Error", f"No se encontró {converter}")
                return
            subprocess.run([converter, file], check=False)

    def duplicar_sesion(self):
        origen = filedialog.askopenfilename(filetypes=[("Session", "*.session")])
        if origen:
            nombre = os.path.basename(origen)
            nuevo = f"copias/{nombre.replace('.session', '_COPIA.session')}"
            os.makedirs("copias", exist_ok=True)
            shutil.copy(origen, nuevo)
            messagebox.showinfo("Hecho", f"Sesión duplicada como: {nuevo}")

    def restaurar_sesion(self):
        carpeta = "copias"
        if not os.path.exists(carpeta):
            messagebox.showerror("Error", "No existe la carpeta copias")
            return
        file = filedialog.askopenfilename(initialdir=carpeta, filetypes=[("Session", "*.session")])
        if file:
            nombre = os.path.basename(file)
            shutil.copy(file, nombre)
            messagebox.showinfo("Hecho", f"Sesión restaurada como: {nombre}")

if __name__ == '__main__':
    app = App()
    app.mainloop()
