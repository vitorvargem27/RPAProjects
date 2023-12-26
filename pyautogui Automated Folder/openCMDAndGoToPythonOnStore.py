import pyautogui as action
import pyautogui as timeLoad

timeLoad.sleep(2)
action.hotkey('win', 'r')

timeLoad.sleep(1)
action.typewrite('cmd')
action.press('enter')

timeLoad.sleep(3)
action.typewrite('python')
action.press('enter')