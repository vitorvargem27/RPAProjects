from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
import pyautogui as timeLoad
import pandas as pd

adressList = []
adress = {}

navigate = seleniumOptions.Chrome()
navigate.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
timeLoad.sleep(4)

#digitando o CEP no site dos correios
navigate.find_element(By.NAME, 'endereco').send_keys('07124000')
timeLoad.sleep(2)

navigate.find_element(By.NAME, 'btn_pesquisar').click()
timeLoad.sleep(2)

tableData = navigate.find_element(By.ID, 'resultado-DNEC')
adress['Street'] = navigate.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[3]/td[1]').text
adress['District'] = navigate.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[3]/td[2]').text
adress['City'] = navigate.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[3]/td[3]').text
adress['Cep'] = navigate.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[3]/td[4]').text

adressList.append(adress.copy())

for key, value in adress.items() :
    print(f'{key} : {value}')

timeLoad.sleep(10)