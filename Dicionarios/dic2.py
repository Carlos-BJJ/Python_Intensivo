#usando get( para acessar valores)
alien_0 = {'color': 'green', 'speed': 'slow', 'speed': 'slow'}

#print(alien_0[points]), essa linha daria erro pois não existe a chave points, então o ideal seria procurar a chave usando o método get

# dicionario.get(chave desejada, mensagem caso não encontre)
#Caso não coloque o segundo argumento aparecerá apenas none (Não exite oq vc procura)

print(alien_0.get('points',))
print(alien_0.get('points', "Chave não encontrada"))

#Percorrendo um dicionario com um loop
#1. Percorrendo todos os pares chave-valor com um loop

for chave, valor in alien_0.items(): #O metodo items retorna um par de chave-valor
    print(f"\nkey : {chave}")
    print(f"value : {valor}") 

#2. Percorrendo todos as chaves com um loop (O loop também pode ser feito sem o método keys, pois por padrão o loop lê somente as chaves do dicionario).

for chave in alien_0.keys(): #O metodo keys retorna a chave do dicionario 
    print(f"\nchave : {chave}")

#3. Percorrendo as chaves com um loop em uma ordem especifica (Usando o método sorted)

for chave in sorted(alien_0):
    print(f"\nchave : {chave}") 

#4. Percorrendo todos os valores com um loop 
#Usei o método set() para remover valores duplicados 
for valor in set(alien_0.values()): #O metodo values retorna o valor do dicionario
    print(valor) 