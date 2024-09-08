from funcoes_do_sistema import (adicionar_produto, verifica_se_ha_no_estoque, caminho, campos,
                                listar_produtos, atualizar_quantidade_produto, remover_produto_pelo_codigo,
                                consultar_produto, le_arquivo)


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


def main():
    parada_principal = 0
    while parada_principal == 0:
        opt1 = int(input('1 - C 2 - L 3 - A 4 - R 5 - CON 6 - S\n-> '))

        match opt1:
            case 1:
                print("Cadastrar Produtos")
                cadastrar()
            case 2:
                print("Listar Produtos")
                produtos = le_arquivo(caminho_arquivo=caminho)
                listar_produtos(produtos)
            case 3:
                print("Atualizar Produto")
                atualizar_quantidade(caminho=caminho, campos=campos)
            case 4:
                print("Remover Produto")
                remover(caminho=caminho, campos=campos)
            case 5:
                print("Consultar Produto")
                print(consultar_produto(caminho=caminho))
            case 6:
                print("Sair")
                parada_principal = 1
            case _:
                print("Valor Inválido")


if __name__=='__main__':
    main()
