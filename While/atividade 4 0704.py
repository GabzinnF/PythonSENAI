from time import sleep
def menu():
    while True:
        print("Deseja fazer mais algo?")
        print("1 - Fatorial ")
        print("2 - Quadrado")
        print("3 - Cubo ")
        print("4 - Tabuada")
        print("0 -  Sair")
        n = int(input("Escolha um número "))
        if n == 1:
            i = int(input("Escolha um número que deseja para descobrir a fatoração "))
            resultado = 1
            fatorial= 1
            while fatorial <= i:
              resultado *= fatorial
              fatorial += 1
            print( resultado)
        elif n == 2:
            n1 = int(input("Escolha um número que deseja para elevar ao quadrado "))
            print(n1*n1)
        elif n == 3:
            n1 = int(input("Escolha um número que deseja para elevar ao cubo "))
            print(n1*n1*n1)
        elif n == 4:
            n1 = int(input("Escolha um número que deseja para descobrir a tabuada "))
            print(n1, 'x 1 =', n1*1)
            sleep(0.5)
            print(n1, 'x 2 =', n1*2)
            sleep(0.5)
            print(n1, 'x 3 =', n1*3)
            sleep(0.5)
            print(n1, 'x 4 =', n1*4)
            sleep(0.5)
            print(n1, 'x 5 =', n1*5)
            sleep(0.5)
            print(n1, 'x 6 =', n1*6)
            sleep(0.5)
            print(n1, 'x 7 =', n1*7)
            sleep(0.5)
            print(n1, 'x 8 =', n1*8)
            sleep(0.5)
            print(n1, 'x 9 =', n1*9)
            sleep(0.5)
            print(n1, 'x 10 =', n1*10)
            sleep(0.5)
        elif n == 0:
            break
        
                
                
                
                
                
            
                
menu()
        
            
    