import tkinter as tk
from tkinter import ttk, messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas - Atajos de Teclado")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')

        # Lista para almacenar las tareas
        self.tasks = []

        # Configurar el estilo
        self.setup_styles()

        # Crear la interfaz
        self.create_widgets()

        # Configurar atajos de teclado
        self.setup_keyboard_shortcuts()

    def setup_styles(self):
        """Configurar estilos para la aplicación"""
        style = ttk.Style()
        style.configure('Completed.TLabel', foreground='gray', font=('Arial', 10, 'overstrike'))
        style.configure('Pending.TLabel', foreground='black', font=('Arial', 10))
        style.configure('Add.TButton', padding=(10, 5))
        style.configure('Action.TButton', padding=(5, 2))

    def create_widgets(self):
        """Crear todos los elementos de la interfaz"""

        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)

        # Título
        title_label = ttk.Label(main_frame,
                                text="Gestor de Tareas",
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))

        # Frame de entrada de tareas
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(0, weight=1)

        # Etiqueta y campo de entrada
        ttk.Label(input_frame, text="Nueva Tarea:").grid(row=0, column=0, sticky=tk.W)

        self.task_entry = ttk.Entry(input_frame, font=('Arial', 11))
        self.task_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        self.task_entry.focus()

        # Botón para añadir tarea
        self.add_button = ttk.Button(input_frame,
                                     text="Añadir Tarea (Enter)",
                                     command=self.add_task,
                                     style='Add.TButton')
        self.add_button.grid(row=1, column=1, padx=(10, 0))

        # Frame de botones de acción
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))

        # Botones de acción
        self.complete_button = ttk.Button(action_frame,
                                          text="Marcar como Completada (C)",
                                          command=self.complete_task,
                                          style='Action.TButton')
        self.complete_button.grid(row=0, column=0, padx=(0, 10))

        self.delete_button = ttk.Button(action_frame,
                                        text="Eliminar Tarea (D)",
                                        command=self.delete_task,
                                        style='Action.TButton')
        self.delete_button.grid(row=0, column=1, padx=(0, 10))

        # Lista de tareas con Scrollbar
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Crear Treeview para mostrar tareas
        self.tasks_tree = ttk.Treeview(list_frame,
                                       columns=('status', 'task'),
                                       show='tree headings',
                                       height=12)
        self.tasks_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar columnas
        self.tasks_tree.column('#0', width=0, stretch=False)
        self.tasks_tree.column('status', width=20, anchor='center')
        self.tasks_tree.column('task', width=400, anchor='w')

        # Configurar headings
        self.tasks_tree.heading('status', text='✓')
        self.tasks_tree.heading('task', text='Tarea')

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tasks_tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tasks_tree.configure(yscrollcommand=scrollbar.set)

        # Etiqueta de instrucciones
        instructions = ttk.Label(main_frame,
                                 text="Atajos: Enter=Añadir, C=Completar, D=Eliminar, Esc=Salir",
                                 font=('Arial', 9),
                                 foreground='gray')
        instructions.grid(row=4, column=0, columnspan=3, pady=(10, 0))

    def setup_keyboard_shortcuts(self):
        """Configurar los atajos de teclado"""
        # Enter para añadir tarea
        self.root.bind('<Return>', lambda event: self.add_task())

        # C para marcar como completada
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<C>', lambda event: self.complete_task())

        # D para eliminar tarea
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())

        # Delete para eliminar tarea
        self.root.bind('<Delete>', lambda event: self.delete_task())

        # Escape para salir
        self.root.bind('<Escape>', lambda event: self.root.quit())

        # Focus en el campo de entrada al presionar cualquier tecla
        self.root.bind('<Key>', self.focus_on_entry)

    def focus_on_entry(self, event):
        """Enfocar el campo de entrada si no es un atajo especial"""
        if event.keysym not in ['Return', 'c', 'C', 'd', 'D', 'Delete', 'Escape']:
            self.task_entry.focus()

    def add_task(self):
        """Añadir una nueva tarea a la lista"""
        task_text = self.task_entry.get().strip()

        if task_text:
            # Añadir a la lista interna
            self.tasks.append({'text': task_text, 'completed': False})

            # Añadir al Treeview
            item_id = self.tasks_tree.insert('', 'end', values=('', task_text))

            # Limpiar campo de entrada
            self.task_entry.delete(0, tk.END)

            # Feedback visual
            self.task_entry.focus()
            print(f"Tarea añadida: {task_text}")
        else:
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")

    def complete_task(self):
        """Marcar la tarea seleccionada como completada"""
        selected_item = self.tasks_tree.selection()

        if selected_item:
            item = selected_item[0]
            current_values = self.tasks_tree.item(item, 'values')

            if current_values[0] == '✓':
                # Si ya está completada, marcarla como pendiente
                self.tasks_tree.set(item, 'status', '')
                self.update_task_status(item, False)
                print("Tarea marcada como pendiente")
            else:
                # Marcar como completada
                self.tasks_tree.set(item, 'status', '✓')
                self.update_task_status(item, True)
                print("Tarea marcada como completada")
        else:
            messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea.")

    def delete_task(self):
        """Eliminar la tarea seleccionada"""
        selected_item = self.tasks_tree.selection()

        if selected_item:
            item = selected_item[0]
            task_text = self.tasks_tree.item(item, 'values')[1]

            # Confirmar eliminación
            if messagebox.askyesno("Confirmar eliminación",
                                   f"¿Estás seguro de que quieres eliminar la tarea:\n\"{task_text}\"?"):
                # Eliminar de la lista interna
                self.remove_task_from_list(task_text)

                # Eliminar del Treeview
                self.tasks_tree.delete(item)
                print(f"Tarea eliminada: {task_text}")
        else:
            messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea.")

    def update_task_status(self, item_id, completed):
        """Actualizar el estado de una tarea en la lista interna"""
        task_text = self.tasks_tree.item(item_id, 'values')[1]

        for task in self.tasks:
            if task['text'] == task_text:
                task['completed'] = completed
                break

    def remove_task_from_list(self, task_text):
        """Eliminar una tarea de la lista interna"""
        self.tasks = [task for task in self.tasks if task['text'] != task_text]

    def get_task_count(self):
        """Obtener estadísticas de tareas"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task['completed'])
        pending = total - completed

        return total, completed, pending


def main():
    """Función principal para ejecutar la aplicación"""
    try:
        root = tk.Tk()
        app = TaskManagerApp(root)

        # Mostrar mensaje de bienvenida
        print("=== Gestor de Tareas Iniciado ===")
        print("Atajos disponibles:")
        print("- Enter: Añadir tarea")
        print("- C: Marcar como completada/pendiente")
        print("- D o Delete: Eliminar tarea")
        print("- Escape: Salir de la aplicación")
        print("=================================")

        root.mainloop()

    except Exception as e:
        print(f"Error al ejecutar la aplicación: {e}")
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")


if __name__ == "__main__":
    main()