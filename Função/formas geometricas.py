def area_circulo (raio):
    pi= 3.14
    return pi * raio**2
   
def area_quadrado (lado):
    return lado**2
def area_retangulo (base,altura):
    retangulo= altura * base
    return retangulo
def area_triangulo (lado_tri):
    return ((lado_tri**2) * (3**0.5)) / 4
def area_hexagono (lado_tri):
    return area_triangulo(lado_tri) * 6
    
def tabela_area ():
    print("1 - area do circulo ")         
    print("2 - area do quadrado")
    print("3 - area do retangulo ")
    print("4 - area do triangulo ")
    print("5 - area do hexagono ")

    n = int(input("Digite o número "))
    if n == 1:
        raio= int(input("Digite o raio do circulo "))
        print(area_circulo(raio))
    elif n == 2:
        lado= int(input("Digite o lado do quadrado "))
        print(area_quadrado(lado))
    elif n == 3:
        base = int(input("Digite a base do retangulo "))
        altura= int(input("Digite a altura do retangulo "))
        print(area_retangulo(base,altura))
    elif n == 6:
        raio= int(input("Digite o raio do circulo "))
        print(area_circulo(raio))
        lado= int(input("Digite o lado do quadrado "))
        print(area_quadrado(lado))
        base = int(input("Digite a base do retangulo "))
        altura= int(input("Digite a altura do retangulo "))
        print(area_retangulo(base,altura))
    elif n == 4:
        lado_tri= int(input("Digite o lado do triangulo "))
        print(area_triangulo(lado_tri))
    elif n == 5:
        lado_hexa= int(input("Digite o lado do hexagono "))
        print(area_hexagono(lado_hexa))

def perimetro_cir (raio):
    pi = 3.14
    return (pi * 2) * raio
def perimetro_quadra (lado):
    return lado * 4
def perimetro_retan (lado2):
    return lado2 * 4
def perimetro_trian (ladot):
    return ladot * 3
def perimetro_hexa (ladoh):
    return ladoh * 6
def tabela_perimetro ():
    print("1 - perimetro do circulo ")         
    print("2 - perimetro do quadrado")
    print("3 - perimetro do retangulo ")
    print("4 - perimetro do triangulo ")
    print("5 - perimetro  do hexagono ")
    n1 = int(input("Digite o número "))
    if n1 == 1:
        raio= int(input("Digite o raio do circulo "))
        print(perimetro_cir(raio))
    elif n1 == 2:
        lado= int(input("Digite o lado do quadrado "))
        print(perimetro_quadra(lado))
    elif n1 == 3:
        lado2= int(input("Digite o lado do retangulo"))
        print(perimetro_retan(lado2))
    elif n1 == 4:
        ladot = int(input("Digite outro lado do triangulo"))
        print(perimetro_trian(ladot))
    elif n1 == 5:
        ladoh= int(input("Digite o lado do hexagono "))
        print(perimetro_hexa (ladoh))
        
print("1 - Calcular área")
print("2 - Calcular perimetro")
n2 = int(input("Digite o número "))

if n2 == 1:
    tabela_area()
elif n2 == 2:
    tabela_perimetro()















    
    



