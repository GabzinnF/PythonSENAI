print("Operações Matemáticas")
print("[1] - Adição")
print("[2] - Subtração")
print("[3] - Multiplicação")
print("[4] - divisão")
op1 = int(input("Solicite uma operação " ))




num1 = int(input("Solicite um número "))
num2 = int(input("Solicite um número "))



if op1 == 1:
    print(num1 + num2)
elif op1 == 2:
    print(num1 - num2)
elif op1 == 3:
    print(num1 * num2)
elif op1 == 4:
    print(num1 / num2)
else:
    print("Erro")


        