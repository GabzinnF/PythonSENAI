#3
import inputs
def calculadora_basica(n1,n2):
    print("Soma:",soma(n1,n2))
    print("Divisão:",divisao(n1,n2))
    print("Subtração:",subtracao(n1,n2))
    print("Multiplicação:",multiplicacao(n1,n2))
    




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
def menu(n1,n2):
            print("1 - soma ")
            print("2 - divisão")
            print("3 - subtração ")
            print("4 - mutiplicação")
            print("5 - Exibir todas")
            n = inputs.input_int("Digite um número ")
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
                
n1 = inputs.input_float("Digite um número para calcular ", decimal=1)
n2 = inputs.input_float("Digite um número para calcular ")




menu(n1,n2)


    
    