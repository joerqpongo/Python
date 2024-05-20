import pandas as pd
from pnp.sp import SharePointClient

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
    enlace_archivo = f"https://gastonydanielasa.sharepoint.com/sites/contabilidad/ARCHIVO%20CONTABLE/2024/{nombre_archivo}"

    # Agregar datos a la lista y al DataFrame
    datos_excel.append([nombre_archivo, enlace_archivo])
    df_excel.loc[len(df_excel.index)] = [nombre_archivo, enlace_archivo]

    # Imprimir nombre y enlace
    print(f"Nombre: {nombre_archivo}")
    print(f"Enlace: {enlace_archivo}")
    print("------------------------------")

# Guardar el DataFrame en Excel
ruta_archivo_excel = "C:\\Users\\jose_l_r\\OneDrive - GASTON Y DANIELA\\_Automatizaciones\\tabvinc\Lista de facturas contabilizadas.xlsx"
df_excel.to_excel(ruta_archivo_excel, index=False)

# Abrir el archivo Excel generado (opcional)
if os.path.exists(ruta_archivo_excel):
    os.startfile(ruta_archivo_excel)
