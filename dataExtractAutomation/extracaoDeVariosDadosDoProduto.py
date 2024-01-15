import pyautogui as mouse
import pyautogui as action
import pyautogui as keyboard
import pyautogui as timeLoad
from selenium import webdriver as webAction
from selenium.webdriver.common.by import By
import pandas as pd

navigate = webAction.Chrome()
navigate.get('https://www.magazineluiza.com.br/')
mouse.click(1468, 35)
timeLoad.sleep(2)

navigate.find_element(By.ID,'input-search').send_keys('geladeira')
timeLoad.sleep(2)
keyboard.press('enter')
timeLoad.sleep(15)

productsList = navigate.find_elements(By.CLASS_NAME, 'ciMFyT')

dataList = []
dataFrameList = []
itemNumber = 1

for item in productsList :
    productData = {
        'code': itemNumber,
        'productName': '',
        'productPrice': '',
        'productUrl': ''
    }

    #verificando o nome do produto
    if productData['productName'] == '' :
        try:
            productData['productName'] = item.find_element(By.CLASS_NAME, 'ehjgcW').text
        except Exception :
            pass

    elif productData['productName'] == '' :
        try:
            productData['productName'] = item.find_element(By.CLASS_NAME, 'sc-fvwjDU').text
        except Exception :
            pass

    #verificando se o preço do produto ficou nulo para mudar o valor
    if productData['productPrice'] == '' :
        try:
            productData['productPrice'] = item.find_element(By.CLASS_NAME, 'dOwMgM').text
        except Exception :
            pass

    elif productData['productPrice'] == '' :
        try :
            productData['productPrice'] = item.find_element(By.CLASS_NAME, 'sc-bOhtcR').text
        except Exception :
            pass

    elif productData['productPrice'] == '' :
        try :
            productData['productPrice'] = item.find_element(By.CLASS_NAME, 'eCPtRw').text
        except Exception :
            pass

    elif productData['productPrice'] == '' :
        try :
            productData['productPrice'] = item.find_element(By.CLASS_NAME, 'sc-kpDqfm').text
        except Exception :
            pass

    else :
        productData['productPrice'] = 0

    #verificando se a url do produto ficou nulo
    if productData['productUrl'] == '' :
        try:
            #o get_attribute serve para puxar o complemento da tag
            productData['productUrl'] = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except Exception :
            pass

    else :
        productData['productUrl'] = '-'

    '''print(productData['productName'], "->", productData['productPrice'])
    print(productData['productUrl'])'''
    #adicionando uma cópia de cada produto para a lista de itens
    dataList.append(productData.copy())
    itemNumber += 1

    #criando uma linha com os dados para adicionar no Excel
    linesData = productData['productName'] + " ; " + productData['productPrice'] + " ; " + productData['productUrl']
    dataFrameList.append(linesData)


#Gerando um arquivo excel à partir dos produtos puxados
excelArchive = pd.ExcelWriter('magazineDataSheet.xlsx', engine='xlsxwriter')
excelArchive._save()
dataFrame = pd.DataFrame(dataFrameList, columns = ['Name ; Price ; URL'])
excelArchive = pd.ExcelWriter('magazineDataSheet.xlsx', engine='xlsxwriter')
dataFrame.to_excel(excelArchive, sheet_name='Dados', index=False)
excelArchive._save()

timeLoad.sleep(10)