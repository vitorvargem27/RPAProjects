from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import pyautogui as timeLoad
import pyautogui as mouse

#perguntanoo se a pessoa tem filhos
haveKids = str(input('Are you have a kids?[\033[1:31mN\033[m]/[\033[1:32mY\033[m]\n')).strip().upper()

#perguntando a cor favorita da pessoa
favoriteColor = int(input("What's your favorite color?\n"
                          "[1] BLUE\n"
                          "[2] YELLOW\n"
                          "[3] RED\n"
                          "[4] ORANGE\n"
                          "[5] BLACK\n"
                          "[6] GREEN\n\n").strip())

while favoriteColor < 1 and favoriteColor > 6 :
    favoriteColor = int(input("What's your favorite color?\n"
                              "[1] BLUE\n"
                              "[2] YELLOW\n"
                              "[3] RED\n"
                              "[4] ORANGE\n"
                              "[5] BLACK\n"
                              "[6] GREEN\n").strip())

formsValidateStars = int(input("What's the note that you give in stars to this form? (Between 1 to 5)\n").strip())
formsValidateService = int(input("What's the note that you give in degree to this form? (Between 1 to 4)\n").strip())
formsValidateDifficulty = int(input("What's the note that you give in degree to this form? (Between 1 to 4)\n").strip())

navigate = seleniumOptions.Chrome()
navigate.get('https://www.jotform.com/221436066464051')
timeLoad.sleep(2)

navigate.find_element(By.NAME, 'q3_nome[first]').send_keys('Vitor')
timeLoad.sleep(1)
navigate.find_element(By.NAME, 'q3_nome[last]').send_keys('Vargem')
timeLoad.sleep(1)
navigate.find_element(By.NAME, 'q4_email').send_keys('teste@gmail.com')
timeLoad.sleep(2)

mouse.scroll(-400)
timeLoad.sleep(1)

#puxando a caixa de opções
optionsForSelect = navigate.find_element(By.ID, 'input_5')
selectedItem = Select(optionsForSelect)

#selecionando o item 2 à partir do seu index/indíce 2
selectedItem.select_by_index(1)
timeLoad.sleep(2)

#respondendo a caixa de filhos do formulário à partir da resposta do usuário
if haveKids == 'N' :
    timeLoad.sleep(2)
    navigate.find_element(By.ID, 'label_input_6_1').click()

else:
    timeLoad.sleep(2)
    navigate.find_element(By.ID, 'label_input_6_0').click()

timeLoad.sleep(2)
mouse.scroll(-400)
timeLoad.sleep(1)

#respondendo a caixa de cores do formulário referente a cor escolhida
if favoriteColor == 1 :
    timeLoad.sleep(1)
    navigate.find_element(By.ID, 'label_input_7_0').click()

elif favoriteColor == 2 :
    timeLoad.sleep(1)
    navigate.find_element(By.ID, 'label_input_7_1').click()

elif favoriteColor == 3 :
    timeLoad.sleep(1)
    navigate.find_element(By.ID, 'label_input_7_2').click()

elif favoriteColor == 4 :
    timeLoad.sleep(1)
    navigate.find_element(By.ID, 'label_input_7_3').click()

elif favoriteColor == 5 :
    timeLoad.sleep(1)
    navigate.find_element(By.ID, 'label_input_7_4').click()

elif favoriteColor == 6 :
    timeLoad.sleep(1)
    navigate.find_element(By.ID, 'label_input_7_5').click()

timeLoad.sleep(2)
mouse.scroll(-400)
timeLoad.sleep(1)

#marcando a nota em estrelas à partir da resposta do usuário
if formsValidateStars == 1 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[7]/div/div/div[1]').click()

elif formsValidateStars == 2 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[7]/div/div/div[2]').click()

elif formsValidateStars == 3 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[7]/div/div/div[3]').click()

elif formsValidateStars == 4 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[7]/div/div/div[4]').click()

elif formsValidateStars == 5 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[7]/div/div/div[5]').click()

timeLoad.sleep(2)

#avaliação do serviço do formulário à partir da resposta do usuário
if formsValidateService == 1 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[8]/div/table/tbody/tr[2]/td[1]/input').click()

elif formsValidateService == 2 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[8]/div/table/tbody/tr[2]/td[2]/input').click()

elif formsValidateService == 3 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[8]/div/table/tbody/tr[2]/td[3]/input').click()

elif formsValidateService == 4 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[8]/div/table/tbody/tr[2]/td[4]/input').click()

timeLoad.sleep(2)

#validação de avaliação de dificuldade à partir da resposta do usuário
if formsValidateDifficulty == 1 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH,'/html/body/form/div[1]/ul/li[8]/div/table/tbody/tr[3]/td[1]/input').click()

elif formsValidateDifficulty == 2 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH,'/html/body/form/div[1]/ul/li[8]/div/table/tbody/tr[3]/td[2]/input').click()

elif formsValidateDifficulty == 3 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH,'/html/body/form/div[1]/ul/li[8]/div/table/tbody/tr[3]/td[3]/input').click()

elif formsValidateDifficulty == 4 :
    timeLoad.sleep(1)
    navigate.find_element(By.XPATH,'/html/body/form/div[1]/ul/li[8]/div/table/tbody/tr[3]/td[4]/input').click()

timeLoad.sleep(2)
navigate.find_element(By.XPATH, '/html/body/form/div[1]/ul/li[9]/div/div/button').click()

timeLoad.sleep(10)
