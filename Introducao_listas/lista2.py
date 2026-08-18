times = ["botafogo", "varmengo", "vasco", "fluminense", "america"]

#Ordenando a lista permanentemente 
#(Ordena em ordem alfabetica, podendo ser normal ou reversa)

times.sort()
print(times)

times.sort(reverse=True)
print(times)

#Ordenando uma lista temporariamente

print(sorted(times))

#Exibindo uma lista em ordem inversa (Não necessariamente em ordem alfabetica)

letras = ["a", "c", "d", "y"]
print(letras)

letras.reverse()
print(letras)

#Tamanho da lista

print(len(times))

#índice -1 retorna o ultimo item da lista
#(Exceto em lista vazias, ocasionando erros.)

print(letras[-1])