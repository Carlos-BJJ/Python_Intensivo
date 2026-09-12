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
 
prompt = "\nDiga qualquer coisa, que eu repetirei para você"
prompt += "\nEscreva 'quit' para encerrar o programa"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#Usando break

cidade = "\nEscolha um lugar que vc já visitou"
cidade += "\nDigite 'sair' para encerrar"

while True:
    mensagem = input(cidade)

    if mensagem == "sair":
        break
    else:
        print(mensagem)

#Usando continue

num = 0

while num < 10:
    num += 1
    if num % 2 == 0:
        continue #Essa instrução faz com que o python volte para o inicio do loop ignorando oque vem adiante (Então esse loop ignorará os nums pares).

    print(num)