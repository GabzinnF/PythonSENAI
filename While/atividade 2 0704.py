from time import sleep
n = int(input("Digite um número,para saber seus pares "))
n1 = 0
while True:
    sleep(0.5)
    print("Par",n)
    n -= 2
    n1 += 1
    if n < 0:
        sleep(0.5)
        break
print("Deseja saber a quantidade de pares o número tem? ")
print("1 - sim ")
print("2 - não")
f = int(input("Escolha um número "))
def oi (f,n1):
    if f == 1:
        print("Quantidade de pares é:",n1)
    elif f == 2:
        print("Ok :(")
    else:
        print("Por favor,Escolha um número válido")



        
oi(f,n1)