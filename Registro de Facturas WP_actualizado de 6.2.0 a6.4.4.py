import pyautogui
import time
import pandas as pd

# Read credentials from Excel sheet
df = pd.read_excel('C:\\Users\\jose_l_r\\OneDrive - GASTON Y DANIELA\\wordpass.xlsx')
username = df['Usuario'][0]
password = df['Contraseña'][0]

# Launch Libra application
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.typewrite('C:\\Users\\jose_l_r\\AppData\\Local\\Programs\\Libra\\Librta.exe')
time.sleep(3)

# Enter credentials and login
pyautogui.click(x=1350, y=350)
time.sleep(1)
pyautogui.typewrite(username)
pyautogui.press('tab')
time.sleep(1)
pyautogui.typewrite(password)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

# Navigate to Documentos
pyautogui.hotkey('alt', 'f4')
time.sleep(1)
pyautogui.hotkey('ctrl', 'w')
time.sleep(2)


pyautogui.click(x=1449, y=820)
time.sleep(1)

# Navigate to C_MREFAP
pyautogui.click(x=1628, y=171)
time.sleep(1)
pyautogui.typewrite('C_MREFAP')
time.sleep(1)
pyautogui.click(x=1679, y=260)
time.sleep(1)

# Read invoice data from Excel sheet
df_invoices = pd.read_excel('C:\\Users\\jose_l_r\\GASTON Y DANIELA\\CONTABILIDAD - FACTURAS\\entrega de facturas\\facturas marcas internacionales\\comprobando\\registrando\\registrando.xlsx')

for index, row in df_invoices.iterrows():
    # Extract invoice data
    numpro = row['Número de documento']
    fechafra = row['Fecha de factura']
    factura = row['Número de factura']
    importe = row['Importe']
    ruta = row['Ruta']

    # Enter invoice details in LIBRA
    pyautogui.typewrite(numpro)
    pyautogui.press('tab')
    pyautogui.typewrite('F')
    pyautogui.press('tab')
    pyautogui.typewrite(fechafra)
    pyautogui.press('tab')
    pyautogui.typewrite(factura)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(importe)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', '2')
    time.sleep(0.5)
    pyautogui.click(x=690, y=441)
    time.sleep(0.5)
    pyautogui.press('s')
    time.sleep(2)

    # Attach invoice file
    pyautogui.click(x=553, y=520)
    time.sleep(1)
    pyautogui.typewrite(ruta)
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)

    # Move invoice file to archived folder
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.5)

    # Record notification
    time.sleep(1)
