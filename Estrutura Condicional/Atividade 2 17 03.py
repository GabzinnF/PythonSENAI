n1 = int(input("Solicite um numero"))
n2 = int(input("Solicite um numero"))

m= n1 + n2 / 2
media = 70

resposta = ""

if m >= media:
    resposta = "aprovado"

elif m < media:
    resposta = "reprovado"

print(resposta)
    
