#Fatiando um lista

jogadores = ["carlos", "Flinstons", "maguila", "musgo", "klevar"]
print(jogadores[0:3]) #O primeiro número é o indice inicial (a falta de um n° faz a fatia começar do inicio da lista), e o segundo numero é quantos indices serão contados (incluindo o inicial, então nesse caso foram os indices (0, 1, 2))

print(jogadores[-3:]) #Começando do final da lista com n° negativo

#percorrendo uma fatia com loop

for jogador in jogadores[0:3]:
    print(jogador.title())

#Copiando uma lista

minhas_comidas = ["pizza", "esfiha", "pastel"]
amigo_comidas = minhas_comidas[:]#Essa fatia sem atribuição faz toda lista ser atribuida a amigo_comidas. 

#Porém se uma das lista for modificada apenas a lista inicial será atribuida
minhas_comidas.append("macarrão")
amigo_comidas.append("sorvete")

print(minhas_comidas)
print(amigo_comidas)