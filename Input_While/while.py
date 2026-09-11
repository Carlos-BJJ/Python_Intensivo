#Usando o loop while

num = 1
lista = []
while num <= 5:
    lista.append(num)
    num += 1

print(lista)

#Usuario encerrando o programa
print("Digite qualquer coisa para continuar")
print("Digite 'sair' se quiser sair")
resp = " "
while resp != "sair":
    resp = input("Digite: ")
    if resp != "sair": #Uso a estrutura if para não exibir o 'sair' no terminal
        print(resp)

#Usando flags

