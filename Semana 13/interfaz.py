import tkinter as tk
from tkinter import messagebox

# Función para agregar un dato de la entrada a la lista
def agregar_dato():
    dato = entrada_texto.get()  # Obtener texto del campo de entrada
    if dato.strip():  # Verificar que no sea solo espacios
        lista_datos.insert(tk.END, dato)  # Insertar dato al final de la lista
        entrada_texto.delete(0, tk.END)  # Limpiar campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un dato válido.")

# Función para limpiar la lista y el campo de entrada
def limpiar():
    lista_datos.delete(0, tk.END)  # Borrar todos los ítems de la lista
    entrada_texto.delete(0, tk.END)  # Limpiar campo de entrada

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos Simple")  # Título descriptivo
ventana.geometry("400x300")  # Tamaño de ventana

# Etiqueta descriptiva
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto para ingreso de datos
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botón para agregar dato a la lista
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=5)

# Botón para limpiar los datos y la entrada
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
