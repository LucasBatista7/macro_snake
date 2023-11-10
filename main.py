import pyautogui #detecta eventos/acoes
import keyboard #parte do mouse
while not keyboard.is_pressed('m'): #Enquanto nao cancelar...
  pyautogui.sleep(5)
  pyautogui.press('down')
  pyautogui.sleep(0.016)
  pyautogui.press('left')
