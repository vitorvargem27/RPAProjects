from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
import pandas as panda

navigate = seleniumOptions.Chrome()

#abrindo o site da tabela
navigate.get("https://rpachallengeocr.azurewebsites.net/")

#puxando os dados da tabela à partir da cópia do xpath do inspecionar da tabela
tableElement = navigate.find_element(By.XPATH, '//*[@id="tableSandbox"]')

#puxando as linhas da tabela à partir dos nomes da tag da tabela no inspecionar
lines = tableElement.find_elements(By.TAG_NAME, 'tr')

#puxando as colunas da tabela à partir da tag nop inspecionar
colums = tableElement.find_elements(By.TAG_NAME, 'td')

#criando o lugar onde os dados serão salvos
dataFrameLista = []

line = 1

#looping de adicionar cada linha da tabela no excel
for currentLine in lines :
    dataFrameLista.append(currentLine.text)
    line += 1

#dando nome para a coluna do excel
dataFrame = panda.DataFrame(dataFrameLista, columns=['Dados'])

#criando o arquivo excel para pegar os dados
#prepara o arquivo do excel com o excel Writer
excelArchive = panda.ExcelWriter('siteData.xlsx', engine='xlsxwriter')

#enviando o arquivo para uma planilha excel
dataFrame.to_excel(excelArchive, sheet_name='Sheet1', index=True)

#salva as informações do arquivo para o excel
excelArchive._save()