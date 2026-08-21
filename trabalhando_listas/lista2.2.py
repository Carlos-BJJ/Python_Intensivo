#Fatiando um lista

jogadores = ["carlos", "Flinstons", "maguila", "musgo", "klevar"]
print(jogadores[0:3]) #O primeiro número é o indice inicial (a falta de um n° faz a fatia começar do inicio da lista), e o segundo numero é quantos indices serão contados (incluindo o inicial, então nesse caso foram os indices (0, 1, 2))

print(jogadores[-3:]) #Começando do final da lista com n° negativo

#percorrendo uma fatia com loop

for jogador in jogadores[0:3]:
    print(jogador.title())

