from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as timeLoad
import pyautogui as mouse

personGender = str(input("What's your gender?\n[M]/[F]\n")).strip().upper()

timeLoad.sleep(2)
navigate = seleniumOptions.Chrome()
navigate.get('https://pt.surveymonkey.com/r/7GX9XRZ')
timeLoad.sleep(2)

navigate.find_element(By.NAME, '72542598').send_keys('Vitor Vargem')
timeLoad.sleep(2)
navigate.find_element(By.NAME, '72542821').send_keys('teste@gmail.com')
timeLoad.sleep(2)
mouse.scroll(-400)
timeLoad.sleep(1)

if personGender == 'F' :
    navigate.find_element(By.XPATH,'/html/body/main/article/section/form/div[1]/div[3]/div/div/fieldset/div/div/div[1]/div/label/span[2]').click()

elif personGender == 'M' :
    navigate.find_element(By.XPATH, '/html/body/main/article/section/form/div[1]/div[3]/div/div/fieldset/div/div/div[1]/div/label/span[1]').click()

timeLoad.sleep(1)
selectItem = navigate.find_element(By.NAME, '72543178')
selectedItem = Select(selectItem)
timeLoad.sleep(1)
selectedItem.select_by_index(1)

timeLoad.sleep(10)