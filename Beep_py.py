""" #Python

import winsound
import time

for sonido in range(1, 5):
    # Reproduce un tono a 300 Hz durante 400 ms
    winsound.Beep(300, 400)
    # Espera 100 ms antes de reproducir el siguiente tono
    time.sleep(0.1)
    
    from gtts import gTTS
import os """

def reproducir_texto(texto):
    # Crear un objeto gTTS con el texto proporcionado
    tts = gTTS(texto, lang='es')

    # Guardar el audio en un archivo temporal
    tts.save('temp_audio.mp3')

    # Reproducir el audio
    os.system('start temp_audio.mp3')

# Mensaje al inicio
reproducir_texto("Empezando el programa")

# Tu código aquí...
# Por ejemplo, el bucle de sonidos
import winsound
import time

for sonido in range(1, 11):
    winsound.Beep(300, 400)
    time.sleep(0.1)

# Mensaje al final
reproducir_texto("Programa terminado")