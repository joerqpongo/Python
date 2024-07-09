import os
import pandas as pd

# Ruta del archivo Excel y la carpeta donde se buscarán los archivos PDF
ruta_excel = r'C:\_ComprobaFra\_FacturasJL.xlsx'
ruta_carpeta = r'C:\_ComprobaFra'

# Leer el archivo Excel en un DataFrame
df = pd.read_excel(ruta_excel)

# Lista para almacenar los resultados
resultados = []

# Iterar sobre las filas de la columna 'S', desde la fila 2 hasta la 1987
for indice in range(1, 1987):
    nombre_archivo = df.at[indice, 'S']

    # ... (rest of your code)

    # Check if the file exists in the folder
    if str(nombre_archivo) + '.pdf' in archivos:
            # Si se encuentra el archivo, añadir "ENC" a la lista de resultados
            resultados.append('ENC')
            encontrado = True
            break
    
    # Si no se encontró el archivo, añadir "NA" a la lista de resultados
    if not encontrado:
        resultados.append('NA')

# Añadir la lista de resultados al DataFrame en la columna 'T' (índice 19)
df['T'] = pd.Series(resultados)

# Guardar el DataFrame modificado de nuevo en el archivo Excel
df.to_excel(ruta_excel, index=False)

print("Proceso completado.")
