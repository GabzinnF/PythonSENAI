import inputs
listas= []
listas2 = []
listas3 = []
while True:
    print("Reunião de pais")
    print("1- Cadastrar nomes")
    print("2- Exibir total de pais")
    print("3- Lista de nomes em ordem alfabética")
    print("4- Confirmação de presença dos pais")
    print("5- Relatório de chamada")
    op = inputs.input_int("Digite um número")
    if op == 1:
        nm = inputs.input_str("Digite seu nome")
        if nm in listas:
            print("este nome ja está na lista")
        else:
            listas.append(nm)
    if op == 2:
        pais = len(listas)
        print("Quantidade de nomes:", pais)
    if op == 3:
        for od in sorted(listas):
            print(od)
    if op == 4:
        for nm in listas:
            print(nm)
            print("está presente?")
            print("1- Sim")
            print("2- Não")
            ps = inputs.input_int("Digite um número")
            if ps == 1:
                listas3.append(nm)
            else:
                listas2.append(nm)
    if op == 5:
        print("Ausentes")
        for ausen in sorted(listas3):
            print(ausen)
        print("Presentes")
        for ps in sorted(listas2):
            print(ps)
                
