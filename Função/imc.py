def imc (peso,altura):
    return peso / altura**2
def tabela_imc (imc):
    if imc < 18.5:
        print("Magreza")
    elif imc >= 18.5 and imc <=24.9:
        print("Normal")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        print("Obesidade grau 1")
    elif imc >= 35 and imc <= 39.9:
        print("Obesidade grau 2")
    else:
        print("Obesidade grau 3")
        
altura= float(input("Digite sua altura "))
peso= int(input("Digite o seu peso "))
imc= (imc(peso,altura))     
tabela_imc(imc)
