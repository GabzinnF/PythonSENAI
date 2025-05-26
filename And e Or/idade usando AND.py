dn1 = int(input("Solicite um ano de nascimento "))
nt = int(input("Digite o ano atual "))

r = nt - dn1


if r < 10:
    print("criança")
elif r >= 11 and r <= 17:
    print("adolescente")
elif r >= 18 and r <= 59:
    print("adulto")
elif r > 60 and r <= 116:
    print("Idoso")
else:
    print("Parabens, você é a pessoa mais velha do mundo")