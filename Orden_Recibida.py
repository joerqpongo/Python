#Comprueba si existe un archivo en la carpeta elegida y ejecuta una acción
import os
import time

while True:
    file_path = "C:/OrdenesRecibidas/ejecutarorden.txt"
    if os.path.exists(file_path):
        print("¡Archivo encontrado! Ejecutando la orden...")
        # Aquí se ejecuta la orden deseada
        os.remove(file_path)
        print("¡Orden ejecutada correctamente!")
    else:
        print("Esperando...")
    time.sleep(10)  # Espera 10 segundos antes de volver a comprobar
