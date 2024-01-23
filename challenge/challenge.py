from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By
import pyautogui as timeLoad
from openpyxl import load_workbook

navigate = webdriver.Chrome()

#procurando no navegador o formulário
navigate.get('https://rpachallenge.com/')
timeLoad.sleep(2)

#puxando o arquivo da planilha Excel
dataArchive = 'challenge.xlsx'
sheetData = load_workbook(dataArchive)

sheetSelected = sheetData['Sheet1']

#gerando um looping para puxar os dados de cada linha e coluna da planilha
for lineData in range(2, len(sheetSelected["A"]) + 1) :
    firstName = sheetSelected['A%s' % lineData].value
    lastName = sheetSelected['B%s' % lineData].value
    companyName = sheetSelected['C%s' % lineData].value
    roleInCompany = sheetSelected['D%s' % lineData].value
    adress = sheetSelected['E%s' % lineData].value
    email = sheetSelected['F%s' % lineData].value
    phoneNumber = sheetSelected['G%s' % lineData].value

    globalLetterValue = ''
    timeLoad.sleep(1)

    #gerando um looping que conta as letras em ordem alfabpetica
    for letter in range(ord('a'), ord('g') + 1) :
        letterValue = chr(letter).upper()
        globalLetterValue = letterValue

    #quebrar o looping se o valor de algum dos itens for None
    if sheetSelected[f'{globalLetterValue}%s' % lineData].value == None :
        break

    #preenchendo o endereço da respectiva pessoa puxado da planilha
    navigate.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelAddress')]").send_keys(f'{adress}')
    timeLoad.sleep(1)

    #preenchendo a empresa da respectiva pessoa puxado da planilha
    navigate.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelCompanyName')]").send_keys(f'{companyName}')
    timeLoad.sleep(1)

    #preenchendo o número de telefone da respectiva pessoa puxado da planilha
    navigate.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelPhone')]").send_keys(f'{phoneNumber}')
    timeLoad.sleep(1)

    #preenchendo o e-mail da respectiva pessoa puxado da planilha
    navigate.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelEmail')]").send_keys(f'{email}')
    timeLoad.sleep(1)

    #preenchendo o cargo da respectiva pessoa puxado da planilha
    navigate.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelRole')]").send_keys(f'{roleInCompany}')
    timeLoad.sleep(1)

    #preenchendo o último sobrenome da pessoa puxado da planilha
    navigate.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelLastName')]").send_keys(f'{lastName}')
    timeLoad.sleep(1)

    #preenchendo o nome da pessoa puxado da planilha
    navigate.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelFirstName')]").send_keys(f'{firstName}')
    timeLoad.sleep(2)

    #apertando o botão e enviando o formulário
    navigate.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()

    timeLoad.sleep(3)

timeLoad.sleep(5)