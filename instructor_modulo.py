import tkinter as tk

def abrir_instructor(usuario):
    root = tk.Tk()
    root.title("Módulo Instructor")
    root.geometry("300x150")

    tk.Label(root, text=f"Instructor: {usuario}").pack(pady=10)
    tk.Label(root, text="Este es el módulo de Instructor").pack()

    tk.Button(root, text="Cerrar", command=root.destroy).pack(pady=10)

    root.mainloop()
