def menu():
    valor_total = 0
    despesa_final = 0
    while True:
        print("Oque Deseja?")
        print("1 - Adicionar valor da despesa ")
        print("2 - Mostrar a quantidade e o valor total das despesas")
        print("0 - Sair ")
        n = int(input(""))
        if n == 0:
            print("Tchau")
            break
        elif n == 2:
            print("Você tem",despesa_final,"contas, e seu valor total é de", valor_total)
        elif n == 1:
            print("Digite o valor da despesa")
            despesa2= float(input(""))
            despesa_final += 1
            while True:
                print("Deseja adicionar outro valor? ")
                print("2 - Não ")
                print("1 - Sim")
                numero3 = int(input(""))
                if numero3 == 1:
                    print("Digite outro valor")
                    despesa = float(input(""))
                    valor_total +=  despesa+despesa2
                    despesa_final += 1 
                elif numero3 == 2:
                    break
                
menu()



        