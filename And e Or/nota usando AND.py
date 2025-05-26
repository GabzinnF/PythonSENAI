n1 = int(input("Solicite uma nota"))
n2 = int(input("Solicite uma nota"))
m = n1 + n2 / 2
if n1 > 0 and n1 <= 100 and n2 > 0 and n2 <= 100:
    if m >= 70:
        print("Aprovado")
    elif m >= 50 and m <= 70:
        print("Recuperação")
    elif m < 50:
        print("Reprovado")
else:
    print("Digite de um número de 0 a 100")
