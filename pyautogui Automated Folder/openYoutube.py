import pyautogui as action
import pyautogui as timeLoad
import pyautogui as mouse
import pyautogui as keyboard

#abrindo o windows
timeLoad.sleep(2)
action.press('win')

#pesquisando google no windows
timeLoad.sleep(1)
action.typewrite('google')
timeLoad.sleep(1)
action.press('enter')

#pesquisando youtube no google
timeLoad.sleep(2)
mouse.moveTo(470, 98)
mouse.click(470,98)
mouse.typewrite('youtube.com')
timeLoad.sleep(1)
action.press("enter")

#procurando video no youtube
timeLoad.sleep(2)
mouse.position(737, 166)
mouse.click(737, 166)
timeLoad.sleep(1)
action.typewrite("de placa")
keyboard.press("enter")

#selecionando video no youtube
timeLoad.sleep(1)
mouse.moveTo(1012, 325)
mouse.click(1012, 325)



