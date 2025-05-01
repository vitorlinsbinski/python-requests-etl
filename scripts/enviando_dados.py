from manipula_repos import ManipulaRepositorios
import os

novo_repo = ManipulaRepositorios('vitorlinsbinski')

nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

caminho_dados = './dados'
arquivos = [arquivo for arquivo in os.listdir(caminho_dados) if arquivo.endswith('.csv')]

for arquivo in arquivos:
    novo_repo.add_arquivo(nome_repo, arquivo, f'{caminho_dados}/{arquivo}')

