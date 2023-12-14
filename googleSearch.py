import pyautogui as mouse
import pyautogui as timeLoad

#abrindo o windows
timeLoad.sleep(2)
mouse.moveTo(4184, 1602)
mouse.click(4184, 1602)

#pesquisando google no windows
timeLoad.sleep(1)
mouse.typewrite('google')
timeLoad.sleep(1)
mouse.press('enter')

#pesquisando facebook no google
timeLoad.sleep(4)
mouse.moveTo(3330, 98)
mouse.click(3330,98)
mouse.typewrite('facebook.com')

#pressionando enter para acessar o facebook
timeLoad.sleep(1)
mouse.press("enter")

