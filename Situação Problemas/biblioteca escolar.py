import inputs

listas=[]



while True:
    print("")
    print("1- Adicionar livro")
    print("2- Exibir dados do livro")
    print("3- Exibir a quantidade de livros")
    print("4- Buscar livro categoria")
    print("5- Buscar livro autor")
    print("6- Editar dados de um livro")
    print("7- Sair")
    print("Oque deseja fazer?")
    n = inputs.input_int("Digite sua escolha ")
    if n == 1:
        isbn = inputs.input_int("Digite o isbn do seu livro ")
        nome = inputs.input_str("Digite o nome do livro ")
        autor = inputs.input_str("Digite o autor do livro ")
        categoria = inputs.input_str("Digite a categoria do livro ")
        ano = inputs.input_int("Digite o ano de fabricação")
        
        listas.append({
            "isbn" : isbn,
            "nome" : nome,
            "autor" : autor,
            "categoria" : categoria,
            "ano" : ano
        })
        print("Livro Cadastrado")
    elif n == 2:
        for livro in listas:
            for chave, valor in livro.items():
                print(f"{chave} = {valor}")
    elif n == 3:
        quantidade = len(listas)
        print("Livros cadastrados:",quantidade)
    elif n == 4:
        n2 = inputs.input_str("Digite a categoria ")
        for livro in listas:
            if livro["categoria"] == n2:
                for chave, valor in livro.items():
                    print(f"{chave} = {valor}")
    elif n == 5:
        n2 = inputs.input_str("Digite o autor ")
        for livro in listas:
            if livro["autor"] == n2:
                for chave, valor in livro.items():
                    print(f"{chave} = {valor}")
                
    elif n == 6:
        editar= inputs.input_int("Digite o isbn do livro ")
        for livro in listas:
            if livro["isbn"] == editar:
                print("livro encontrado, faça suas alterações")
                livro["nome"] = inputs.input.str("Digite um novo nome ")
                livro["autor"] = inputs.input_str("Digite o nome do autor ")
                livro["categoria"] = inputs.input_str("Digite a categoria ")
                livro["ano"] = inputs.input_int("Digite o ano de fabricação")
                print("alteração feita")
                break
    elif n == 7:
        break
            