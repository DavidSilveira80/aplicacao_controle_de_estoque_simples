from pathlib import Path
import csv

caminho = Path(__file__).parent / 'estoque.csv'
campos = ['codigo', 'nome', 'quantidade', 'preco']


def adicionar_produto(pacote_produto, caminho_arquivo, campos):
    with open(caminho_arquivo, 'a', newline='') as arquivo:
        gravador = csv.DictWriter(arquivo, fieldnames=campos)

        for produto in pacote_produto:
            gravador.writerow(produto)


def listar_produtos(caminho_arquivo):
    with open(caminho_arquivo, 'r', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            print(f'Código do produto: {linha["codigo"]} Nome: {linha["nome"]} '
                  f'Quantidade: {linha["quantidade"]} Preço unitário: {linha["preco"]}')
