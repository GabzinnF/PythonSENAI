import random
def saco():
    print("Seja Bem-Vindo ao jogo Ímpar ou Par")
    print("Escolha oque deseja ser")
    print("1- Par")
    print("2- Ímpar")
    n = int(input(""))
    if n == 1:
        print("Você será número Par então")
        
    elif n == 2:
        print("Você será número Ímpar então")
        
    print("Por favor, digite seu número e BOA SORTE")
    n_jogador = int(input(""))
    n_robo = random.randint(1, 10)
    print("Seu inimigo escolheu o número",n_robo)
    n_total = n_robo + n_jogador
    escolha = n_total % 2 == 0
    if n == 1:
        if escolha:
            print("Você ganhou, deseja jogar denovo?")
        else:
            print("Você perdeu, deseja jogar denovo?")
    if n == 2:
        if escolha:
            print("Você perdeu, deseja jogar denovo?")
        else:
            print("Seu inimigo ganhou, deseja jogar denovo?")
    print("1- Sim")
    print("2- Não")
    n2 = int(input(""))
    if n2 == 1:
        saco()
    elif n2 == 2:
        print("Adeus")
            
saco()
    


