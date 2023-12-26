from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By

navigate = seleniumOptions.Chrome()

#abrindo o site da tabela
navigate.get("https://rpachallengeocr.azurewebsites.net/")

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
