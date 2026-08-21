#Usando loop

magicos = ["MisterM", "TruqueDeMestre", "MrBean"]

for magico in magicos:
    print(f"O {magico.title()} é um otário")

#Lista númerica

for valor in range(1, 6):
    print(valor)

numeros = list(range(1, 6))#criando a lista númerica
print(numeros)

numeros_pares = list(range(2, 11 ,2))#O terceiro argumento (2) serve como marca passo, ou seja, o primeiro número será pulado de 2 em 2 até ultrapassar 11
print(numeros_pares)

nums_quadrados = []
for nums in list(range(1, 11)):
    nums_quadrados.append(nums ** 2)

print(nums_quadrados)

#Estatística simples com uma lista de números

digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digitos)) #O valor minino da lista
print(sum(digitos)) #A soma dos valores da lista
print(max(digitos)) #O valor máximo da lista

#list comprehensions/ lista comprimida

quadrados = [val **2 for val in range(1, 11)]
print(quadrados)


