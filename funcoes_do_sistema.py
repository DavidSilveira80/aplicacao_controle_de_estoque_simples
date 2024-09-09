from pathlib import Path
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


def listar_produtos(produtos):
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
                nova_quantidade = int(produto['quantidade']) + int(quantidade)
            elif operacao == '-':
                nova_quantidade = int(produto['quantidade']) - int(quantidade)
            produto['quantidade'] = str(nova_quantidade)
            break

    grava_produtos(produtos, caminho, campos)


def empacota_produto(codigo, nome, quantidade, preco):
    return [{'codigo': codigo, 'nome': nome, 'quantidade': quantidade, 'preco': preco}]


def cadastrar():
    op_loop = 1
    while op_loop == 1:
        cod = input("Informe o código do produto: ")
        nome = input("Informe o nome do produto: ")
        quantidade = input("Informe a quantidade do produto: ")
        preco = input("Informe o preço do produto: ")
        if verifica_se_ha_no_estoque(caminho=caminho, codigo_produto=cod):
            print('Produto já cadastrado.')
        else:
            pacote = empacota_produto(codigo=cod, nome=nome, quantidade=quantidade, preco=preco)
            adicionar_produto(pacote_produto=pacote, caminho_arquivo=caminho, campos=campos)
            print('Produto adicionado ao estoque.')
            op_loop = int(input('Adicionar outro produto: 1- Sim 2- Não: '))


def atualizar_quantidade(caminho, campos):
    cod = input("Informe o código do produto: ")
    if verifica_se_ha_no_estoque(caminho=caminho, codigo_produto=cod):
        oper = input('Informe a operação: -/+\n-> ')
        quantidade = input('Quantidade: ')
        atualizar_quantidade_produto(codigo_produto=cod, operacao=oper, quantidade=quantidade, caminho=caminho,
                                     campos=campos)
    else:
        print('Produto não cadastrado')

def remover(caminho, campos):
    cod = input("Informe o código do produto: ")
    if verifica_se_ha_no_estoque(caminho=caminho, codigo_produto=cod):
        remover_produto_pelo_codigo(codigo_produto=cod, caminho_arquivo=caminho, campos=campos)
        print('Produto removido com sucesso.')
    else:
        print('Produto não cadastrado.')



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
