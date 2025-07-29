import tkinter as tk

def abrir_admin(usuario):
    root = tk.Tk()
    root.title("Administrador")
    root.geometry("300x150")

    tk.Label(root, text=f"Administrador: {usuario}").pack(pady=10)
    tk.Label(root, text="Este es el módulo Administrador").pack()

    tk.Button(root, text="Cerrar", command=root.destroy).pack(pady=10)

    root.mainloop()
