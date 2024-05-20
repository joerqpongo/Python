import pandas as pd
from pnp import SharePointClient

# Conexión a SharePoint
client = SharePointClient("https://gastonydanielasa.sharepoint.com")

# Ruta del directorio en SharePoint
ruta_directorio_pdf = "/sites/contabilidad/ARCHIVO%20CONTABLE/2024"

# Lista para almacenar datos del Excel
datos_excel = []

# Crear el DataFrame de Pandas
df_excel = pd.DataFrame(columns=["Nombre del archivo", "Enlace"])

# Recorrer los archivos PDF en el directorio
for archivo in client.web.get_folder(ruta_directorio_pdf).files:
    # Obtener nombre y enlace del archivo PDF
    nombre_archivo = archivo.name
    ruta_completa = archivo.server_relative_url
    enlace_archivo = f"https://gastonydanielasa.sharepoint.com{ruta_completa}"

    # Modificar el enlace para usar la URL de SharePoint
    enlace_archivo_modificado = f"{enlace_archivo}/{nombre_archivo}"

    # Agregar datos a la lista y al DataFrame con el enlace modificado
    datos_excel.append([nombre_archivo, enlace_archivo_modificado])
    df_excel.loc[len(df_excel.index)] = [nombre_archivo, enlace_archivo_modificado]

    # Imprimir nombre y enlace
    print(f"Nombre: {nombre_archivo}")
    print(f"Enlace: {enlace_archivo_modificado}")
    print("------------------------------")

# Guardar el DataFrame en Excel
ruta_archivo_excel = "C:\\Users\\jose_l_r\\OneDrive - GASTON Y DANIELA\\_Automatizaciones\\tabvinc"