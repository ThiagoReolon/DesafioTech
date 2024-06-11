# DesafioTech
Desafios Técnicos - Thiago Reolon


# Descrição do Projeto = **"task1-crud.py"**

Este projeto consiste em um programa Python que implementa um CRUD (Create, Read, Update, Delete) utilizando uma planilha Excel para armazenar e persistir os dados de logins e senhas. Ele permite inserir novos registros, ler os registros existentes, atualizar informações de login e senha, além de excluir registros.


Requisitos
Python 3.x
Bibliotecas: pandas, openpyxl
Como Usar
Instale as dependências executando os seguintes comandos:

`pip install pandas openpyxl`

`python task1-crud.py`



Siga as opções do menu para interagir com o programa:

```python
1 - Inserir registro
2 - Ler registros
3 - Atualizar registros
4 - Deletar registros
5 - Sair
```



**Exemplo de Uso**

Para inserir um novo registro, selecione a opção 1 no menu e siga as instruções para inserir o login e senha.

Para ler os registros existentes, selecione a opção 2.

Para atualizar um registro, selecione a opção 3, escolha o número do registro que deseja atualizar e insira as novas informações de login e senha.

Para deletar um registro, selecione a opção 4, escolha o número do registro que deseja deletar.

Para sair do programa, selecione a opção 5.



> [!Observações]
Certifique-se de ter as permissões adequadas para escrita no sistema de arquivos, especialmente ao salvar ou criar arquivos Excel.
Os arquivos Excel são salvos no diretório do projeto com o nome logins.xlsx.



-------------------------------------------------------------------------------------------------------------------------------------


# Descrição do Projeto = **"task2_site.py"**


Objetivo
Este script em Python foi desenvolvido como parte de um desafio técnico. O objetivo é realizar o login em um site utilizando dados de login e senha armazenados em um arquivo Excel.


Requisitos:
Python 3.x
Bibliotecas: pandas, selenium, openpyxl
ChromeDriver (para automação do Chrome)


Como Usar
Instale as dependências necessárias executando o seguinte comando:

`pip install pandas selenium openpyxl`

`python task2_site.py`


Baixe o ChromeDriver compatível com a versão do seu navegador Chrome:
[Download do ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable)

Coloque o ChromeDriver na mesma pasta do script ou defina o caminho correto para o ChromeDriver na variável service.


Certifique-se de ter um arquivo Excel chamado logins.xlsx na mesma pasta do script. Este arquivo deve conter os dados de login e senha.



Execute o script Python.

O script realiza o seguinte:

Carrega os dados de login e senha do arquivo Excel logins.xlsx utilizando a biblioteca pandas.

Utiliza a biblioteca selenium para automatizar o navegador Chrome.

Realiza o login em um site específico (no exemplo fornecido, o site é https://www.fbb.org.br/pt-br/ra/conteudo/teste-login) usando os dados fornecidos no arquivo Excel.

Captura e exibe os retornos de login (como mensagens de erro) para cada conjunto de login e senha.

Fecha o navegador Chrome após a conclusão do processo.




> [!Observações] 
Certifique-se de que o ChromeDriver esteja na mesma pasta do script ou defina o caminho correto na variável service.
O arquivo Excel logins.xlsx deve estar corretamente preenchido com os dados de login e senha.
O site utilizado para o login é apenas um exemplo. Substitua-o pelo site desejado no código conforme necessário.




--------------------------------------------------------------------------------------------------------------------

# Descrição do Projeto = **"task3_api.py"**



Descrição
Este projeto realiza uma chamada a uma API HTTPS de um site de testes e salva os dados obtidos em um arquivo Excel.


Requisitos:
Python 3.x
Bibliotecas:
requests
pandas
Instalação
Para instalar as bibliotecas necessárias, execute o seguinte comando:

`pip install requests pandas`

`python task3_api.py`

Clone este repositório para sua máquina local.
Execute o script api_to_excel.py:

python api_to_excel.py
Estrutura do Código
Funções
`get_api()`
Esta função realiza uma chamada GET para a URL da API e retorna os dados em formato JSON se a resposta for bem-sucedida (código de status 200). Caso contrário, imprime uma mensagem de erro e retorna None.

```python
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
save_to_excel(retorno)
```
Esta função recebe os dados retornados pela função get_api(), converte-os para um DataFrame do pandas e salva em um arquivo Excel chamado resultadoapi.xlsx no diretório atual.

```python
def save_to_excel(retorno):
    df = pd.DataFrame(retorno)
    df.to_excel(os.path.join(str(os.getcwd()), 'resultadoapi.xlsx'), index=False)

```
Execução Principal
O código principal executa a função get_api() e, se os dados forem obtidos com sucesso, chama a função save_to_excel() para salvar os dados em um arquivo Excel. Caso contrário, imprime uma mensagem de erro.

```python
retorno = get_api()
if retorno:
    save_to_excel(retorno)
    print('Dados salvos com sucesso!')
else:
    print('Erro ao salvar dados.')
```


