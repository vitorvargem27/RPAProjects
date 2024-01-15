from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
import pyautogui as timeLoad
import pandas as pd

adressList = []
dataFrameList = []
cepList = {
            'CEP01': '07124-000',
            'CEP02': '07134-645',
            'CEP03': '07134-000'
           }
adressData = {}

navigate = seleniumOptions.Chrome()
navigate.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
timeLoad.sleep(4)

#digitando o CEP no site dos correios
for item in cepList.values():
    timeLoad.sleep(5)
    navigate.find_element(By.NAME, 'endereco').send_keys(f'{item}')
    timeLoad.sleep(2)
    navigate.find_element(By.NAME, 'btn_pesquisar').click()
    timeLoad.sleep(2)
    tableData = navigate.find_element(By.ID, 'resultado-DNEC')
    listCopy = []

    #adicionando um dicionário CEP por CEP com suas características
    adressData['Street'] = navigate.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[1]/td[1]').text
    adressData['District'] = navigate.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr[1]/td[2]').text
    adressData['City'] = navigate.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr[1]/td[3]').text
    adressData['CEP'] = navigate.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[1]/td[4]').text
    adressList.append(adressData.copy())
    timeLoad.sleep(3)
    navigate.find_element(By.XPATH, '//*[@id="btn_nbusca"]').click()
    adressToExcelList = adressData['Street'] + ';' + adressData['District'] + ';' + adressData['City'] + adressData['CEP']
    dataFrameList.append(adressToExcelList)

for adresses in adressList:
    print(adresses)

#extraindo a lista de CEPs e transformando em planilha do Excel
excelArchive = pd.ExcelWriter('correiosData.xlsx', engine='xlsxwriter')
excelArchive._save()
dataFrame = pd.DataFrame(dataFrameList, columns=['Street ; District ; City ; CEP'])
excelArchive = pd.ExcelWriter('correiosData.xlsx', engine='xlsxwriter')
dataFrame.to_excel(excelArchive, sheet_name='Correio Adress Data', index=False)
excelArchive._save()

timeLoad.sleep(10)