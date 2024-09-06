from pathlib import Path
from funcoes_auxiliares import operacao_soma, operacao_subtracao
import csv


caminho = Path(__file__).parent / 'estoque.csv'
campos = ['codigo', 'nome', 'quantidade', 'preco']


def verifica_se_ha_no_estoque(caminho, codigo_produto):
    produtos = le_arquivo(caminho_arquivo=caminho)
    resp = False
    for produto in produtos:
        if produto['codigo'] == codigo_produto:
            resp = True
            break
    return resp


def le_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        produtos = list(leitor)
        return produtos


def grava_produtos(produtos, caminho, campos):
    with open(caminho, 'w', newline='') as arquivo:
        gravador = csv.DictWriter(arquivo, fieldnames=campos)
        gravador.writeheader()
        gravador.writerows(produtos)


def adicionar_produto(pacote_produto, caminho_arquivo, campos):
    with open(caminho_arquivo, 'a', newline='') as arquivo:
        gravador = csv.DictWriter(arquivo, fieldnames=campos)

        for produto in pacote_produto:
            gravador.writerow(produto)


def listar_produtos(caminho_arquivo):
    produtos = le_arquivo(caminho_arquivo)

    for produto in produtos:
        print(f'Código do produto: {produto["codigo"]} Nome: {produto["nome"]} '
            f'Quantidade: {produto["quantidade"]} Preço unitário: {produto["preco"]}')


def remover_produto_pelo_codigo(codigo_produto, caminho_arquivo, campos):
    produtos = le_arquivo(caminho_arquivo)
    for produto in produtos:
        if produto['codigo'] == codigo_produto:
            produtos.remove(produto)
            break

    grava_produtos(produtos, caminho, campos)


def atualizar_quantidade_produto(codigo_produto, operacao, quantidade, caminho, campos):
    produtos = le_arquivo(caminho)

    for produto in produtos:
        if produto['codigo'] == codigo_produto:
            if operacao == '+':
                nova_quantidade = operacao_soma(int(produto['quantidade']), int(quantidade))
            elif operacao == '-':
                nova_quantidade = operacao_subtracao(int(produto['quantidade']), int(quantidade))
            produto['quantidade'] = str(nova_quantidade)
            break

    grava_produtos(produtos, caminho, campos)


def consultar_produto(caminho):
    prod = ''
    cod = input("Informe o código do produto: ")
    if verifica_se_ha_no_estoque(caminho=caminho, codigo_produto=cod):
        produtos = le_arquivo(caminho_arquivo=caminho)
        for produto in produtos:
            if produto['codigo'] == cod:
                prod = produto
                break
        return prod
    else:
        print('Produto não cadastrado')
