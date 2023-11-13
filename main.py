import pyautogui #detecta eventos/acoes
import keyboard #parte do mouse

freq = float(input("Enter frequency (in seconds): "))
print("Task will start in 3 seconds")
pyautogui.sleep(3)
while not keyboard.is_pressed('m'): #Enquanto nao cancelar...
    pyautogui.sleep(freq)
    pyautogui.press('down')
    pyautogui.press('left')
print('Ended task')
