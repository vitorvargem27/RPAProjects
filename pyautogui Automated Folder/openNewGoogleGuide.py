import pyautogui as mouse
import pyautogui as timeLoad
import pyautogui as action

#abrindo a aba de pesquisa do Windows
timeLoad.sleep(1.5)
action.press('win')

#abrindo o google chrome automaticamente
timeLoad.sleep(1)
action.typewrite('google')
timeLoad.sleep(1)
action.press("enter")

#abrindo outra pasta dentro do google
timeLoad.sleep(3)
action.keyDown('ctrl')
action.press('t')
action.keyUp('ctrl')