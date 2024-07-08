import os
from PyPDF2 import PdfReader

# Ruta del directorio de las facturas
ruta_directorio = "C:\\JL\\F_Prueba"  # Doble barra invertida o usar barra inclinada

# Diccionario para almacenar los metadatos de cada archivo PDF
metadatos = {}

# Recorremos las facturas del directorio
for archivo in os.listdir(ruta_directorio):
    # Si el archivo es un PDF
    if archivo.endswith(".pdf"):
        # Obtenemos la ruta del archivo
        archivo_pdf = os.path.join(ruta_directorio, archivo)

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
                    if texto_pagina.find("A48005102") != -1:
                        print(f"El archivo {archivo} contiene el texto 'A48005102'.")
                    else:print(f"El archivo {archivo} NooooooooooooooooooooooO contiene el texto 'A48005102'.")
                except Exception as e:
                    print(f"Error al leer el archivo PDF: {e}")
                    texto_pagina = ""

                # Imprimimos el texto de la página
                print(f"Contenido de la página en {archivo}:\n{texto_pagina}\n")

# Imprimimos los metadatos de cada archivo PDF
for archivo, info in metadatos.items():
    print(f"Metadatos del archivo {archivo}:\n{info}\n")
    print("Parece que "+ archivo, " no tiene metadatos de interés " )