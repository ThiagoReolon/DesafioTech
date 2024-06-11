#
#  Desafio Tech - Thiago Reolon
#
#  3- via python realizar uma chamada de api https em algum site de testes de api e os dados obtidos salvar no Excel
#
# Necessário instalar biblioteca
# pip install requests pytest
#
import pandas as pd
import os
import requests

def get_api():
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            retorno = resposta.json()
            return retorno
        else:
            print('Erro:', resposta.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Erro:', e)
        return None

def save_to_excel(retorno):
    df = pd.DataFrame(retorno)
    df.to_excel(os.path.join(str(os.getcwd()),   'resultadoapi.xlsx'), index=False)


retorno = get_api()
if retorno:
    save_to_excel(retorno)
    print('Dados salvos com sucesso!')
else:
    print('Erro ao salvar dados.')

