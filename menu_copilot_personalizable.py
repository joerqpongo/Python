import tkinter as tk

# Definimos las opciones del menú
opciones = ["Opción 1", "Opción 2", "Opción 3"]

# Función que se ejecuta cuando se selecciona una opción
def opcion_seleccionada(opcion):
    # Aquí puedes implementar la lógica para cada opción seleccionada
    print(f"Has elegido: {opcion}")

# Creamos la ventana principal
root = tk.Tk()
root.title("Menú Reutilizable")

# Creamos una variable para almacenar la opción seleccionada
seleccion = tk.StringVar(root)
seleccion.set(opciones[0])  # Establecemos la opción predeterminada

# Creamos el menú desplegable
menu_desplegable = tk.OptionMenu(root, seleccion, *opciones, command=opcion_seleccionada)
menu_desplegable.pack()

# Iniciamos el bucle principal de la aplicación
root.mainloop()