import tkinter as tk
from tkinter import messagebox, filedialog
import os
import subprocess

# === FUNCIONES INTERNAS ===

def transformar_py_a_exe():
    archivo = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if not archivo:
        return
    os.makedirs("EXE", exist_ok=True)
    nombre = os.path.basename(archivo)
    os.system(f"pyinstaller --noconfirm --onefile --noconsole \"{archivo}\" >nul")
    exe_name = nombre.replace(".py", ".exe")
    if os.path.exists(f"dist/{exe_name}"):
        os.replace(f"dist/{exe_name}", f"EXE/{exe_name}")
    for carpeta in ["build", "dist"]:
        if os.path.exists(carpeta): subprocess.call(["cmd", "/c", f"rmdir /s /q {carpeta}"])
    for spec in [f for f in os.listdir() if f.endswith(".spec")]: os.remove(spec)
    messagebox.showinfo("Éxito", f"{nombre} convertido a EXE")

def transformar_py_a_bat():
    archivo = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if not archivo:
        return
    os.makedirs("BAT", exist_ok=True)
    nombre = os.path.basename(archivo)
    bat_name = nombre.replace(".py", ".bat")
    with open(f"BAT/{bat_name}", "w") as f:
        f.write(f"@echo off\npython \"{nombre}\"\npause")
    messagebox.showinfo("Éxito", f"{nombre} convertido a BAT")

def transformar_bat_a_exe():
    archivo = filedialog.askopenfilename(filetypes=[("Batch files", "*.bat")])
    if not archivo:
        return
    if not os.path.exists("Bat_To_Exe_Converter.exe"):
        messagebox.showerror("Falta herramienta", "No se encontró 'Bat_To_Exe_Converter.exe' en la carpeta actual.")
        return
    os.makedirs("EXE", exist_ok=True)
    nombre = os.path.basename(archivo)
    exe_name = nombre.replace(".bat", ".exe")
    os.system(f"Bat_To_Exe_Converter.exe /bat \"{archivo}\" /exe \"EXE/{exe_name}\" /invisible")
    messagebox.showinfo("Éxito", f"{nombre} convertido a EXE")

def transformar_bat_a_py():
    archivo = filedialog.askopenfilename(filetypes=[("Batch files", "*.bat")])
    if not archivo:
        return
    os.makedirs("PY", exist_ok=True)
    nombre = os.path.basename(archivo)
    py_dest = nombre.replace(".bat", ".py")
    with open(archivo, "r") as f_in, open(f"PY/{py_dest}", "w") as f_out:
        f_out.writelines(f_in.readlines())
    messagebox.showinfo("Éxito", f"{nombre} convertido a PY")

# === GUI ===

root = tk.Tk()
root.title("Transformador de Scripts")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="Seleccioná qué querés transformar:", font=("Segoe UI", 12), bg="#f0f0f0")
label.pack(pady=20)

opciones = [
    ("PY ➜ EXE", transformar_py_a_exe),
    ("PY ➜ BAT", transformar_py_a_bat),
    ("BAT ➜ EXE", transformar_bat_a_exe),
    ("BAT ➜ PY", transformar_bat_a_py)
]

for texto, funcion in opciones:
    b = tk.Button(root, text=texto, font=("Segoe UI", 10), width=25, command=funcion)
    b.pack(pady=5)

root.mainloop()
