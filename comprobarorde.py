import os
import time

while True:
    if os.path.exists("C:/OrdenesRecibidas/ejecutarorden.txt"):
        print("¡Archivo encontrado! Ejecutando la orden...")
        # Aquí se ejecuta la orden deseada
        print("texto imprimido")
        os.remove("C:/OrdenesRecibidas/ejecutarorden.txt")
        print("¡Orden ejecutada correctamente!")
    else:
        print("Esperando...")
    time.sleep(15)  # Espera 15 segundos antes de volver a comprobar

    if os.path.exists("C:/OrdenesRecibidas/programa1.txt"):
        print("¡Archivo programa1 encontrado! Ejecutando la orden...")
        # Aquí se ejecuta la orden deseada para programa1
        print("imprime programa1")
        os.remove("C:/OrdenesRecibidas/programa1.txt")
        print("¡Orden ejecutada correctamente para programa1!")
    elif os.path.exists("C:/OrdenesRecibidas/programa2.txt"):
        print("¡Archivo programa2 encontrado! Ejecutando la orden...")
        # Aquí se ejecuta la orden deseada para programa2
        print("imprime programa2")
        os.remove("C:/OrdenesRecibidas/programa2.txt")
        print("¡Orden ejecutada correctamente para programa2!")
    elif os.path.exists("C:/OrdenesRecibidas/programa3.txt"):
        print("¡Archivo programa3 encontrado! Ejecutando la orden...")
        # Aquí se ejecuta la orden deseada para programa3
        print("imprime programa3")
        os.remove("C:/OrdenesRecibidas/programa3.txt")
        print("¡Orden ejecutada correctamente para programa3!")
    else:
        print("Esperando...")