import os

# Ruta de la carpeta
carpeta = "C:\\Users\\jose_l_r\\GASTON Y DANIELA\\CONTABILIDAD - FACTURAS\\entrega de facturas\\facturas marcas internacionales\\comprobando\\registrando\\registradas\\Contabilizadas\\2024\\2024 07 JULIO\\100.07"

# Recorrer todos los archivos en la carpeta
for archivo in os.listdir(carpeta):
    # Verificar si el archivo es un PDF
    if archivo.endswith(".pdf"):
        # Verificar si el nombre comienza con "100.07."
        if not archivo.startswith("100.07."):
            # Renombrar el archivo
            os.rename(os.path.join(carpeta, archivo), os.path.join(carpeta, "100.07." + archivo))

print("¡Los archivos PDF han sido renombrados!")