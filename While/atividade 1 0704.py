from time import sleep
n = int(input("Digite um número,para saber seus pares "))
n1 = 0
while True:
    sleep(0.2)
    print(n)
    n -= 2
    n1 += 1
    if n < 0:
        print("Quantidade de pares é :",n1)
        break

    
    
    
    
    