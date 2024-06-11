#
#  Desafio Tech - Thiago Reolon
#
#  1-fazer um crud no Python e salvar persistir os dados em uma planilha Excel
#
# necessário instalar:
# pip install pandas
# pip install openpyxl
import pandas as pd
import os

caminho = str(os.getcwd())
caminho_nome_arquivo = os.path.join(caminho, 'logins.xlsx')

def create_excel():
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    if not os.path.exists(caminho_nome_arquivo):
        df = pd.DataFrame(columns=['Login', 'Senha'])
        df.to_excel(caminho_nome_arquivo, index=False)

def insert_registro():
    login = input("Login: ")
    senha = input("Senha: ")

    df = pd.read_excel(caminho_nome_arquivo)
    registro = pd.DataFrame({
        'Login': [login],
        'Senha': [senha]
    })
    df = pd.concat([df, registro], ignore_index=True)
    df.to_excel(caminho_nome_arquivo, index=False)
    print('Dados salvos no arquivo: ', caminho_nome_arquivo)

def read_excel():
    df = pd.read_excel(caminho_nome_arquivo)
    if df.empty:
        print('Arquivo sem registros.')
    else:
        print(df)

def altera_registro():
    read_excel()
    item = int(input("Digite o número do registro que deseja alterar: "))

    df = pd.read_excel(caminho_nome_arquivo)
    if not df.empty and 0 <= item < len(df):
        login = input("Alterar Login para: ")
        senha = input("Alterar Senha para: ")

        if login:
            df.at[item, 'Login'] = login
        if senha:
            df.at[item, 'Senha'] = senha

        df.to_excel(caminho_nome_arquivo, index=False)
        print("Dados atualizados com sucesso!!")
    else:
        print("Número de registro inválido")

def deleta_registro():
    read_excel()
    item = int(input("Digite o número do registro que deseja deletar: "))

    df = pd.read_excel(caminho_nome_arquivo)
    if not df.empty and 0 <= item < len(df):
        df = df.drop(item).reset_index(drop=True)
        df.to_excel(caminho_nome_arquivo, index=False)
        print("Registro deletado: ", item)
    else:
        print("Ítem inválido: ", item)
def menu():
    create_excel()

    while True:
        print("""
            
            Menu CRUD:
            
            1 - Inserir registro
            2 - Ler registros
            3 - Atualziar registros
            4 - Deletar registros
            5 - Sair
            """)
        opcao = input("Selecione uma opção:")

        if opcao == '1':
            insert_registro()
        elif opcao == '2':
            read_excel()
        elif opcao == '3':
            altera_registro()
        elif opcao == '4':
            deleta_registro()
        elif opcao == '5':
            print("Programa finalizdo")
            break
        else:
            print("Opção inválida", opcao)


if __name__ == "__main__":
    menu()

