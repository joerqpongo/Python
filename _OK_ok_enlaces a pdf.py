import os
import pandas as pd

#Definir la ruta del directorio de PDFs
ruta_directorio_pdf = "C:\\Users\\jose_l_r\\GASTON Y DANIELA\\CONTABILIDAD - ARCHIVO CONTABLE\\2024"

#ruta_directorio_pdf = "https://gastonydanielasa.sharepoint.com\\:b:\\r\\contabilidad\\ARCHIVO%20CONTABLE\\2024"
# Lista para almacenar datos del Excel
datos_excel = []

# Crear el DataFrame de Pandas
df_excel = pd.DataFrame(columns=["Nombre del archivo", "Enlace"])

# Recorrer el directorio y sus subdirectorios
for directorio, _, archivos in os.walk(ruta_directorio_pdf):
    # Recorrer cada archivo en el directorio actual
    for archivo in archivos:
        # Verificar si el archivo es un PDF
        if archivo.endswith(".pdf"):
            # Obtener el nombre del archivo PDF
            nombre_archivo = archivo
            # Generar el enlace para ver el archivo PDF
            ruta_completa = os.path.join(directorio, archivo)
            enlace_archivo = f"file:///{ruta_completa}"

            # Agregar datos a la lista y al DataFrame
            datos_excel.append([nombre_archivo, enlace_archivo])
            df_excel.loc[len(df_excel.index)] = [nombre_archivo, enlace_archivo]

            # Imprimir nombre y enlace
            print(f"Nombre: {nombre_archivo}")
            print(f"Enlace: {enlace_archivo}")
            print("------------------------------")

# Guardar el DataFrame en Excel
ruta_archivo_excel = "C:\\Users\\jose_l_r\\OneDrive - GASTON Y DANIELA\\_Automatizaciones\\tabvinc\Lista de Pdfs guardados.xlsx"
df_excel.to_excel(ruta_archivo_excel, index=False)

# Guardarlo en la nueva carpeta
ruta_archivo_excel = "C:\\Users\\jose_l_r\\GASTON Y DANIELA\CONTABILIDAD - TESORERIA\PAGOS\Tab_Vinc\Lista de Pdfs guardados.xlsx"
df_excel.to_excel(ruta_archivo_excel, index=False)


# Abrir el archivo Excel generado (opcional)
#if os.path.exists(ruta_archivo_excel):
#    os.startfile(ruta_archivo_excel)
    
print("\n\n*******************Archivo creado*******************")
print("*******************FIN*******************\n\n")