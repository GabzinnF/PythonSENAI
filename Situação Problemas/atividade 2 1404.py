import random
n_robo = random.randint(0,100)
print("Seja Bem-Vindo")
print("Regras do jogo:")
print("\033[1;31mTentar adivinhar o número que o jogo irá escolher\033[m")
print("Digite um número e te direi se é maior ou menor ao que escolhi")
while True:
    n = int(input(""))
    if n_robo > n:
        print("Seu chute ta menor")
    elif n_robo < n:
        print("Seu chute ta maior")
    elif n == n_robo:
        print("\033[1;32mVocê acertou, Parabens")
        print("Deseja prosseguir para uma próxima rodada?")
        print("1- Sim")
        print("2- Não\033[m")
        n2 = int(input(""))
        if n2 == 1:
            print("Vamos recomeçar então")
            print("Seja Bem-Vindo")
            print("Regras do jogo:")
            print("\033[1;31mTentar adivinhar o número que o jogo irá escolher\033[m")
            print("Digite um número e te direi se é maior ou menor ao que escolhi")
            n_robo = random.randint(0,100)
        elif n2 == 2:
            print("Adeus então")
            break 
