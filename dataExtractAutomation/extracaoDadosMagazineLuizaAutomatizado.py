import pyautogui as mouse
import pyautogui as action
import pyautogui as keyboard
import pyautogui as timeLoad
from selenium import webdriver as webAction
from selenium.webdriver.common.by import By

#acessando o site da magazine luiza
navigate = webAction.Chrome()
navigate.get('https://www.magazineluiza.com.br/')
mouse.click(1468, 35)
timeLoad.sleep(2)

#procurando na barra de pesquisas por geladeiras
navigate.find_element(By.ID,'input-search').send_keys('geladeira')
timeLoad.sleep(2)
keyboard.press('enter')

productsList = navigate.find_elements(By.CLASS_NAME, 'eJDyHN')

#loop para puxar o nome de cada geladeira da lista
for item in productsList :
    productName = ''
    productPrice = ''
    productUrl = ''

    if productName == '' :
        try:
            productName = item.find_element(By.CLASS_NAME, 'uaEbk').text
        except Exception :
            pass

    elif productName == '' :
        try:
            productName = item.find_element(By.CLASS_NAME, 'sc-eWzREE').text
        except Exception :
            pass

    print(productName)

timeLoad.sleep(10)

