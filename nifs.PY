<<<<<<< HEAD
import PyPDF2
=======
import os
from PyPDF2 import PdfReader
>>>>>>> 7f9732bdf44b79eed2a03e821abd793b4612fc25

<<<<<<< HEAD
<<<<<<< HEAD
# Ruta del archivo PDF a buscar
archivo_pdf = "C:/Users/jose_l_r/GASTON Y DANIELA/CONTABILIDAD - FACTURAS/entrega de facturas/facturas marcas internacionales/110786_1053151_2024.pdf"
=======
# Ruta de la carpeta a buscar
#En Gaston_____ ruta_carpeta = "C:\Users\jose_l_r\GASTON Y DANIELA\CONTABILIDAD - FACTURAS\entrega de facturas\facturas marcas internacionales"
ruta_carpeta = "C:\JL\F_Prueba"
>>>>>>> 5fd23adc030a8d4f1509dc874eb6f32669bf399e
=======
# Ruta del directorio de las facturas
ruta_directorio = "C:\\JL\\F_Prueba"  # Doble barra invertida o usar barra inclinada
>>>>>>> 7f9732bdf44b79eed2a03e821abd793b4612fc25

<<<<<<< HEAD
# Palabra a buscar
nif_gaston = "A48005102"
nif_proveedor="TVA FR 78 582 015 251"
=======
# Diccionario para almacenar los metadatos de cada archivo PDF
metadatos = {}
>>>>>>> 7f9732bdf44b79eed2a03e821abd793b4612fc25

<<<<<<< HEAD

# Función para buscar texto en un PDF
def buscar_texto_en_pdf(archivo_pdf, palabras_buscar):
    # Cargo el PDF
    with open(archivo_pdf, "rb") as f:
        pdf = f.read()
=======
# Recorremos las facturas del directorio
for archivo in os.listdir(ruta_directorio):
    # Si el archivo es un PDF
    if archivo.endswith(".pdf"):
        # Obtenemos la ruta del archivo
        archivo_pdf = os.path.join(ruta_directorio, archivo)
>>>>>>> 7f9732bdf44b79eed2a03e821abd793b4612fc25

        # Abrimos el archivo PDF
        with open(archivo_pdf, "rb") as f:
            reader = PdfReader(f)

            # Guardamos los metadatos del archivo PDF
            metadatos[archivo] = reader.metadata
            # Recorremos las páginas del PDF
            for pagina in reader.pages:
                try:
                    # Extraemos el texto de la página
                    texto_pagina = pagina.extract_text()
                except Exception as e:
                    print(f"Error al leer el archivo PDF: {e}")
                    texto_pagina = ""

                # Imprimimos el texto de la página
                print(f"Contenido de la página en {archivo}:\n{texto_pagina}\n")

# Imprimimos los metadatos de cada archivo PDF
for archivo, info in metadatos.items():
    print(f"Metadatos del archivo {archivo}:\n{info}\n")