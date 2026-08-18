#Alterando letras maiúsculas e minúsculas em string com métodos

nome = "carLos eduArdo"
print(nome.title())
print(nome.upper())
print(nome.lower())

#Usando variaveis em strings

first_name = "maluco"
last_name = "beleza"
full_name = f"{first_name.title()} {last_name.title()}"
print(full_name)

#Adicionando espaço em branco a strings com tabs ou quebra de linhas

print("\npython\n") #Quebra de linha
print("\tpython") #Tabulação

#Removendo espaçoes em branco com o strip()

linguagem_favorita = "\n\tC"
print(linguagem_favorita.strip()) #Também existe o lstrip(left/esquerda) e rstrip(right/direita)

#Removendo prefixos e sufixos

url_aleatoria = "https://mendigo.com"
url_simplificada = url_aleatoria.removeprefix("https://").removesuffix(".com")
print(url_simplificada)

#Evitando erros de sintaxe com strings

mensagem = "Os usuarios de python's gostam de gagau?"
"""
mensagem = 'Os usuarios de python's gostam de gagau?' 
(Essa mensagem daria erro pois para usar apostrofo não se pode utilizar string com aspas simples)
"""
print(mensagem,", (NÃO!)")

