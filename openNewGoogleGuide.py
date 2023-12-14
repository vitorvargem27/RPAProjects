import pyautogui as mouse
import pyautogui as timeLoad
import pyautogui as action

#abrindo a aba de pesquisa do Windows
timeLoad.sleep(1.5)
mouse.moveTo(4184, 1602)
mouse.click(4184, 1602)

#abrindo o google chrome automaticamente
timeLoad.sleep(1)
mouse.typewrite('google')
timeLoad.sleep(1)
mouse.press("enter")

#abrindo outra pasta dentro do google
timeLoad.sleep(3)
action.keyDown('ctrl')
action.press('t')
action.keyUp('ctrl')