#Trabalhando com dicionarios

alien_0 = {"cor": "verde", "pontos": "5"}
print(alien_0["cor"])
print(alien_0["pontos"])

#Adicionando novos pares chave-valor

alien_0["x_posicao"] = 25
alien_0["y_posicao"] = 50

print(alien_0)

#Modificando valores

alien_0["cor"] = "amarelo"
print(alien_0)

#Velocidade do alien
alien_0["velocidade"] = "medio"

if alien_0["velocidade"] == "devagar":
    x_incremento = 1

elif alien_0["velocidade"] == "medio":
    x_incremento = 2 

else:
    x_incremento = 3

alien_0["x_posicao"] = alien_0["x_posicao"] + x_incremento #Posicao nova = posicao antiga + incremento

#Removendo pares chave-valor

del alien_0["pontos"]
print(alien_0)
