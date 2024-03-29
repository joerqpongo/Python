# Importar la biblioteca PyPDF2
import PyPDF2

# Abrir el archivo PDF en modo binario de lectura
file = open("documento.pdf", "rb")

# Crear un objeto PdfFileReader
pdfreader = PyPDF2.PdfFileReader(file)

# Recorrer todas las páginas del PDF
for i in range(pdfreader.numPages):

    # Obtener la página actual
    page = pdfreader.getPage(i)

    # Extraer el texto de la página
    text = page.extractText()

    # Buscar el texto deseado
    if "A48005102" in text:

        # Imprimir el número de página donde se encontró el texto
        print(f"El texto 'A48005102' se encontró en la página {i + 1}")

# Cerrar el archivo PDF
file.close()

