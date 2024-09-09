from funcoes_do_sistema import (caminho, campos,
                                listar_produtos,
                                consultar_produto, le_arquivo, cadastrar, atualizar_quantidade, remover)


def main():
    parada_principal = 0
    while parada_principal == 0:
        print("==========================================")
        print("          1- Cadastrar\n"
              "          2- Listas Produtos\n"
              "          3- Atualizar Quantidade\n"
              "          4- Remover Produto\n"
              "          5- Consultar Produto\n"
              "          6- Sair                         ")
        opt1 = int(input('-> '))

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
