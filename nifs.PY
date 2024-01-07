import os

# Ruta de la carpeta a buscar
#En Gaston_____ ruta_carpeta = "C:\Users\jose_l_r\GASTON Y DANIELA\CONTABILIDAD - FACTURAS\entrega de facturas\facturas marcas internacionales"
ruta_carpeta = "C:\JL\F_Prueba"

# Palabras a buscar
palabras_buscar = ["A48005102", "FR 15 642 048 821"]

# Función para buscar texto en un PDF
def buscar_texto_en_pdf(archivo_pdf, palabras_buscar):
    # Cargo el PDF
    with open(archivo_pdf, "rb") as f:
        pdf = f.read()

    # Extraigo el texto del PDF
    texto = pdftotext.PDF(pdf)

    # Busco las palabras
    for palabra in palabras_buscar:
        if palabra in texto:
            print(f"La palabra '{palabra}' encontrada en el PDF {archivo_pdf}")

# Recorro la carpeta y busco los PDF
for archivo in os.listdir(ruta_carpeta):
    if archivo.endswith(".pdf"):
        archivo_pdf = os.path.join(ruta_carpeta, archivo)
        buscar_texto_en_pdf(archivo_pdf, palabras_buscar)
