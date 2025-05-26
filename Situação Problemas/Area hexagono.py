l = int(input("Lado do triângulo"))
l2 = l * l
r = 3 ** 0.5
l3 = l2 * r
at = round(l3 / 4, 2)
print("Vamos descobrir a área do triangulo equilatero")

print ("A área do triangulo equilatero é ", at)
print("Agora vamos descobrir a área do hexagono")

h = 6

print("A área do hexagono é", at * h)
print("Parabens")