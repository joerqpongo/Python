import webbrowser
import pyautogui
url="https://empresas.bankinter.com/secure/es/cuentas-y-tarjetas/cuentas/norma43?tab=pendientes"
webbrowser.open(url)


# # Obtiene las dimensiones de la pantalla
# width, height = pyautogui.Size()

# # Imprime las dimensiones de la pantalla
# print(f"Ancho de la pantalla: {width} píxeles")
# print(f"Alto de la pantalla: {height} píxeles")
#pantalla = pyautogui.Size()

# Obtiene las dimensiones de la pantalla
#screen_width, screen_height = pyautogui.Size()

pyautogui.sleep(4)

# Maximiza la ventana actual
pyautogui.hotkey('winleft', 'up')  # Puedes ajustar esto según tus necesidades

# Puedes agregar comentarios para explicar cada línea de código

pyautogui.sleep(5)
pyautogui.press('tab', presses=11)
pyautogui.sleep(2)
pyautogui.write('GASROM2'.upper())
pyautogui.sleep(1)
pyautogui.press('tab', presses=1)
pyautogui.sleep(1)
pyautogui.write('318031')

pyautogui.sleep(2)

pyautogui.press('enter', presses=1)

pyautogui.sleep(5)

pyautogui.leftClick(411,540,1)
#pyautogui.moveandclick(411,540,0)

pyautogui.sleep(2)

pyautogui.leftClick(1225,538)

pyautogui.sleep(2)

#pyautogui.leftClick(1193,558)
#pyautogui.moveto(1193,558)

pyautogui.sleep(3)

pyautogui.alert("Archivo descargado")
#pyautogui.sleep(2)

#print(pantalla)
#pyautogui.alert(Pantalla)

#pyautogui.moveTo(1131, 484)
#print (screen_width, screen_height)

#Y INTRO
""" pyautogui.press('tab', presses=1)
pyautogui.sleep(5) """




#""" # Encuentra el elemento por su expresión XPath
# element = driver.find_element_by_xpath("//a[contains(text(), 'Descargar en formato Excel')]")

# # Hace clic en el elemento
# element.click() """
#""" pyautogui.moveTo(1131, 484)
