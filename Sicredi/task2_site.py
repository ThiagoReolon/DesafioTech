#
#  Desafio Tech - Thiago Reolon
#
#  2- obter os dados de um Excel de login e senha e input em um site para realizar o login e senha
#
# é necessário que o arquivo logins.xlsx já esteja criado na pasta com logins e senhas preenchidos.
# Necessário instalar as bibliotecas:
# pip install pandas selenium openpyxl
# necessário baixar o chromedriver na versão do chrome:
# https://googlechromelabs.github.io/chrome-for-testing/#stable
# https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/win64/chromedriver-win64.zip
#
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

df = pd.read_excel(os.path.join(str(os.getcwd()), 'logins.xlsx'))

#Se Windows utilizar esse driver:
#service = Service(os.path.join(str(os.getcwd()), 'chromedriver', 'chromedriver.exe'))

#Se Linux utilizar esse driver:
service = Service(os.path.join(str(os.getcwd()), 'chromedriver', 'chromedriver'))

driver = webdriver.Chrome(service=service)

def login(login, senha):
    try:
        driver.get('https://www.fbb.org.br/pt-br/ra/conteudo/teste-login')

        campo_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'modlgn-username')))
        campo_senha = driver.find_element(By.ID, 'modlgn-passwd')
        campo_login.clear()
        campo_senha.clear()
        campo_login.send_keys(login)
        campo_senha.send_keys(senha)
        campo_senha.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="messages error"]')))
        resultado = driver.find_element(By.XPATH, '//div[@class="messages error"]').text
        return resultado

    except TimeoutException:
        return "Timeout ao tentar logar"
    except Exception as e:
        return str(e)

retornos = []
for i, linha in df.iterrows():
    loginvar = linha['Login']
    senhavar = linha['Senha']
    retorno = login(loginvar, senhavar)
    retornos.append({'Login': loginvar, 'Senha': senhavar, 'Retorno': retorno})
    time.sleep(1)

retornos_df = pd.DataFrame(retornos)
print(retornos_df)

driver.quit()

