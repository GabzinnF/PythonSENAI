p = int(input("Solicite seu peso em kg "))
a = float(input("Solicite sua altura em metros "))
imc1 = a * a
imc2 = p / imc1

if imc2 < 18.5:
    print("Magreza ")
elif imc2 >= 18.5 and imc2 <= 24.9:
    print("Normal ")
elif imc2 >= 25 and imc2 <= 29.9:
    print("Sobrepeso ")
elif imc2 >= 30 and imc2 <= 34.9:
    print("Obesidade grau 1")
elif imc2 >= 35 and imc2 <= 39.9:
    print("Obesidade grau 2")
elif imc2 > 40:
    print("Obesidade grau 3")