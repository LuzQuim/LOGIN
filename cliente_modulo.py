import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

reservas = []

def abrir_cliente(usuario):
    root = tk.Tk()
    root.title(f"Panel de Cliente - {usuario}")
    root.geometry("400x300")

    tk.Label(root, text=f"Bienvenido, {usuario}", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Crear Reserva", command=lambda: crear_reserva(root)).pack(pady=5)
    tk.Button(root, text="Ver Caballos", command=ver_caballos).pack(pady=5)
    tk.Button(root, text="Agendar Clase", command=lambda: agendar_clase(root)).pack(pady=5)
    tk.Button(root, text="Ver Reservas", command=lambda: ver_reservas(root)).pack(pady=5)

    root.mainloop()

def crear_reserva(root):
    ventana = tk.Toplevel(root)
    ventana.title("Crear Reserva")
    ventana.geometry("300x300")

    tk.Label(ventana, text="Nombre:").pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    tk.Label(ventana, text="Selecciona una fecha:").pack()
    calendario = Calendar(ventana, selectmode='day', date_pattern='yyyy-mm-dd')
    calendario.pack(pady=10)

    tk.Label(ventana, text="Caballo:").pack()
    caballo_entry = tk.Entry(ventana)
    caballo_entry.pack()

    def guardar():
        nombre = nombre_entry.get()
        fecha = calendario.get_date()
        caballo = caballo_entry.get()
        if not nombre or not caballo:
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
            return
        reservas.append((nombre, fecha, caballo))
        messagebox.showinfo("Reserva creada", "Tu reserva ha sido registrada.")
        ventana.destroy()

    tk.Button(ventana, text="Guardar reserva", command=guardar).pack(pady=10)

def ver_caballos():
    caballos = ["Relámpago", "Tornado", "Estrella", "Pegaso", "Lucero"]
    texto = "\n".join(caballos)
    messagebox.showinfo("Caballos disponibles", texto)

def agendar_clase(root):
    ventana = tk.Toplevel(root)
    ventana.title("Agendar Clase")
    ventana.geometry("300x300")

    tk.Label(ventana, text="Nombre:").pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    tk.Label(ventana, text="Fecha:").pack()
    calendario = Calendar(ventana, selectmode='day', date_pattern='yyyy-mm-dd')
    calendario.pack(pady=10)

    tk.Label(ventana, text="Instructor:").pack()
    instructor_entry = tk.Entry(ventana)
    instructor_entry.pack()

    def guardar_clase():
        nombre = nombre_entry.get()
        fecha = calendario.get_date()
        instructor = instructor_entry.get()
        if not nombre or not instructor:
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
            return
        messagebox.showinfo("Clase agendada", f"{nombre} tiene clase con {instructor} el {fecha}")
        ventana.destroy()

    tk.Button(ventana, text="Agendar clase", command=guardar_clase).pack(pady=10)

def ver_reservas(root):
    ventana = tk.Toplevel(root)
    ventana.title("Reservas existentes")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Reservas creadas:").pack(pady=5)

    lista = tk.Listbox(ventana, width=60)
    for i, (nombre, fecha, caballo) in enumerate(reservas):
        lista.insert(tk.END, f"{i+1}. {nombre} - {fecha} - {caballo}")
    lista.pack(pady=10)

    def cancelar_reserva():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Selecciona una reserva para cancelar.")
            return
        index = seleccion[0]
        reservas.pop(index)
        lista.delete(index)
        messagebox.showinfo("Reserva cancelada", "La reserva ha sido eliminada.")

    tk.Button(ventana, text="Cancelar reserva seleccionada", command=cancelar_reserva).pack(pady=5)

