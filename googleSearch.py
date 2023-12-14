import pyautogui as mouse
import pyautogui as timeLoad

#abrindo o windows
timeLoad.sleep(2)
mouse.moveTo(4136, 1596)
mouse.click(4136, 1596)

#pesquisando google no windows
timeLoad.sleep(1)
mouse.typewrite('google')
mouse.moveTo(4001, 749)
mouse.click(4001, 749)

#pesquisando facebook no google
timeLoad.sleep(1)
mouse.moveTo(4424, 1557)
mouse.click(4424,1557)
mouse.typewrite('facebook.com')

#pressionando enter para acessar o facebook
timeLoad.sleep(1)
mouse.press("enter")

