#1- Criar uma lista com 5 elementos
listas=['maça','uva','banana','damasco','pera']
print(listas)

#2 - Adicionar um elemeto
listas.append("mamão")
print(listas)

#3 - Acessar o objeto da posição 2 e exibir
obj = listas[1]
print(obj)

#4- Remova um objeto e exiba-o
obj1 = listas.pop(2)
print(obj1)

#5 - Exiba o tamanho da lista
obj2 = len(listas)
print(obj2)

#6 - mostrar os itens com o FOR
for lista in listas:
    print(lista)
    
#7 - verificar se 'cadeira' esta na lista, se sim remover se n adicionar
if "cadeira" in lista:
    listas.remove("cadeira")
else:
    listas.append("cadeira")
    
#8 - lista em ordem alfabética e exibir o antes e depois
print(listas)
listas.sort()
print(listas)

#9 - exibir o primeiro e ultimo número
obj4 = listas[0]
obj5 = listas[len(listas)-1]
print(obj4)
print(obj5)

#10 - limpar a lista
listas.clear()