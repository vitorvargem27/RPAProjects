import pyautogui as mouse
import pyautogui as keyboard
import pyautogui as action
import pyautogui as timeLoad

timeLoad.sleep(2)
print(mouse.position())

#abrindo o whatsApp
timeLoad.sleep(2)
action.press('win')

#pesquisando whatsapp no windows
timeLoad.sleep(1)
action.typewrite('whatsapp')
timeLoad.sleep(1)
action.press('enter')

#achando conversa
timeLoad.sleep(4)
mouse.moveTo(356, 188)
mouse.click(356, 188)
timeLoad.sleep(2)
action.typewrite("vitor")
timeLoad.sleep(2)
keyboard.press("tab")
keyboard.press("down")
keyboard.press("enter")

#escrevendo mensagem
timeLoad.sleep(2)
mouse.moveTo(1033, 974)
mouse.click(1033, 974)
timeLoad.sleep(2)
action.typewrite("Boa noite, aqui vai um teste de mensagem!!", interval=0.1)
keyboard.press("enter")



