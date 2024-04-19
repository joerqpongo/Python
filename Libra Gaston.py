import tkinter as tk
import pyttsx3
import pandas as pd

# Función para hablar
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Configuración de voz
engine = pyttsx3.init()

# Lectura de datos de Excel
df = pd.read_excel('C:\Users\jose_l_r\OneDrive - GASTON Y DANIELA\wordpass.xlsx')

# Obtención de usuario y contraseña
username = df.loc[68, 0]
password = df.loc[68, 1]

# Función para mostrar mensaje
def show_message(text):
    message_label.config(text=text)

# Función para iniciar el proceso
def start_process():
    speak("Iniciando proceso...")
    show_message("Iniciando proceso...")
    # Aquí se debería implementar la automatización de Libra
    # ...
    speak("Proceso finalizado.")
    show_message("Proceso finalizado.")

# Creación de la ventana principal
root = tk.Tk()
root.title("Automatización Libra")

# Creación de widgets
message_label = tk.Label(text="Presione el botón para iniciar el proceso")
start_button = tk.Button(text="Iniciar", command=start_process)

# Diseño de la ventana
message_label.pack()
start_button.pack()

# Bucle principal
root.mainloop()