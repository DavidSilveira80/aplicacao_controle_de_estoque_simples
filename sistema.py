

opt1 = int(input('1 - C 2 - L 3 - A 4 - R 5 - CON 6 - S\n-> '))

match opt1:
    case 1:
        print("Cadastrar Produtos")
    case 2:
        print("Listar Produtos")
    case 3:
        print("Atualizar Produto")
    case 4:
        print("Remover Produto")
    case 5:
        print("Consultar Produto")
    case 6:
        print("Sair")
    case _:
        print("Valor Inválido")
