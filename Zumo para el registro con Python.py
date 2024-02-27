import os
import win32com.client
import tkinter as tk
import time

def talk(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
    
def start_registration():
    #talk("Haz click para empezar")
    os.startfile(r"C:\Users\jose_l_r\OneDrive - GASTON Y DANIELA\Equipo 318\DROPBOX 318\AutoitPortable\Mis programas\Libra\_CONTABIIZAR\01 de C Registro de  Facturas dar de alta.exe")

window = tk.Tk()
window.title("Zumito de fras PARA el REGISTRO")
window.geometry("450x121+192+145")
time.sleep(2)
talk("Haz click para empezar")

button = tk.Button(window, text="Zumo de Facturas a Registrar", font=("Tahoma", 20, "bold"), command=start_registration)
button.pack(expand=True)

window.mainloop()

print("Archivo Terminado")