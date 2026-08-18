#Oque é uma lista?

carros = ["fusca", "meriva", "corolla"]
print(carros)

#Acessando os elementos em uma lista

print(carros[0])
print(carros[0].upper())

#Usando somente um valor da lista

mensagem = f"Meu carro é um {carros[1].title()}"
print(mensagem)

#Modificando elementos

carros[0] = "bugatti"
print(carros)

#Anexando elementos ao final da lista

carros.append("Kwid")
print(carros)

#Inserindo elementos em uma lista

carros.insert(0, "Carroça")
print(carros)

#Removendo elementos de uma lista 
#(instrução del)

del carros[0]
print(carros)

#(Método pop())
#Remove o ultimo item da lista, o topo da pilha

carros.pop()
print(carros)

carros.pop(1) #Removi no indice 1
print(carros)

#(Método remove())
#Remove o valor desejado

carros.remove("bugatti")
print(carros)