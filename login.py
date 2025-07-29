import tkinter as tk
from tkinter import messagebox
from cliente_modulo import abrir_cliente
from instructor_modulo import abrir_instructor
from admin_modulo import abrir_admin

# Diccionario de usuarios: usuario -> (clave, rol)
usuarios = {
    "cliente1": ("1234", "cliente"),
    "instructor1": ("abcd", "instructor"),
    "admin1": ("admin", "admin")
}

def ventana_login():
    def validar_login():
        usuario = entry_usuario.get()
        clave = entry_clave.get()
        modulo = variable_rol.get()

        if usuario in usuarios:
            clave_correcta, rol = usuarios[usuario]
            if clave == clave_correcta and modulo == rol:
                print("Login exitoso:", usuario, modulo)
                root.destroy()
                if rol == "cliente":
                    abrir_cliente(usuario)
                elif rol == "instructor":
                    abrir_instructor(usuario)
                elif rol == "admin":
                    abrir_admin(usuario)
                return
        messagebox.showerror("Error", "Usuario, contraseña o módulo incorrecto")

    root = tk.Tk()
    root.title("Login - Centro Ecuestre")
    root.geometry("300x200")

    tk.Label(root, text="Usuario").pack(pady=5)
    entry_usuario = tk.Entry(root)
    entry_usuario.pack()

    tk.Label(root, text="Contraseña").pack(pady=5)
    entry_clave = tk.Entry(root, show="*")
    entry_clave.pack()

    tk.Label(root, text="Módulo").pack(pady=5)
    variable_rol = tk.StringVar(value="cliente")
    tk.OptionMenu(root, variable_rol, "cliente", "instructor", "admin").pack()

    tk.Button(root, text="Ingresar", command=validar_login).pack(pady=10)

    root.mainloop()

