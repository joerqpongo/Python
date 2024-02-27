import pyautogui
import time
import pandas as pd
import openpyxl

# Ruta del programa Libra.exe
libra_path = 'C:\\Users\\jose_l_r\\AppData\\Local\\Programs\\Libra.exe'

# Ejecutar el programa Libra.exe
os.system(libra_path)




# Ruta del archivo Excel
file_path = 'C:\\Users\\jose_l_r\\OneDrive - GASTON Y DANIELA\\wordpass.xlsx'

# Cargar el libro de trabajo
workbook = openpyxl.load_workbook(file_path)

# Seleccionar la hoja de trabajo
sheet = workbook.active

  # Puedes especificar el nombre de la hoja si no es la hoja activa
# Leer el valor de la celda A69
username = sheet['A69'].value
password = sheet['B69'].value


# Cerrar el libro de trabajo
workbook.close()




# # Read credentials from Excel sheet
# df = pd.read_excel('C:\\Users\\jose_l_r\\OneDrive - GASTON Y DANIELA\\wordpass.xlsx')    
# username = df[0][68]
# password = df[1][68]
# Launch Libra application
#pyautogui.hotkey('win', 'r')
#time.sleep(5)
# Ejecutar el programa Libra.exe
os.system(libra_path)
time.sleep(5)

#print (username)
#print (password)

pyautogui.hotkey('enter')


# Enter credentials and login
pyautogui.click(x=1350, y=350)
time.sleep(11)
pyautogui.typewrite(username)
pyautogui.press('tab')
#C:\Users\jose_l_r\AppData\Local\Programs\Libra\Libra.exeC:\Users\jose_l_r\AppData\Local\Programs\Libra\Libra.exe 
time.sleep(1)
pyautogui.typewrite(password)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

# # Navigate to Documentos
# pyautogui.hotkey('alt', 'f4')
# time.sleep(1)
# pyautogui.hotkey('ctrl', 'w')
# time.sleep(2)


# pyautogui.click(x=1449, y=820)
# time.sleep(1)

# # Navigate to C_MREFAP
# pyautogui.click(x=1628, y=171)
# time.sleep(1)
# pyautogui.typewrite('C_MREFAP')
# time.sleep(1)
# pyautogui.click(x=1679, y=260)
# time.sleep(1)

# # Read invoice data from Excel sheet
# df_invoices = pd.read_excel('C:\\Users\\jose_l_r\\GASTON Y DANIELA\\CONTABILIDAD - FACTURAS\\entrega de facturas\\facturas marcas internacionales\\comprobando\\registrando\\registrando.xlsx')

# for index, row in df_invoices.iterrows():
#     # Extract invoice data
#     numpro = row['Número de documento']
#     fechafra = row['Fecha de factura']
#     factura = row['Número de factura']
#     importe = row['Importe']
#     ruta = row['Ruta']

#     # Enter invoice details in LIBRA
#     pyautogui.typewrite(numpro)
#     pyautogui.press('tab')
#     pyautogui.typewrite('F')
#     pyautogui.press('tab')
#     pyautogui.typewrite(fechafra)
#     pyautogui.press('tab')
#     pyautogui.typewrite(factura)
#     pyautogui.press('tab')
#     pyautogui.press('tab')
#     pyautogui.typewrite(importe)
#     pyautogui.press('tab')
#     time.sleep(0.5)
#     pyautogui.hotkey('ctrl', '2')
#     time.sleep(0.5)
#     pyautogui.click(x=690, y=441)
#     time.sleep(0.5)
#     pyautogui.press('s')
#     time.sleep(2)

#     # Attach invoice file
#     pyautogui.click(x=553, y=520)
#     time.sleep(1)
#     pyautogui.typewrite(ruta)
#     pyautogui.press('enter')
#     time.sleep(4)
#     pyautogui.press('enter')
#     time.sleep(2)
#     pyautogui.press('enter')
#     time.sleep(1)

#     # Move invoice file to archived folder
#     time.sleep(0.5)
#     pyautogui.press('down')
#     time.sleep(1)
#     pyautogui.press('tab')
#     time.sleep(0.5)

#     # Record notification
#     time.sleep(1)
