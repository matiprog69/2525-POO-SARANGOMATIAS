import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Lista para almacenar tareas
tasks = []

# Función para añadir tarea
def add_task():
    task = entry_task.get()
    if task != "":
        # Añadir tarea a la lista y al Listbox
        tasks.append(task)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese una tarea")

# Función para marcar tarea como completada (modificar visualmente)
def complete_task():
    try:
        # Obtener índice de la tarea seleccionada
        selected_index = listbox_tasks.curselection()[0]
        task = tasks[selected_index]
        # Agregar indicativo de completado
        if not task.endswith(" (Completada)"):
            tasks[selected_index] = task + " (Completada)"
            listbox_tasks.delete(selected_index)
            listbox_tasks.insert(selected_index, tasks[selected_index])
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar")

# Función para eliminar tarea seleccionada
def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
        tasks.pop(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar")

# Función que añade tarea al presionar Enter
def enter_pressed(event):
    add_task()

# Crear widgets
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)
entry_task.bind('<Return>', enter_pressed)  # Evento Enter

button_add = tk.Button(root, text="Añadir Tarea", command=add_task)
button_add.pack(pady=5)

button_complete = tk.Button(root, text="Marcar como Completada", command=complete_task)
button_complete.pack(pady=5)

button_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
button_delete.pack(pady=5)

listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Evento opcional: doble clic para marcar tarea como completada
def double_click(event):
    complete_task()

listbox_tasks.bind('<Double-Button-1>', double_click)

# Ejecutar la aplicación
root.mainloop()
