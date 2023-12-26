import pyautogui as mousePosition #pode ser qualquer nome referente à automação criado
import pyautogui as timeLoad

#tempo de espera para que o computador processe as informações
timeLoad.sleep(1.5)

#ver as coordenadas da aba do windows
#print(mousePosition.position())

#mover para a coordenada da aba do windows
mousePosition.moveTo(4136, 1596)
timeLoad.sleep(1)

#clicar na coordenada solicitada
mousePosition.click(4136, 1596)
timeLoad.sleep(1)

#o typewrite serve para ele escrever o que você quer
mousePosition.typewrite('calculadora')
timeLoad.sleep(1)

#ir até o aplicativo calculadra e abrir ele
mousePosition.moveTo(4001, 749)
timeLoad.sleep(0.5)
mousePosition.click(4001, 749)

