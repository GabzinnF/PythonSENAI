import inputs
listas=[]

while True:
    print("1- Cadastrar nome")
    print("2- Exibir total de inscritos")
    print("3- Exibir a lista de nomes em ordem alfabética")
    print("4- Consultar um nome")
    op = inputs.input_int("Digite um número ")
    if op == 1:
        nm = inputs.input_str("Digite seu nome ")
        if nm in listas:
            print("seu nome ja está na lista")
        else:
            listas.append(nm)
            print("Nome Cadastrado")
    if op == 2:
        ttl = len(listas)
        print("Total de inscritos:",ttl)
    if op == 3:
        for lista in sorted(listas):
            print("Ordem alfabética: ",lista)
    if op ==4:
        vr = inputs.input_str()
        if vr in listas:
            print("Nome encontrado")
            print("Deeja remover?")
            print("1- Sim")
            print("2- Não")
            rt = inputs.input_int("Digite um número ")
            if rt == 1:
                listas.remove(vr)
                print("Nome removido")
            else:
                print("Sessão finalizada")
        else:
            print("Nome não encontrado")
            print("Deseja adicionar?")
            print("1- Sim")
            print("2- Não")
            ad = inputs.input_int("Digite um número ")
            if ad == 1:
                print("Nome adicionado")
            else:
                print("sessão encerrada")
