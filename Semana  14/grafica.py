import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Para el DatePicker, se usa tkcalendar


class EventSchedulerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda de Eventos")
        self.geometry("600x400")
        self.resizable(False, False)

        # Frame para la lista de eventos
        self.frame_events = ttk.Frame(self)
        self.frame_events.pack(fill="both", expand=True, padx=10, pady=10)

        # TreeView para mostrar eventos con columnas fecha, hora y descripción
        columns = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_events, columns=columns, show="headings", height=10)
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.column("fecha", width=100, anchor="center")
        self.tree.column("hora", width=80, anchor="center")
        self.tree.column("descripcion", width=380, anchor="w")
        self.tree.pack(side="left", fill="both", expand=True)

        # Scrollbar para la lista de eventos
        scrollbar = ttk.Scrollbar(self.frame_events, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Frame para entrada de datos
        self.frame_input = ttk.Frame(self)
        self.frame_input.pack(fill="x", padx=10, pady=5)

        # Etiquetas y campos de entrada para fecha, hora y descripción
        ttk.Label(self.frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.date_entry = DateEntry(self.frame_input, date_pattern="yyyy-mm-dd")
        self.date_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(self.frame_input, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=2, sticky="e")
        self.entry_time = ttk.Entry(self.frame_input, width=10)
        self.entry_time.grid(row=0, column=3, padx=5, pady=2)

        ttk.Label(self.frame_input, text="Descripción:").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.entry_desc = ttk.Entry(self.frame_input, width=50)
        self.entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=2, sticky="w")

        # Frame para botones
        self.frame_buttons = ttk.Frame(self)
        self.frame_buttons.pack(fill="x", padx=10, pady=10)

        # Botones: Agregar evento, Eliminar evento seleccionado, Salir
        self.btn_add = ttk.Button(self.frame_buttons, text="Agregar Evento", command=self.add_event)
        self.btn_add.pack(side="left", padx=5)

        self.btn_delete = ttk.Button(self.frame_buttons, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.btn_delete.pack(side="left", padx=5)

        self.btn_exit = ttk.Button(self.frame_buttons, text="Salir", command=self.quit)
        self.btn_exit.pack(side="right", padx=5)

    def add_event(self):
        """Agrega un evento nuevo al TreeView si los datos son válidos."""
        fecha = self.date_entry.get()
        hora = self.entry_time.get().strip()
        descripcion = self.entry_desc.get().strip()

        # Validar que hora tenga formato HH:MM básico
        if not self.validate_time(hora):
            messagebox.showerror("Error", "Formato de hora inválido. Use HH:MM.")
            return

        if not descripcion:
            messagebox.showerror("Error", "La descripción no puede estar vacía.")
            return

        # Insertar evento en la lista
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos de entrada después de agregar
        self.entry_time.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def validate_time(self, time_str):
        """Validar que la hora esté en formato HH:MM y valores de 00-23 y 00-59."""
        if len(time_str) != 5 or time_str[2] != ":":
            return False
        hh, mm = time_str.split(":")
        if not (hh.isdigit() and mm.isdigit()):
            return False
        h = int(hh)
        m = int(mm)
        return 0 <= h < 24 and 0 <= m < 60

    def delete_event(self):
        """Elimina el evento seleccionado con confirmación."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Atención", "Debe seleccionar un evento para eliminar.")
            return

        # Confirmar eliminación
        confirm = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar el evento seleccionado?")
        if confirm:
            self.tree.delete(selected_item)


if __name__ == "__main__":
    app = EventSchedulerApp()
    app.mainloop()
