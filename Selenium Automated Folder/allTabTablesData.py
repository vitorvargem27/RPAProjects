import pyautogui as mouseAction
import pyautogui as timeLoad
from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By

navigate = seleniumOptions.Chrome()

#abrindo o site da tabela
navigate.get("https://rpachallengeocr.azurewebsites.net/")
timeLoad.sleep(3)
mouseAction.click(1477, 33)
timeLoad.sleep(1)
mouseAction.mouseDown(949,1001)
timeLoad.sleep(1)
mouseAction.move(1400, 0, duration= 1)
mouseAction.mouseUp()

for x in range(0,3) :
    #puxando os dados da tabela à partir da cópia do xpath do inspecionar da tabela
    tableElement = navigate.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    #puxando as linhas da tabela à partir dos nomes da tag da tabela no inspecionar
    lines = tableElement.find_elements(By.TAG_NAME, 'tr')

    #puxando as colunas da tabela à partir da tag nop inspecionar
    colums = tableElement.find_elements(By.TAG_NAME, 'td')

    line = 1

    for currentLine in lines :
        print(currentLine.text)
        line += 1

    timeLoad.sleep(1)
    navigate.find_element(By.XPATH,'//*[@id="tableSandbox_next"]').click()
    timeLoad.sleep(1)
