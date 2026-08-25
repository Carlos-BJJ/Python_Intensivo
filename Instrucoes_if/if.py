jogos = ["gta", "rdr2", "minecraft", "csgo"]

for jogo in jogos:
    if jogo == "csgo":
        print(jogo.upper())
    else:
        print(jogo.lower())

#Ignorando letras maiusculas e minusculas ao verificar igualdade

bicho = "Gato"
print(bicho == "gato") #False

bicho2 = "Cachorro"
print(bicho2.lower() == "cachorro") #True

#verificando se um valor não está na lista

jogos = ["gta", "rdr2", "minecraft", "csgo"]
rlk = "PlantsVsZombie"

if rlk not in jogos:   
    print(f"O jogo {rlk.title()} não está na lista")