import inputs




#3.1
def soma (n1,n2):
    return n1+n2
def divisao (n1,n2):
    return n1/n2
def subtracao (n1,n2):
    return n1 - n2
def multiplicacao (n1,n2):
    return n1 * n2





#3.2
def menu(n1,n2, ):
            print("1 - soma ")
            print("2 - divisão")
            print("3 - subtração ")
            print("4 - mutiplicação")
            print("5 - Exibir todas")
            while True:
                try:
                    n = int(input("Digite um número "))
                    break
                except ValueError:
                    print("Digite um número válido")
            if n == 1:
                print(soma(n1,n2))
            elif n == 2:
                print(divisao(n1,n2))
            elif n == 3:
                print(subtracao(n1,n2))
            elif n == 4:
                print(multiplicacao(n1,n2))
            elif n == 5:
                calculadora_basica(n1,n2)
            else:
                print("Digite um número valido por favor")
            break
while True:
    try:
        n1 = float(input("Digite um número para calcular "))
        break
    except ValueError:
        print("Digite apenas números")
while True:
    try:
        n2 = float(input("Digite um número para calcular "))
        break
    except ValueError:
        print("Digite apenas números")



menu(n1,n2)
