import pyautogui as mouse
import pyautogui as timeLoad
import pyautogui as action

#abrindo o windows
timeLoad.sleep(2)
action.press('win')

#pesquisando google no windows
timeLoad.sleep(1)
action.typewrite('google')
timeLoad.sleep(1)
action.press('enter')

#pesquisando facebook no google
timeLoad.sleep(2)
mouse.moveTo(3330, 98)
mouse.click(3330,98)
mouse.typewrite('facebook.com')

#pressionando enter para acessar o facebook
timeLoad.sleep(1)
mouse.press("enter")

